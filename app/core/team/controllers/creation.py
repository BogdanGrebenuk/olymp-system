from aiohttp import web

from app.commandbus import Bus

import app.core.validators as domain_validator
from app.core.team.commands import CreateTeam
from app.core.team.transformers import TeamTransformer
from app.db import TeamMapper
from app.utils.resolver import Resolver


async def create_team(
        request: web.Request,
        bus: Bus,
        contest_resolver: Resolver,
        team_mapper: TeamMapper,
        team_transformer: TeamTransformer
        ):

    body = request['body']
    contest = await contest_resolver.resolve(request)

    await domain_validator.create_team(contest)

    team = await bus.execute(
        CreateTeam(
            name=body['name'],
            contest_id=contest.id,
            trainer_id=request['user'].id
        )
    )

    await team_mapper.create(team)

    return web.json_response(await team_transformer.transform(team))
