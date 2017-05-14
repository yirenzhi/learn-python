#-*-coding:utf-8-*-

from flask import Flask ,render_template ,request ,session ,redirect ,url_for ,escape

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route('/hello')
def hello():
    return 'Hello '

# 变量规则
# 要给 URL 添加变量部分，你可以把这些特殊的字段标记为 <variable_name> ，
# 这个部分将会作为命名参数传递到你的函数。规则可以用 <converter:variable_name> 指定一个可选的转换器。这里有一些不错的例子:
@app.route('/user/<username>')
def show_user_profile(username):
    return 'Hello %s' % username

@app.route('/post/<int:postid>')
def show_postid(postid):
    return 'post %d' % postid

# 转换器有下面几种：
#
# int	接受整数
# float	同 int ，但是接受浮点数
# path	和默认的相似，但也接受斜线


# 如果 Flask 能匹配 URL，那么 Flask 可以生成它们吗？当然可以。你可以用 url_for() 来给指定的函数构造 URL。
# 它接受函数名作为第一个参数，也接受对应 URL 规则的变量部分的命名参数。未知变量部分会添加到 URL 末尾作为查询参数。这里有一些例子:
# >>> from flask import Flask, url_for
# >>> app = Flask(__name__)
# >>> @app.route('/')
# ... def index(): pass
# ...
# >>> @app.route('/login')
# ... def login(): pass
# ...
# >>> @app.route('/user/<username>')
# ... def profile(username): pass
# ...
# >>> with app.test_request_context():
# ...  print url_for('index')
# ...  print url_for('login')
# ...  print url_for('login', next='/')
# ...  print url_for('profile', username='John Doe')
# ...
# /
# /login
# /login?next=/
# /user/John%20Doe

# HTTP 方法
# HTTP （与 Web 应用会话的协议）有许多不同的访问 URL 方法。默认情况下，
# 路由只回应 GET 请求，但是通过 route() 装饰器传递 methods 参数可以改变这个行为。这里有一些例子:

'''
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
'''
# 模板渲染
# 用 Python 生成 HTML 十分无趣，而且相当繁琐，因为你必须手动对 HTML 做转义来保证应用的安全。为此，Flask 配备了 Jinja2 模板引擎。
#
# 你可以使用 render_template() 方法来渲染模板。你需要做的一切就是将模板名和你想作为关键字的参数传入模板的变量。这里有一个展示如何渲染模板的简例:

@app.route('/hellohtml/')
@app.route('/hellohtml/<name>')
def hellohtml(name=None):
    return render_template('hello.html',name=name)

# 当前请求的 HTTP 方法可通过 method 属性来访问。通过:attr:~flask.request.form
# 属性来访问表单数据（ POST 或 PUT 请求提交的数据）。这里有一个用到上面提到的那两个属性的完整实例:
# @app.route('/login',methods=['POST','GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if variable_login(request.form['username'],request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#
#     return render_template('login.html',error=error)

@app.route('/upload',methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.sava('/var/www/uploads/uploaded_file.txt')

# 会话
# 除请求对象之外，还有一个 session 对象。它允许你在不同请求间存储特定用户的信息。它是在 Cookies 的基础上实现的，
# 并且对 Cookies 进行密钥签名。这意味着用户可以查看你 Cookie 的内容，但却不能修改它，除非用户知道签名的密钥。
#
# 要使用会话，你需要设置一个密钥。这里介绍会话如何工作:


@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))

app.secret_key = '\xcd\xbe\x1c`\xf1K\xd9\x17\xf7q\x93pcg\x9f$\xf2#K\x01\x8a\xb2\r\xfa'












if __name__ == '__main__':
    app.run(debug=True)
