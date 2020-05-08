import logging.config

from aiohttp import web
from marshmallow import ValidationError


logger = logging.getLogger(__name__)


@web.middleware
async def error_middleware(request, handler):
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
        logger.error(f"Unexpected exception: {e}")
        return web.json_response(
            {'error': 'Something went wrong..'},
            status=500
        )


@web.middleware
async def request_logger(request, handler):
    logger.info(f"{request.method} {request.rel_url}")
    response = await handler(request)
    return response
