import enum
from functools import wraps

from aiohttp import web


class BodyType(enum.Enum):
    FORM_DATA = 'FormData'
    JSON = 'JSON'


class UserRole(enum.Enum):
    PARTICIPANT = 'participant'
    TRAINER = 'trainer'
    ORGANIZER = 'organizer'


async def get_body(request, body_type):
    if body_type == BodyType.JSON:
        return await request.json()
    elif body_type == BodyType.FORM_DATA:
        return await request.post()
    raise ValueError(f'unsupported body_type: {body_type}')


def validate_body(function=None, *, schema, body_type=BodyType.JSON):
    if function is None:
        return lambda func: validate_body(
            func,
            schema=schema,
            body_type=body_type
        )

    @wraps(function)
    async def wrapper(request):
        raw_body = await get_body(request, body_type)
        body = schema().load(raw_body)
        request['body'] = body
        return await function(request)
    return wrapper


def check_permission(function=None, *, roles):
    if function is None:
        return lambda func: check_permission(func, roles=roles)

    @wraps(function)
    async def wrapper(request):
        role = request['user'].role
        if role not in roles:
            return web.json_response(
                {
                    'error': "you don't have permissions for this resource!",
                    'payload': {}
                },
                status=403
            )
        return await function(request)
    return wrapper
