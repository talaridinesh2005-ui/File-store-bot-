from aiohttp import web
from .route import routes


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app





# @TD_Public_Bots
# Don't Remove Credit!!!
#YouTube channel link https://youtube.com/@tdbotdev?si=j3HVY4E69-C4ZDcw
# Telegram Channel @TD_Public_Bots
# Developer @TD_Public_Bots
