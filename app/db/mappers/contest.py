from typing import List

from sqlalchemy.sql import select

from app.db.common import Mapper
from app.core.contest.domain.entity import Contest as ContestEntity
from app.db.entities import (
    Task as TaskEntity,
    Team as TeamEntity
)
from app.db.models import (
    Task as TaskModel,
    Team as TeamModel
)


class ContestMapper(Mapper):

    async def get_tasks(self, contest: ContestEntity) -> List[TaskEntity]:
        async with self.engine.acquire() as conn:
            result = await conn.execute(
                TaskModel.select().where(TaskModel.c.contest_id == contest.id)
            )
            return [TaskEntity(**i) for i in await result.fetchall()]

    # todo: user_mapper.get_created_teams_by_contest ?
    async def get_teams(self, contest: ContestEntity) -> List[TeamEntity]:
        async with self.engine.acquire() as conn:
            res = await conn.execute(
                select([TeamModel]).where(TeamModel.c.contest_id == contest.id)
            )
            return [TeamEntity(**i) for i in await res.fetchall()]
