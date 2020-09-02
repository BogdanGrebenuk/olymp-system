from aiohttp import web

import app.core.validators as domain_validator
from app.commandbus.commands.team import CreateTeam
from app.db import mappers_container
from app.exceptions.entity import EntityNotFound
from app.transformers import transform_team
from app.utils.injector import inject
from app.utils.injector.entity import (
    Contest,
    Team,
    # Creator
)


@inject(Contest)
async def create_team(request):
    bus = request.app['bus']
    engine = request.app['db']
    body = request['body']

    contest = request['contest']

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


@inject(Contest)
async def get_teams_for_contest(request):
    # TODO: temporary solution, inject user_mapper after refactoring domain-related code
    user_mapper = mappers_container.user_mapper()

    engine = request.app['db']

    contest = request['contest']

    teams = await user_mapper.get_created_teams_by_contest(
        engine, contest
    )

    return web.json_response({
        'teams': [transform_team(team) for team in teams]
    })


@inject(Contest)
async def get_teams_for_contest_and_creator(request):
    engine = request.app['db']

    # TODO: temporary solution, inject user_mapper after refactoring domain-related code
    user_mapper = mappers_container.user_mapper()

    contest = request['contest']
    creator_id = request['params']['creator_id']
    creator = await user_mapper.get(
        engine, creator_id
    )

    teams = await user_mapper.get_created_teams_by_contest(
        engine, contest, creator
    )

    return web.json_response({
        'teams': [transform_team(team) for team in teams]
    })


@inject(Team, Contest)
async def get_team(request):
    team = request['team']
    contest = request['contest']

    await domain_validator.get_team(contest, team)

    return web.json_response({
        'team': transform_team(team)
    })
