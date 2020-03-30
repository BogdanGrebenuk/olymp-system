from aiohttp import web

from commandbus import default_bus as bus
from routes import setup_routes
from settings import config


if __name__ == '__main__':
    app = web.Application()
    setup_routes(app)
    app['config'] = config
    app['bus'] = bus
    host = config['app']['host']
    port = config['app']['port']
    web.run_app(app, host=host, port=port)
