from functools import partial
from typing import List

from db.common import create as _create, get as _get
from db.entities.contest import Contest as ContestEntity
from db.entities.task import Task as TaskEntity
from db.models import (
    Contest as ContestModel,
    Task as TaskModel
)


create = partial(_create, model=ContestModel)


get = partial(_get, model=ContestModel, entity=ContestEntity)


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
