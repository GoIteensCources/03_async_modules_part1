from aiohttp import web

app = web.Application()


async def handle(request):
    name = request.match_info.get("name", "Anonimus")
    return web.Response(text=f"Hello, {name} from aiohttp!")


app.router.add_route("get", '/', handle)
app.router.add_get('/{name}', handle)

if __name__ == "__main__":
    web.run_app(app, port=8001)
