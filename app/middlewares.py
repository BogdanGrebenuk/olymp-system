import logging
from asyncio import gather

from aiohttp import web
from aiopg.sa import Engine
from dependency_injector import containers
from dependency_injector.ext import aiohttp as ext_aiohttp
from jwt.exceptions import ExpiredSignatureError
from marshmallow import ValidationError

from containers import application_container
from db import mappers_container
from exceptions import OlympException
from resources import resources_map
from utils.token import token_services_container
from utils.token import TokenDecoder
from utils.token import InvalidTokenContent


logger = logging.getLogger(__name__)


@web.middleware
async def error_handler(request, handler):
    try:
        response = await handler(request)
        return response
    except ValidationError as e:
        return web.json_response(
            {
                'error': 'Validation error',
                'payload': e.messages
            },
            status=400
        )
    except OlympException as e:
        return web.json_response(
            {
                'error': e.message,
                'payload': e.payload
            },
            status=e.HTTP_STATUS
        )
    except Exception as e:
        logger.exception(f"Unexpected exception")
        return web.json_response(
            {'error': 'Something went wrong..'},
            status=500
        )


@web.middleware
async def request_logger(request, handler):
    logger.info(f"{request.method} {request.rel_url}")
    response = await handler(request)
    return response


@web.middleware
async def user_injector(
        request,
        handler,
        token_extractor,
        token_decoder: TokenDecoder,
        user_mapper,
        engine: Engine
        ):
    rel_url = str(request.rel_url)
    if not rel_url.startswith('/api'):
        return await handler(request)

    if request.method == 'OPTIONS':
        return await handler(request)

    token = token_extractor.extractor(request)
    try:
        payload = await token_decoder.decode(token)
    except ExpiredSignatureError:
        return web.json_response({
            'error': 'Token signature has expired! Log in again',
            'payload': {}
        }, status=400)

    user_id = payload.get('user_id')
    user = await user_mapper.get(engine, user_id)
    if user is None:
        raise InvalidTokenContent('token contains invalid information')

    request['user'] = user
    return await handler(request)


@web.middleware
async def request_validator(
        request,
        handler,
        resources_map
        ):
    if request.method == 'OPTIONS':
        return await handler(request)

    resource = resources_map.get(
        (
            request.method,
            request.match_info.route.resource.canonical
        )
    )
    if resource is None:
        return await handler(request)  # pass request ro resolver for 404
    if resource.validators:
        await gather(*[
            validator.validate(request)
            for validator in resource.validators
        ])
    return await handler(request)


middlewares_container = containers.DynamicContainer()
middlewares_container.error_handler = ext_aiohttp.Middleware(
    error_handler
)
middlewares_container.request_logger = ext_aiohttp.Middleware(
    request_logger
)
middlewares_container.user_injector = ext_aiohttp.Middleware(
    user_injector,
    token_extractor=token_services_container.token_extractor,
    token_decoder=token_services_container.token_decoder,
    user_mapper=mappers_container.user_mapper,
    engine=application_container.engine
)
middlewares_container.request_validator = ext_aiohttp.Middleware(
    request_validator,
    resources_map=resources_map
)
