import aiopg.sa
from dependency_injector import providers


async def init_pg(app):
    container = app['container']
    config = container.config()
    database_info = config['database']
    engine = await aiopg.sa.create_engine(
        database=database_info['name'],
        user=database_info['user'],
        password=database_info['password'],
        host=database_info['host'],
        port=database_info['port']
    )
    container.engine.provided_by(
        providers.Object(engine)
    )
    app['db'] = engine
    app['engine'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()
