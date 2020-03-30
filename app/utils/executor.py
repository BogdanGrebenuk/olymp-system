import asyncio
import concurrent.futures


async def io_bound(task):
    loop = asyncio.get_running_loop()
    pool = concurrent.futures.ThreadPoolExecutor()
    try:
        result = await loop.run_in_executor(pool, task)
        return result
    finally:
        pool.shutdown(wait=True)  # TODO: investigate exception when wait is set to False


async def cpu_bound(task):
    loop = asyncio.get_running_loop()
    pool = concurrent.futures.ProcessPoolExecutor()
    try:
        result = await loop.run_in_executor(pool, task)
        return result
    finally:
        pool.shutdown(wait=True)
