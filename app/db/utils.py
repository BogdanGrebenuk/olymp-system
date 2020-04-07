import aiopg.sa

from settings import config


async def init_pg(app):
    database_info = config['database']
    engine = await aiopg.sa.create_engine(
        database=database_info['name'],
        user=database_info['user'],
        password=database_info['password'],
        host=database_info['host'],
        port=database_info['port']
    )
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()
