import enum
from functools import wraps


class BodyType(enum.Enum):
    FORM_DATA = 'FormData'
    JSON = 'JSON'


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
