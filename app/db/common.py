import sqlalchemy as sa
from dataclasses import asdict


async def create(engine, entity, model):
    async with engine.acquire() as conn:
        await conn.execute(
            model.insert().values(asdict(entity))
        )


async def get(engine, id, entity, model):
    async with engine.acquire() as conn:
        result = await (await conn.execute(
            model.select().where(model.c.id == id)
        )).fetchone()
        if result is None:
            return None  # TODO: raise an exception
        return entity(**result)


async def get_all(engine, entity, model):
    async with engine.acquire() as conn:
        result = await conn.execute(model.select())
        return [entity(**i) for i in await result.fetchall()]


async def update(engine, entity, model):
    async with engine.acquire() as conn:
        return await conn.execute(
            sa.update(model)
            .values(asdict(entity))
            .where(model.c.id == entity.id)
        )


async def delete(engine, entity, model):
    async with engine.acquire() as conn:
        return await conn.execute(
            model
            .delete()
            .where(model.c.id == entity.id)
        )
