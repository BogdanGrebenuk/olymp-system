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


def extract_from(source_key):
    def inner(request, request_attr):
        source = request.get(source_key)
        if source is None:
            return None
        return source.get(request_attr)
    return inner


default_extractor = partial(
    extract_attr,

    extractors=[
        extract_from('body'),
        extract_from('params'),
        extract_from('vars')
    ]
)
