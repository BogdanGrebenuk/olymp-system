from dataclasses import dataclass, asdict

import sqlalchemy as sa


@dataclass
class Entity:

    def to_dict(self):
        return asdict(self)


class Mapper:

    def __init__(self, engine, model, entity_cls):
        self.engine = engine
        self.model = model
        self.entity_cls = entity_cls

    async def create(self, entity: Entity):
        async with self.engine.acquire() as conn:
            return await conn.execute(
                self.model
                    .insert()
                    .values(entity.to_dict())
            )

    async def get(self, id):
        async with self.engine.acquire() as conn:
            result = await (
                await conn.execute(
                    self.model
                        .select()
                        .where(self.model.c.id == id)
                )
            ).fetchone()
            if result is None:
                return None
            # TODO: it would be better if 'get' method raises an exception
            return self.entity_cls(**result)

    async def get_all(self):
        async with self.engine.acquire() as conn:
            result = await conn.execute(self.model.select())
            return [self.entity_cls(**i) for i in await result.fetchall()]

    async def update(self, entity):
        async with self.engine.acquire() as conn:
            return await conn.execute(
                sa
                    .update(self.model)
                    .values(entity.to_dict())
                    .where(self.model.c.id == entity.id)
            )

    async def delete(self, entity):
        async with self.engine.acquire() as conn:
            return await conn.execute(
                self.model
                    .delete()
                    .where(self.model.c.id == entity.id)
            )


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
