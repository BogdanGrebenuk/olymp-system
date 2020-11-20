from typing import List

from sqlalchemy.sql import select

from app.core.solution.domain.entity import Solution as SolutionEntity
from app.db.common import Mapper
from app.db.entities import (
    Contest as ContestEntity,
    Team as TeamEntity
)

from app.db.models import (
    Solution as SolutionModel,
    Task as TaskModel,
)


class SolutionMapper(Mapper):

    async def get_all_from_contest(
            self, contest: ContestEntity
            ) -> List[SolutionEntity]:
        async with self.engine.acquire() as conn:
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

    async def get_all_from_team(self, team: TeamEntity) -> List[SolutionEntity]:
        async with self.engine.acquire() as conn:
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
