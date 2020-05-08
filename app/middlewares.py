import logging
from functools import partial

from aiohttp import web
from marshmallow import ValidationError

import utils.executor as executor
from utils.token import decode_token
from db.procedures.user import (
    get_user
)


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
            status=400)
    except Exception as e:
        logger.exception(f"Unexpected exception")
        return web.json_response(
            {'error': 'Something went wrong..'},
            status=500
        )


@web.middleware
async def user_injector(request, handler):
    rel_url = str(request.rel_url)
    if not rel_url.startswith('/api'):
        return await handler(request)

    token_header = request.headers.get('Authorization')
    if token_header is None:
        return web.json_response({
            'error': 'this action requires a token!',
            'payload': {}
        }, status=400)

    try:
        _, token = token_header.split()
    except ValueError:
        return web.json_response({
            'error': 'invalid token header',
            'payload': {}
        }, status=400)

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
    user = await get_user(engine, user_id)
    if user is None:
        return web.json_response({
            'error': f'token contains invalid information',
            'payload': {}
        }, status=400)

    request['user'] = user
    return await handler(request)


@web.middleware
async def request_logger(request, handler):
    logger.info(f"{request.method} {request.rel_url}")
    response = await handler(request)
    return response
