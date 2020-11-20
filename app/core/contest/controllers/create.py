from app.core.contest.commands.create_contest import CreateContest
from app.db.mappers.contest import ContestMapper
from app.commandbus import Bus

from aiohttp import web


async def create_contest(
        request,
        bus: Bus,
        contest_mapper: ContestMapper
        ):

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
        )
    )
    await contest_mapper.create(contest)
    return web.json_response({'contest_id': contest.id})
