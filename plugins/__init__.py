from aiohttp import web
from .route import routes


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app





# Tech freak 
# Don't Remove Credit!!!
# Telegram Channel @Team_TD_Links
# Developer @Team_TD_Links
