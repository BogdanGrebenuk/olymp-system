from functools import partial
from typing import List, Union

from core.team_member import MemberStatus
from db import contest_mapper
from db.common import create as _create, get as _get
from db.entities import (
    Team as TeamEntity,
    TeamMember as TeamMemberEntity,
    Contest as ContestEntity
)
from db.models import (
    Team as TeamModel,
    TeamMember as TeamMemberModel,
)


create = partial(_create, model=TeamModel)


get = partial(_get, model=TeamModel, entity=TeamEntity)


async def get_members(
        engine,
        team: TeamEntity,
        status: Union[MemberStatus, None] = None
        ) -> List[TeamMemberEntity]:
    """Get all members of team

    If status isn't specified, return members with any status
    """
    async with engine.acquire() as conn:
        select_query = TeamMemberModel.select()
        where = TeamMemberModel.c.team_id == team.id
        if status is not None:
            where = where & (TeamMemberModel.c.status == status.value)

        result = await conn.execute(select_query.where(where))
        return [TeamMemberEntity(**i) for i in await result.fetchall()]


async def get_contest(engine, team: TeamEntity) -> ContestEntity:
    contest = await contest_mapper.get(engine, team.contest_id)
    return contest
