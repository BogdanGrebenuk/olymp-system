from aiohttp import web

from aiopg.sa import Engine

import app.core.validators as domain_validator

from app.core.team.transformers import TeamTransformer
from app.db import mappers_container, UserMapper
from app.utils.resolver import Resolver


async def get_teams_for_contest(
        request: web.Request,
        contest_resolver: Resolver,
        user_mapper: UserMapper,
        team_transformer: TeamTransformer
        ):
    contest = await contest_resolver.resolve(request)

    teams = await user_mapper.get_created_teams_by_contest(
        contest
    )

    return web.json_response({
        'teams': await team_transformer.transform_many(teams)
    })


async def get_teams_for_contest_and_creator(
        request: web.Request,
        contest_resolver: Resolver,
        user_mapper: UserMapper,
        team_transformer: TeamTransformer
        ):
    contest = await contest_resolver.resolve(request)

    creator_id = request['params']['creator_id']
    creator = await user_mapper.find(creator_id)

    teams = await user_mapper.get_created_teams_by_contest(
       contest, creator
    )

    return web.json_response({
        'teams': await team_transformer.transform_many(teams)
    })


async def get_team(
        request: web.Request,
        team_resolver: Resolver,
        contest_resolver: Resolver,
        team_transformer: TeamTransformer
        ):
    team = await team_resolver.resolve(request)

    contest = await contest_resolver.resolve(request)

    await domain_validator.get_team(contest, team)

    return web.json_response({
        'team': await team_transformer.transform(team)
    })
