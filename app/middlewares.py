import logging
from functools import partial

from aiohttp import web
from marshmallow import ValidationError

import utils.executor as executor
from db import user_mapper
from exceptions import OlympException
from exceptions.token import InvalidTokenContent
from exceptions.role import PermissionException
from resources import resources_map
from utils.token import decode_token, get_token


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
async def user_injector(request, handler):
    rel_url = str(request.rel_url)
    if not rel_url.startswith('/api'):
        return await handler(request)

    token = get_token(request)

    pool = request.app['process_pool']
    engine = request.app['db']
    token_config = request.app['config']['token']

    task = partial(
        decode_token,

        token,
        token_config
    )
    payload = await executor.run(task, pool)

    user_id = payload.get('user_id')
    user = await user_mapper.get(engine, user_id)
    if user is None:
        raise InvalidTokenContent('token contains invalid information')

    request['user'] = user
    return await handler(request)


@web.middleware
async def permission_checker(request, handler):
    resource = resources_map.get((request.method, str(request.rel_url)))
    if resource is None:
        return await handler(request)  # pass request ro resolver for 404
    if (
            resource.allowed_roles is not None
            and
            request['user'].get_user_role() not in resource.allowed_roles
            ):
        raise PermissionException(
            "you don't have permissions for this resource!"
        )
    return await handler(request)


@web.middleware
async def request_validator(request, handler):
    resource = resources_map.get((request.method, str(request.rel_url)))
    if resource is None:
        return await handler(request)  # pass request ro resolver for 404
    if resource.validator is not None:
        await resource.validator.validate(request)
    return await handler(request)

