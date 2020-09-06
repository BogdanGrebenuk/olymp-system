from typing import Union

from app.core.user.domain.entity import User as UserEntity
from app.db.common import Mapper
from app.db.entities import (
    Contest as ContestEntity,
    Team as TeamEntity,
    TeamMember as TeamMemberEntity,
)
from app.db.models import TeamMember as TeamMemberModel


class TeamMemberMapper(Mapper):

    def __init__(self, team_mapper, **kwargs):
        super().__init__(**kwargs)
        self.team_mapper = team_mapper

    async def get_team(self, team_member: TeamMemberEntity) -> TeamEntity:
        team = await self.team_mapper.get(self.engine, team_member.team_id)
        return team

    async def get_contest(self, team_member: TeamMemberEntity) -> ContestEntity:
        team = await self.get_team(team_member)
        contest = await self.team_mapper.get_contest(self.engine, team)
        return contest

    async def get_by_user_and_team(
            self,
            user: UserEntity,
            team: TeamEntity
    ) -> Union[TeamMemberEntity, None]:
        async with self.engine.acquire() as conn:
            result = await conn.execute(
                TeamMemberModel.select().where(
                    (TeamMemberModel.c.user_id == user.id)
                    & (TeamMemberModel.c.team_id == team.id)
                )
            )
            entity = await result.fetchone()
            if entity is None:
                return None
            return TeamMemberEntity(**entity)



# create = partial(_create, model=TeamMemberModel)
#
#
# get = partial(_get, model=TeamMemberModel, entity=TeamMemberEntity)
#
#
# update = partial(_update, model=TeamMemberModel)
#
#
# delete = partial(_delete, model=TeamMemberModel)


# async def get_team(engine, team_member: TeamMemberEntity) -> TeamEntity:
#     team = await mappers_container.team_mapper.get(engine, team_member.team_id)
#     return team
#
#
# async def get_contest(engine, team_member: TeamMemberEntity) -> ContestEntity:
#     team = await get_team(engine, team_member)
#     contest = await mappers_container.team_mapper.get_contest(engine, team)
#     return contest
#
#
# async def get_by_user_and_team(
#         engine,
#         user: UserEntity,
#         team: TeamEntity
#         ) -> Union[TeamMemberEntity, None]:
#     async with engine.acquire() as conn:
#         result = await conn.execute(
#             TeamMemberModel.select().where(
#                 (TeamMemberModel.c.user_id == user.id)
#                 & (TeamMemberModel.c.team_id == team.id)
#             )
#         )
#         entity = await result.fetchone()
#         if entity is None:
#             return None
#         return TeamMemberEntity(**entity)
#
#
# async def _get_contest(engine, team_member: TeamMemberEntity) -> ContestEntity:
#     """'get_contest' version with join"""
#     async with engine.acquire() as conn:
#         join = TeamModel.join(
#             ContestModel,
#             TeamModel.c.contest_id == ContestModel.c.id
#         )
#         result = await conn.execute(
#             select([ContestModel])
#             .select_from(join)
#             .where(TeamModel.c.id == team_member.id)
#         )
#         contest = await result.fetchone()
#         # TODO: if we change fk behaviour we must rewrite this section because of possible None
#         return ContestEntity(**contest)
