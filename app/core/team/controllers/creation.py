from aiohttp import web

from aiopg.sa import Engine

from app.commandbus import Bus

import app.core.validators as domain_validator
from app.core.team.commands import CreateTeam
from app.utils.resolver import Resolver


async def create_team(
        request: web.Request,
        bus: Bus,
        engine: Engine,
        contest_resolver: Resolver
        ):

    body = request['body']
    contest = await contest_resolver.resolve(request)

    await domain_validator.create_team(contest)

    team = await bus.execute(
        CreateTeam(
            name=body['name'],
            contest_id=contest.id,
            trainer_id=request['user'].id,
            engine=engine
        )
    )

    return web.json_response({'team_id': team.id}, status=201)
