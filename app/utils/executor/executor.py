import asyncio
from functools import partial


class Executor:

    def __init__(self, pool, loop=None):
        if loop is None:
            loop = asyncio.get_running_loop()
        self.pool = pool
        self.loop = loop

    async def run(self, function, *args, **kwargs):
        task = partial(function, *args, **kwargs)
        return await self.loop.run_in_executor(self.pool, task)


async def run(task, pool, *, loop=None):
    if loop is None:
        loop = asyncio.get_running_loop()
    return await loop.run_in_executor(pool, task)
