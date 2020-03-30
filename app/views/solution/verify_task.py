from aiohttp import web
from marshmallow import ValidationError

from commandbus.commands.solution import (
    CreateSolution,
    VerifySolution
)
from validators.request import VerifyTaskBody


async def verify_task(request):
    bus = request.app['bus']

    raw_body = await request.json()
    try:
        body = VerifyTaskBody().load(raw_body)
    except ValidationError as err:
        return web.json_response(err.messages, status=400)

    user_id = body['user_id']
    contest_id = body['contest_id']
    task_id = body['task_id']
    language = body['language']
    code = body['code']

    solution = await bus.execute(
        CreateSolution(user_id, contest_id, task_id, language, code)
    )

    is_passed = await bus.execute(VerifySolution(solution))
    solution['is_passed'] = is_passed  # TODO: entity!

    return web.json_response({
        'is_passed': is_passed
    })
