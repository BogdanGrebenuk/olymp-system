from functools import partial
from typing import List

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


async def get_members(engine, team: TeamEntity) -> List[TeamMemberEntity]:
    async with engine.acquire() as conn:
        result = await conn.execute(
            TeamMemberModel
            .select()
            .where(TeamMemberModel.c.team_id == team.id)
        )
        return [TeamMemberEntity(**i) for i in await result.fetchall()]


async def get_contest(engine, team: TeamEntity) -> ContestEntity:
    contest = await contest_mapper.get(engine, team.contest_id)
    return contest
