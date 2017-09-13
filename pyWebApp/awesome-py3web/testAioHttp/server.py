from aiohttp import web

async def hello(request):
    return web.Response(text='hello,world')

app=web.Application()
app.router.add_get('/',hello)

def init_func(argv):
    app = web.Application()
    app.router.add_get("/",index_handler)
    return app

async def handler(request):
    return web.Response()

web.run_app(app)
