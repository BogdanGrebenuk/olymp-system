from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor

from dependency_injector import providers


async def init_pools(app):
    thread_pool = ThreadPoolExecutor()
    process_pool = ProcessPoolExecutor()
    container = app['container']
    container.thread_pool.provided_by(
        providers.Object(thread_pool)
    )
    container.process_pool.provided_by(
        providers.Object(process_pool)
    )
    app['thread_pool'] = thread_pool
    app['process_pool'] = process_pool


async def close_pools(app):
    app['thread_pool'].shutdown(wait=True)
    app['process_pool'].shutdown(wait=True)