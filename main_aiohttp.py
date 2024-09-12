from aiohttp import web
import aiohttp

app = web.Application()


async def fetch_data(url):
    """make GET query to url with aiohttp"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def handle(request):
    name = request.match_info.get("name", "Anonimus")
    return web.Response(text=f"Hello, {name} from aiohttp!")


app.router.add_route("get", '/', handle)
app.router.add_get('/{name}', handle)

if __name__ == "__main__":
    web.run_app(app, port=8001)
