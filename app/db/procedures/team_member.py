from functools import partial

from sqlalchemy.sql.expression import select

from db import team_mapper
from db.common import (
    create as _create,
    get as _get,
    update as _update,
    delete as _delete
)
from db.entities import (
    Contest as ContestEntity,
    Team as TeamEntity,
    TeamMember as TeamMemberEntity
)
from db.models import (
    Contest as ContestModel,
    TeamMember as TeamMemberModel,
    Team as TeamModel,
)


create = partial(_create, model=TeamMemberModel)


get = partial(_get, model=TeamMemberModel, entity=TeamMemberEntity)


update = partial(_update, model=TeamMemberModel, entity=TeamMemberEntity)


delete = partial(_delete, model=TeamMemberModel, entity=TeamMemberEntity)


async def get_team(engine, team_member: TeamMemberEntity) -> TeamEntity:
    team = await team_mapper.get(engine, team_member.team_id)
    return team


async def get_contest(engine, team_member: TeamMemberEntity) -> ContestEntity:
    team = await get_team(engine, team_member)
    contest = await team_mapper.get_contest(engine, team)
    return contest


async def _get_contest(engine, team_member: TeamMemberEntity) -> ContestEntity:
    """'get_contest' version with join"""
    async with engine.acquire() as conn:
        join = TeamModel.join(
            ContestModel,
            TeamModel.c.contest_id == ContestModel.c.id
        )
        result = await conn.execute(
            select([ContestModel])
            .select_from(join)
            .where(TeamModel.c.id == team_member.id)
        )
        contest = await result.fetchone()
        # TODO: if we change fk behaviour we must rewrite this section because of possible None
        return ContestEntity(**contest)
