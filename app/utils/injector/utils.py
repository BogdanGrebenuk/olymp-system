from asyncio import gather
from functools import wraps, partial


def inject(*injectors):
    def decorator(function):
        @wraps(function)
        async def wrapper(request):
            await gather(*[inj.resolve(request) for inj in injectors])
            return await function(request)
        return wrapper
    return decorator


def extract_attr(request, request_attr, extractors=None):
    if extractors is None:
        extractors = []
    for extractor in extractors:
        value = extractor(request, request_attr)
        if value is not None:
            return value
    return None


default_extractor = partial(
    extract_attr,

    extractors=[
        lambda request, request_attr: request['body'].get(request_attr),
        lambda request, request_attr: request['params'].get(request_attr),
        lambda request, request_attr: request['vars'].get(request_attr)
    ]
)
