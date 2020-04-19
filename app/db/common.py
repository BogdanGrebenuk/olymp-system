from dataclasses import asdict


async def create(engine, entity, model):
    async with engine.acquire() as conn:
        await conn.execute(
            model.insert().values(asdict(entity))
        )


async def get(engine, id, model):
    async with engine.acquire() as conn:
        result = await conn.execute(
            model.select().where(model.c.id == id)
        )
        return await result.fetchone()
