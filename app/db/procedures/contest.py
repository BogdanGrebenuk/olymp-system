from functools import partial
from typing import List

from sqlalchemy.sql import select

from db.common import create as _create, get as _get
from db.entities import (
    Contest as ContestEntity,
    Task as TaskEntity,
    Team as TeamEntity
)
from db.models import (
    Contest as ContestModel,
    Task as TaskModel,
    Team as TeamModel
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


# todo: user_mapper.get_created_teams_by_contest ?
async def get_teams(engine, contest: ContestEntity) -> List[TeamEntity]:
    async with engine.acquire() as conn:
        res = await conn.execute(
            select([TeamModel]).where(TeamModel.c.contest_id == contest.id)
        )
        return [TeamEntity(**i) for i in await res.fetchall()]
