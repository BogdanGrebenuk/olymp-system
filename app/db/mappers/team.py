from typing import List, Union

from app.core.team_member import MemberStatus
from app.db.common import Mapper
from app.db.entities import (
    Team as TeamEntity,
    TeamMember as TeamMemberEntity,
)
from app.core.contest.domain.entity import Contest as ContestEntity
from app.db.models import (
    Team as TeamModel,
    TeamMember as TeamMemberModel,
)


class TeamMapper(Mapper):


    async def get_members(
            self,
            team: TeamEntity,
            status: Union[MemberStatus, None] = None
            ) -> List[TeamMemberEntity]:
        """Get all members of team

        If status isn't specified, return members with any status
        """
        async with self.engine.acquire() as conn:
            select_query = TeamMemberModel.select()
            where = TeamMemberModel.c.team_id == team.id
            if status is not None:
                where = where & (TeamMemberModel.c.status == status.value)

            result = await conn.execute(select_query.where(where))
            return [TeamMemberEntity(**i) for i in await result.fetchall()]

    async def get_contest(
            self,
            team: TeamEntity
            ) -> ContestEntity:
        from app.db import mappers_container
        contest = await mappers_container.contest_mapper().get(self.engine, team.contest_id)
        return contest

# create = partial(_create, model=TeamModel)
#
#
# get = partial(_get, model=TeamModel, entity=TeamEntity)


# async def get_members(
#         engine,
#         team: TeamEntity,
#         status: Union[MemberStatus, None] = None
#         ) -> List[TeamMemberEntity]:
#     """Get all members of team
#
#     If status isn't specified, return members with any status
#     """
#     async with engine.acquire() as conn:
#         select_query = TeamMemberModel.select()
#         where = TeamMemberModel.c.team_id == team.id
#         if status is not None:
#             where = where & (TeamMemberModel.c.status == status.value)
#
#         result = await conn.execute(select_query.where(where))
#         return [TeamMemberEntity(**i) for i in await result.fetchall()]
#
#
# async def get_contest(engine, team: TeamEntity) -> ContestEntity:
#     contest = await contest_mapper.get(engine, team.contest_id)
#     return contest
