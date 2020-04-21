from typing import List

from db.common import create, get
from db.entities.contest import Contest as ContestEntity
from db.entities.task import Task as TaskEntity
from db.models import (
    Contest as ContestModel,
    Task as TaskModel
)


async def create_contest(engine, contest: ContestEntity):
    return await create(engine, contest, ContestModel)


async def get_contest(engine, id) -> ContestEntity:
    result = await get(engine, id, ContestModel)
    if result is None:
        return None
    return ContestEntity(**result)


async def get_contests(engine) -> List[ContestEntity]:
    async with engine.acquire() as conn:
        result = await conn.execute(ContestModel.select())
        return [ContestEntity(**i) for i in await result.fetchall()]


async def get_tasks(engine, contest: ContestEntity) -> List[TaskEntity]:
    async with engine.acquire() as conn:
        result = await conn.execute(
            TaskModel.select().where(TaskModel.c.contest_id == contest.id)
        )
        return [TaskEntity(**i) for i in await result.fetchall()]
