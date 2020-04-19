from aiohttp import web

from db.utils import init_pg, close_pg
from commandbus import Bus
from middlewares import error_middleware
from routes import setup_routes
from settings import config


if __name__ == '__main__':
    app = web.Application(
        middlewares=[error_middleware]
    )

    setup_routes(app)
    app['config'] = config
    app['bus'] = Bus.from_default()
    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)

    host = config['app']['host']
    port = config['app']['port']

    web.run_app(app, host=host, port=port)
