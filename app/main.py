from functools import partial

import aiohttp_cors
from aiohttp import web

from db.utils import init_pg, close_pg
from commandbus import Bus
from middlewares import error_middleware
from routes import setup_routes
from settings import config
from utils.executor import init_pools, close_pools


if __name__ == '__main__':
    app = web.Application(middlewares=[error_middleware])

    setup_routes(app)

    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
            allow_methods="*"
        )
    })

    for route in app.router.routes():
        cors.add(route)

    app['config'] = config
    app['bus'] = Bus.from_default()

    app.on_startup.append(partial(init_pg, config=config))
    app.on_startup.append(init_pools)

    app.on_cleanup.append(close_pg)
    app.on_cleanup.append(close_pools)

    host = config['app']['host']
    port = config['app']['port']

    web.run_app(app, host=host, port=port)
