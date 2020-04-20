from aiohttp import web

from commandbus.commands.contest import CreateContest
from validators.request import CreateContestBody
from utils.request import validate_body


@validate_body(schema=CreateContestBody)
async def create_contest(request):
    bus = request.app['bus']
    engine = request.app['db']
    body = request['body']

    name = body['name']
    contest = await bus.execute(CreateContest(name, engine))
    return web.json_response({'contest_id': contest.id})
