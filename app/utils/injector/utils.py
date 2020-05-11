from asyncio import gather

from functools import wraps


def inject(*injectors):
    def decorator(function):
        @wraps(function)
        async def wrapper(request):
            await gather(*[inj.resolve(request) for inj in injectors])
            return await function(request)
        return wrapper
    return decorator
