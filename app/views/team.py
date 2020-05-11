from aiohttp import web

from commandbus.commands.team import CreateTeam
from db import contest_mapper


async def create_team(request):
    bus = request.app['bus']
    engine = request.app['db']
    body = request['body']

    contest_id = body['contest_id']

    contest = await contest_mapper.get(engine, contest_id)
    if contest is None:
        return web.json_response(
            {
                'error': f'there is no contest with id {contest_id}',
                'payload': {'contest_id': contest_id}
            },
            status=400
        )

    if contest.is_started():
        return web.json_response(
            {
                'error': f"you can't register new command for already running contest",
                'payload': {'contest_id': contest_id}
            },
            status=400
        )

    team = await bus.execute(
        CreateTeam(
            name=body['name'],
            contest_id=contest_id,
            trainer_id=request['user'].id,
            engine=engine
        )
    )

    return web.json_response({'team_id': team.id}, status=201)
