from functools import partial
from typing import List

from sqlalchemy.sql import select

from app.db.common import (
    create as _create,
    get as _get,
    get_all as _get_all,
    update as _update
)
from app.db.entities import (
    Solution as SolutionEntity,
    Team as TeamEntity
)
from app.core.contest.domain.entity import Contest as ContestEntity
from app.db.models import (
    Solution as SolutionModel,
    Task as TaskModel,
)


create = partial(_create, model=SolutionModel)


get = partial(_get, model=SolutionModel, entity=SolutionEntity)


get_all = partial(_get_all, model=SolutionModel, entity=SolutionEntity)


update = partial(_update, model=SolutionModel)


async def get_team(engine, solution: SolutionEntity) -> TeamEntity:
    from app.db import team_mapper  # TODO: investgate what can i do with it
    return await team_mapper.get(engine, solution.team_id)


async def get_all_from_contest(
        engine,
        contest: ContestEntity
        ) -> List[SolutionEntity]:
    async with engine.acquire() as conn:
        join = (
            SolutionModel
            .join(
                TaskModel,
                SolutionModel.c.task_id == TaskModel.c.id
            )
        )
        result = await conn.execute(
            select([SolutionModel])
            .select_from(join)
            .where(
                TaskModel.c.contest_id == contest.id
            )
        )
        return [
            SolutionEntity(**i)
            for i in await result.fetchall()
        ]


async def get_all_from_team(engine, team: TeamEntity) -> List[SolutionEntity]:
    async with engine.acquire() as conn:
        result = await conn.execute(
            SolutionModel
            .select()
            .where(
                SolutionModel.c.team_id == team.id
            )
        )
        return [
            SolutionEntity(**i)
            for i in await result.fetchall()
        ]
