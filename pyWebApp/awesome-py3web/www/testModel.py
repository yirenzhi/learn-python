import orm
import asyncio
from models import User, Blog, Comment

loop = asyncio.get_event_loop()

async def test():
    await orm.create_pool(loop, user='zhouda', password='1234', db='awesome')
    u=User(name='Test', email='yiren_zhi@163.com', passwd='123456', image='ablout:blank')
    await u.save()


loop.run_until_complete(test())
loop.close()
