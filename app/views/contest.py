from aiohttp import web

from commandbus.commands.contest import CreateContest
from db import contest_mapper
from transformers import transform_contest
from utils.injector import inject, Contest


async def create_contest(request):
    bus = request.app['bus']
    engine = request.app['db']
    thread_pool = request.app['thread_pool']
    body = request['body']

    creator_id = request['user'].id

    contest = await bus.execute(
        CreateContest(
            name=body['name'],
            description=body['description'],
            max_teams=body['max_teams'],
            max_participants_in_team=body['max_participants_in_team'],
            image=body['image'],
            start_date=body['start_date'],
            end_date=body['end_date'],
            creator_id=creator_id,
            engine=engine,
            pool=thread_pool
        )
    )
    return web.json_response({'contest_id': contest.id})  # TODO: hide bare web.json_response


async def get_contests(request):
    engine = request.app['db']
    contests = await contest_mapper.get_contests(engine)
    return web.json_response({
        'contests': [transform_contest(i) for i in contests]
    })


@inject(Contest)
async def get_contest(request):
    contest = request['contest']
    return web.json_response({
        'contest': transform_contest(contest)
    })
