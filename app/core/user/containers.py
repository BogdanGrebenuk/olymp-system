import dependency_injector.containers as containers
import dependency_injector.providers as providers
from dependency_injector.ext import aiohttp as ext_aiohttp

from app.containers import application_container
from app.core.user.command_handlers import CreateUserHandler
from app.core.user.controllers import (
    authenticate_user,
    register_user,
    get_user,
    get_users
)

from app.core.user.services import (
    PasswordChecker,
    PasswordGenerator
)
from app.core.user.transformers import UserTransformer
from app.db import mappers_container as mapper_container
from app.utils.token import token_services_container


services = containers.DynamicContainer()
services.password_checker = providers.Singleton(
    PasswordChecker
)
services.password_generator = providers.Singleton(
    PasswordGenerator
)


transformers = containers.DynamicContainer()
transformers.user_transformer = providers.Singleton(
    UserTransformer
)


controllers = containers.DynamicContainer()
controllers.authenticate_user = ext_aiohttp.View(
    authenticate_user,
    password_checker=services.password_checker,
    user_mapper=mapper_container.user_mapper,
    token_generator=token_services_container.token_generator
)
controllers.register_user = ext_aiohttp.View(
    register_user,
    bus=application_container.bus,
    user_mapper=mapper_container.user_mapper,
    transformer=transformers.user_transformer
)
controllers.get_user = ext_aiohttp.View(
    get_user,
    user_mapper=mapper_container.user_mapper,
    user_transformer=transformers.user_transformer
)
controllers.get_users = ext_aiohttp.View(
    get_users,
    user_mapper=mapper_container.user_mapper,
    user_transformer=transformers.user_transformer
)


command_handlers = containers.DynamicContainer()
command_handlers.create_user = providers.Singleton(
    CreateUserHandler,
    hash_client=services.password_generator,
    user_mapper=mapper_container.user_mapper
)
