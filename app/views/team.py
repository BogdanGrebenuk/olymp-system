from aiohttp import web

from commandbus.commands.team import CreateTeam
from db import user_mapper
from exceptions.entity import EntityNotFound
from transformers import transform_team
from utils.injector import inject
from utils.injector.entity import (
    Contest,
    Team
)


@inject(Contest)
async def create_team(request):
    bus = request.app['bus']
    engine = request.app['db']
    body = request['body']

    contest = request['contest']

    if contest.is_started():
        return web.json_response(
            {
                'error': f"you can't register new command for already running contest",
                'payload': {'contest_id': contest.id}
            },
            status=400
        )

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
async def get_teams(request):
    engine = request.app['db']

    contest = request['contest']

    # if creator_id is None, return all teams of contest
    creator = None
    creator_id = request['params'].get('creator_id')
    if creator_id is not None:
        creator = await user_mapper.get(engine, creator_id)

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

    if team.contest_id != contest.id:
        raise EntityNotFound(
            'there is no such team in requested contest',
            {'team_id': team.id, 'contest_id': contest.id}
        )

    return web.json_response({
        'team': transform_team(team)
    })
