import aiohttp_cors
from aiohttp import web
from dependency_injector import providers
from dependency_injector.ext import aiohttp as ext_aiohttp

from app.common import PUBLIC_DIR
from app.db.utils import init_pg, close_pg
from app.commandbus import Bus
from app.commandbus.middlewares import Resolver
from app.containers import application_container
from app.core.team.containers import command_handlers as team_command_handlers
from app.core.user.containers import command_handlers as user_command_handlers
from app.middlewares import middlewares_container
from app.resources import setup_routes, resources
from app.settings import config
from app.utils.executor import Executor
from app.utils.executor.utils import init_pools, close_pools
from app.utils.logger import init_logging


def create_app():
    application_container.config.from_dict(config)
    application_container.app.provided_by(
        ext_aiohttp.Application(web.Application)
    )
    application_container.resolver.provided_by(
        providers.Singleton(
            Resolver,
            [
                user_command_handlers,
                team_command_handlers,
            ]
        )
    )
    application_container.bus.provided_by(
        providers.Singleton(
            Bus,
            middlewares=providers.List(
                application_container.resolver
            )
        )
    )
    app = application_container.app(
        middlewares=[
            middlewares_container.error_handler,
            middlewares_container.request_logger,
            middlewares_container.user_injector,
            middlewares_container.request_validator
        ]
    )
    app['container'] = application_container
    app['bus'] = application_container.bus()
    app['config'] = config

    # filling container (engine) inside init_pg
    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)
    # filling container (thread_pool, process_pool) inside init_pools
    app.on_startup.append(init_pools)
    app.on_cleanup.append(close_pools)

    application_container.thread_executor.provided_by(
        providers.Singleton(
            Executor,
            application_container.thread_pool
        )
    )
    application_container.process_executor.provided_by(
        providers.Singleton(
            Executor,
            application_container.process_pool
        )
    )

    init_logging(config["loggers"])

    setup_routes(app, resources)
    app.add_routes([web.static('/public', PUBLIC_DIR)])

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

    return app


if __name__ == '__main__':
    app = create_app()

    host = config['app']['host']
    port = config['app']['port']

    web.run_app(app, host=host, port=port)
