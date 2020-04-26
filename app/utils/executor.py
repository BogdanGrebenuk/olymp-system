import asyncio
from concurrent.futures import (
    ThreadPoolExecutor,
    ProcessPoolExecutor
)


async def run(task, pool, *, loop=None):
    if loop is None:
        loop = asyncio.get_running_loop()
    return await loop.run_in_executor(pool, task)


async def init_pools(app):
    app['thread_pool'] = ThreadPoolExecutor()
    app['process_pool'] = ProcessPoolExecutor()


async def close_pools(app):
    app['thread_pool'].shutdown(wait=True)
    app['process_pool'].shutdown(wait=True)
