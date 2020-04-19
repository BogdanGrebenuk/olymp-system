from functools import wraps


def validate_body(function=None, *, schema):
    if function is None:
        return lambda func: validate_body(func, schema=schema)

    @wraps(function)
    async def wrapper(request):
        raw_body = await request.json()
        body = schema().load(raw_body)
        request['body'] = body
        return await function(request)
    return wrapper
