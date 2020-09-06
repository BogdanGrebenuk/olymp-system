import dependency_injector.containers as containers
import dependency_injector.providers as providers
from dependency_injector.ext import aiohttp as ext_aiohttp

from app.containers import application_container
from app.core.contest.command_handlers import CreateContestHandler
from app.core.contest.controllers import (
    create_contest,
    get_contest,
    get_contests,
    get_leader_board
)
from app.core.contest.services import ImagePathGenerator
from app.core.contest.transformers import ContestTransformer
from app.db import mappers_container as mapper_container
from app.utils.transformer import transformer_container
from app.utils.resolver import resolvers_container as resolver_container

services = containers.DynamicContainer()
services.image_path_generator = providers.Singleton(
    ImagePathGenerator
)

transformers = containers.DynamicContainer()
transformers.contest_transformer = providers.Singleton(
    ContestTransformer,
    datetime_transformer=transformer_container.datetime_transformer
)

controllers = containers.DynamicContainer()
controllers.create_contest = ext_aiohttp.View(
    create_contest,
    bus=application_container.bus,
    engine=application_container.engine,
    thread_pool=application_container.thread_pool,
)
controllers.get_contest = ext_aiohttp.View(
    get_contest,
    contest_resolver=resolver_container.contest_resolver,
    contest_transformer=transformers.contest_transformer
)
controllers.get_contests = ext_aiohttp.View(
    get_contests,
    contest_mapper=mapper_container.contest_mapper,
    contest_transformer=transformers.contest_transformer
)
controllers.get_leader_board = ext_aiohttp.View(
    get_leader_board,
    contest_resolver=resolver_container.contest_resolver,
    contest_mapper=mapper_container.contest_mapper,
    engine=application_container.engine
)

command_handlers = containers.DynamicContainer()
command_handlers.create_contest = providers.Singleton(
    CreateContestHandler,
    engine=application_container.engine,
    executor=application_container.process_executor,
    thread_pool=application_container.thread_pool,
    bus=application_container.bus,
    contest_mapper=mapper_container.contest_mapper,
    image_path_generator=services.image_path_generator
)
