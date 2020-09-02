from typing import Union, List

from sqlalchemy.sql import select, exists

from app.core.team_member import MemberStatus
from app.core.user.domain.entity import User as UserEntity
from app.db.common import Mapper
from app.db.entities import (
    Contest as ContestEntity,
    Team as TeamEntity,
    TeamMember as TeamMemberEntity
)
from app.db.models import (
    Team as TeamModel,
    TeamMember as TeamMemberModel
)


class UserMapper(Mapper):

    async def get_user_by_email(self, email: str) -> Union[UserEntity, None]:
        async with self.engine.acquire() as conn:
            result = await conn.execute(
                self.model
                    .select()
                    .where(self.model.c.email == email)
            )
            entity = await result.fetchone()
            if entity is None:
                return None
            return self.entity_cls(**entity)

    # TODO: remove to team_mapper?
    async def get_accepted_team_for_contest(
            self,
            user: UserEntity,
            contest: ContestEntity
            ) -> Union[TeamEntity, None]:
        async with self.engine.acquire() as conn:
            join = (
                TeamModel
                .join(
                    TeamMemberModel,
                    TeamModel.c.id == TeamMemberModel.c.team_id
                )
            )
            result = await conn.execute(
                select([TeamModel])
                .select_from(join)
                .where(
                    (TeamModel.c.contest_id == contest.id)
                    & (TeamMemberModel.c.user_id == user.id)
                    & (TeamMemberModel.c.status == MemberStatus.ACCEPTED.value)
                )
            )
            team = await result.fetchone()
            if team is None:
                return None
            return TeamEntity(**team)

    # TODO: remove to team_member mapper
    async def get_received_invites_for_contest(
            self,
            user: UserEntity,
            contest: ContestEntity
            ) -> List[TeamMemberEntity]:
        async with self.engine.acquire() as conn:
            join = (
                TeamMemberModel
                .join(
                    TeamModel,
                    TeamModel.c.id == TeamMemberModel.c.team_id
                )
            )

            result = await conn.execute(
                select([TeamMemberModel])
                .select_from(join)
                .where(
                    (TeamModel.c.contest_id == contest.id)
                    & (TeamMemberModel.c.user_id == user.id)
                    & (TeamMemberModel.c.status == 'pending')
                )
            )

            rows = await result.fetchall()
            return [TeamMemberEntity(**i) for i in rows]

    # TODO: remove to team_member mapper?
    async def get_sent_invites_for_contest(
            self,
            user: UserEntity,
            contest: ContestEntity
            ) -> List[TeamMemberEntity]:
        async with self.engine.acquire() as conn:
            join = (
                TeamMemberModel
                .join(
                    TeamModel,
                    TeamModel.c.id == TeamMemberModel.c.team_id
                )
            )

            result = await conn.execute(
                select([TeamMemberModel])
                .select_from(join)
                .where(
                    (TeamModel.c.contest_id == contest.id)
                    & (TeamModel.c.trainer_id == user.id)
                )
            )

            rows = await result.fetchall()
            return [TeamMemberEntity(**i) for i in rows]

    # TODO: remove to team mapper?
    async def get_created_teams_by_contest(
            self,
            contest: ContestEntity,
            creator: Union[UserEntity, None] = None
            ) -> List[TeamEntity]:
        async with self.engine.acquire() as conn:
            if creator is None:
                where = TeamModel.c.contest_id == contest.id
            else:
                where = (
                    (TeamModel.c.trainer_id == creator.id)
                    & (TeamModel.c.contest_id == contest.id)
                )
            result = await conn.execute(
                TeamModel.select().where(where)
            )
            return [TeamEntity(**i) for i in await result.fetchall()]

    async def is_registered_for_contest_as_participant(
            self,
            user: UserEntity,
            contest: ContestEntity
            ) -> bool:
        async with self.engine.acquire() as conn:
            join = TeamMemberModel.join(
                TeamModel,
                TeamMemberModel.c.team_id == TeamModel.c.id,
            )
            where = (
                (TeamMemberModel.c.user_id == user.id)
                & (TeamModel.c.contest_id == contest.id)
                & (TeamMemberModel.c.status == MemberStatus.ACCEPTED.value)
            )
            query = (
                select([TeamMemberModel])
                .select_from(join)
                .where(where)
            )
            result = await conn.execute(select([exists(query)]))
            return await result.scalar()

    async def is_registered_for_contest_as_trainer(
            self,
            user: UserEntity,
            contest: ContestEntity
            ) -> bool:
        async with self.engine.acquire() as conn:
            query = (
                TeamModel
                .select()
                .where(
                    (TeamModel.c.contest_id == contest.id)
                    & (TeamModel.c.trainer_id == user.id)
                )
            )
            result = await conn.execute(
                select([exists(query)])
            )
            return await result.scalar()

    async def is_registered_for_team_as_participant(
            self,
            user: UserEntity,
            team: TeamEntity
            ) -> bool:
        async with self.engine.acquire() as conn:
            query = (
                TeamMemberModel
                .select()
                .where(
                    (TeamMemberModel.c.user_id == user.id)
                    & (TeamMemberModel.c.team_id == team.id)
                    & (TeamMemberModel.c.status == MemberStatus.ACCEPTED.value)
                )
            )
            result = await conn.execute(
                select([exists(query)])
            )
            return await result.scalar()

    async def is_registered_for_team_as_trainer(
            self,
            user: UserEntity,
            team: TeamEntity,
            ) -> bool:
        async with self.engine.acquire() as conn:
            query = (
                TeamModel
                .select()
                .where(
                    (TeamModel.c.id == team.id)
                    & (TeamModel.c.trainer_id == user.id)
                )
            )
            result = await conn.execute(
                select([exists(query)])
            )
            return await result.scalar()
