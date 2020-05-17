from functools import partial
from typing import Union, List

from sqlalchemy.sql import select

from core.team_member import MemberStatus
from db.common import create as _create, get as _get
from db.entities import (
    User as UserEntity,
    Contest as ContestEntity,
    Team as TeamEntity,
    TeamMember as TeamMemberEntity
)
from db.models import (
    User as UserModel,
    Contest as ContestModel,
    Team as TeamModel,
    TeamMember as TeamMemberModel
)


create = partial(_create, model=UserModel)


get = partial(_get, model=UserModel, entity=UserEntity)


async def get_all(engine) -> List[UserEntity]:
    async with engine.acquire() as conn:
        result = await conn.execute(
            UserModel.select()
        )
        return [UserEntity(**i) for i in await result.fetchall()]


async def get_user_by_email(engine, email: str) -> Union[UserEntity, None]:
    async with engine.acquire() as conn:
        result = await conn.execute(
            UserModel.select().where(UserModel.c.email == email)
        )
        entity = await result.fetchone()
        if entity is None:
            return None
        return UserEntity(**entity)


async def get_accepted_team_for_contest(
        engine,
        user: UserEntity,
        contest: ContestEntity
        ) -> Union[TeamEntity, None]:
    async with engine.acquire() as conn:
        join = (
            ContestModel
            .join(
                TeamModel,
                ContestModel.c.id == TeamModel.c.contest_id
            )
            .join(
                TeamMemberModel,
                TeamModel.c.id == TeamMemberModel.c.team_id
            )
        )
        result = await conn.execute(
            select([TeamModel])
            .select_from(join)
            .where(
                (ContestModel.c.id == contest.id)
                & (TeamMemberModel.c.user_id == user.id)
                & (TeamMemberModel.c.status == MemberStatus.ACCEPTED.value)
            )
        )
        team = await result.fetchone()
        if team is None:
            return None
        return TeamEntity(**team)


async def get_received_invites_for_contest(
        engine,
        user: UserEntity,
        contest: ContestEntity
        ) -> List[TeamMemberEntity]:
    async with engine.acquire() as conn:
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


async def get_sent_invites_for_contest(
        engine,
        user: UserEntity,
        contest: ContestEntity
        ) -> List[TeamMemberEntity]:
    async with engine.acquire() as conn:
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


async def get_created_teams_by_contest(
        engine,
        contest: ContestEntity,
        creator: Union[UserEntity, None]
        ) -> List[TeamEntity]:
    async with engine.acquire() as conn:
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
