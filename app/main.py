from aiohttp import web

from db.utils import init_pg, close_pg
from commandbus import get_bus
from routes import setup_routes
from settings import config


if __name__ == '__main__':
    app = web.Application()

    setup_routes(app)
    app['config'] = config
    app['bus'] = get_bus('default')
    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)

    host = config['app']['host']
    port = config['app']['port']
    web.run_app(app, host=host, port=port)
