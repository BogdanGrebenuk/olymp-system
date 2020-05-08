from aiohttp import web

from commandbus.commands.contest import CreateContest
from db.procedures.contest import (
    get_contests as get_contests_procedure,
    get_contest as get_contest_procedure
)
from transformers import transform_contest
from validators.request import CreateContestBody
from utils.request import (validate_body, BodyType)


@validate_body(schema=CreateContestBody, body_type=BodyType.FORM_DATA)
async def create_contest(request):
    bus = request.app['bus']
    engine = request.app['db']
    body = request['body']

    name = body['name']
    description = body['description']
    max_participants = body['max_participants']
    image = body['image']
    start_date = body['start_date']
    end_date = body['end_date']

    contest = await bus.execute(CreateContest(name, description, max_participants, image, engine, start_date, end_date))
    return web.json_response({'contest_id': contest.id})  # TODO: hide bare web.json_response


async def get_contests(request):
    engine = request.app['db']
    contests = await get_contests_procedure(engine)
    return web.json_response({
        'contests': [transform_contest(i) for i in contests]
    })


async def get_contest(request):
    engine = request.app['db']
    contest_id = request.match_info.get('contest_id')
    contest = await get_contest_procedure(engine, contest_id)
    if contest is None:
        return web.json_response(
            {
                'error': f'there is no contest with id {contest_id}',
                'payload': {'contest_id': contest_id}
            },
            status=400
        )
    return web.json_response({
        'contest': transform_contest(contest)
    })
