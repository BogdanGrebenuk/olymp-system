from aiohttp import web
from marshmallow import ValidationError


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
        # TODO: logger!
        print(f'FATAL EXCEPTION:', e)
        return web.json_response(
            {'error': 'Something went wrong..'},
            status=500
        )
