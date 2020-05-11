from functools import partial
from typing import Union

from sqlalchemy.sql import select

from core.team_member import MemberStatus
from db.common import create as _create, get as _get
from db.entities import (
    User as UserEntity,
    Contest as ContestEntity,
    Team as TeamEntity
)
from db.models import (
    User as UserModel,
    Contest as ContestModel,
    Team as TeamModel,
    TeamMember as TeamMemberModel
)


create = partial(_create, model=UserModel)


get = partial(_get, model=UserModel, entity=UserEntity)


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
