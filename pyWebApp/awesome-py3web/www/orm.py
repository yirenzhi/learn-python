#coding=utf-8

import asyncio, logging, aiomysql


'''
创建连接池

我们需要创建一个全局的连接池，每个HTTP请求都可以从连接池中直接获取数据库连接。使用连接池的好处是不必频繁地打开和关闭数据库连接，而是能复用就尽量复用。

连接池由全局变量__pool存储，缺省情况下将编码设置为utf8，自动提交事务：
'''

@asyncio.coroutine
def create_pool(loop,**kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = yield from aiomysql.create_pool(
        host = kw.get('host','localhost'),
        port = kw.get('',3306),
        user = kw['user'],
        password = kw['password'],
        db = kw['db'],
        charset = kw.get('charset','utf8'),
        autocommit = kw.get('maxsize',10),
        minsize = kw.get('minsize',1),
        loop = loop
    
    )
    
'''
用于执行select语句
'''
@asyncio.coroutine
def select(sql.args.size=None):
    log(sql,args)
    global __pool
    with(yield from __pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql.replace('?','%s',args or ()))
        if size:
            rs = yield from cur.fetchmany(size)
        else:
            rs = yield from cur.fetchall()
        yield from cur.close()
        logging.info('rows returned:%s' % len(rs))
        return rs
    
'''
通用的execute()用来执行insert,update,delete
'''   
@asyncio.coroutine
def execute(sql, args):
    log(sql)
    with(yield from __pool) as conn:
        try:
            cur = yield from conn.cursor()
            yield from cur.execute(sql.replace('?','%s'),args)
            affected = cur.rowcount
            yield from cur.close()
        except BaseException as e:
            raise
        return affected
    
    
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        #获取table名称
        tableName = attrs.get('__table__', None) or name
        logging.info('found model: %s (table: %s)' % (name, tableName))
        #获取所有的Field和主键名：
        mappings = dict()
        fields = []
        primarykey = None

        for k, v in attrs.item():
            if isinstance(v, Field):
                logging.info('  found mapping: %s ==> %s' % (k,v))
                mappings[k] = v
                if v.primary_key:
                    #找到主键
                    if primarykey:
                        raise RuntimeError('Duplicate primary key for field: %s' % k)
                    primarykey = k
                else:
                    field.append(k)

        if not primarykey:
            raise RuntimeError('Primary key not found.')

        for k in mappings.keys():
            attrs.pop(k)
        escaped_fields = list(map(lambda f: '`%s`' % f, fields))
        attrs['__mappings__'] = mappings #保存属性和列的映射关系
        attrs['__table__'] = tableName
        attrs['__primary_key__'] = primaryKey #主键属性名
        attrs['__fields__'] = fields #出主键外的属性名
        #构造默认的SELECT, INSERT, UPDATE, DELETE语句：
        attrs['__select__'] = 'select `%s`, %s from `%s`' % (primarykey, ','.join(escaped_fields), tableName)
        attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (tableName, ','.join(escaped_fields), primarykey, create_args_string(len(escaped_fields) + 1))
        attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (tableName, ','.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primarykey)
        attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName, primarykey)
        return type.__new__(cls, name, bases, attrs)



        

class Model(dict, metaclass = ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def getValue(self, key):
        return getattr(self, key, None)

    def getValueOrDefault(self, key):
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]
            if field.default is not None:
                value = field.default() if callable(field.default) else field.default
                logging.debug('using default value for %s : %s' % (key, str(value)))
                setattr(self,key, value)
        return value

    @classmethod
    async def find(cls, pk):
        'find object by primary key.'
        rs = yield from select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__),[pk], 1)
        if len(rs) == 0:
            return None
        return cls(**rs[0])

    async def save(self):
        args = lsit(map(self.getValueOrDefault, self.__fields__))
        args.append(self.getValueOrDefault(self.__primary_key__))
        rows = yield from excute(self.__insert__, args)
        if rows != 1:
            logging.warn("failed to insert record: affected rows: %s" % rows)

class Field(object):
    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, slef.column_type, self.name)


class StringField(Field):
    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
        super().__init__(name, ddl, primary_key, default)