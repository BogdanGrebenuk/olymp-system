from concurrent.futures import (
    ThreadPoolExecutor,
    ProcessPoolExecutor
)
from logging import Logger

from aiohttp import web
from aiopg.sa import Engine
from dependency_injector import providers, containers

from app.commandbus import Bus
from app.commandbus.middlewares import Resolver
from app.utils.executor import Executor


application_container = containers.DynamicContainer()
application_container.config = providers.Configuration()
application_container.engine = providers.Dependency(
    instance_of=Engine
)
application_container.app = providers.Dependency(
    instance_of=web.Application
)
application_container.resolver = providers.Dependency(
    instance_of=Resolver
)
application_container.bus = providers.Dependency(
    instance_of=Bus
)
application_container.thread_pool = providers.Dependency(
    instance_of=ThreadPoolExecutor
)
application_container.process_pool = providers.Dependency(
    instance_of=ProcessPoolExecutor
)
application_container.thread_executor = providers.Dependency(
    instance_of=Executor
)
application_container.process_executor = providers.Dependency(
    instance_of=Executor
)
application_container.middleware_logger = providers.Dependency(
    instance_of=Logger
)
