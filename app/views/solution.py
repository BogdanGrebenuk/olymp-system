from aiohttp import web

from commandbus.commands.solution import (
    CreateSolution,
    VerifySolution
)
from db.procedures.contest import get_contest
from db.procedures.task import get_task
from db.procedures.solution import update_solution
from validators.request import VerifyTaskBody
from utils.request import validate_body


@validate_body(schema=VerifyTaskBody)
async def verify_task(request):
    bus = request.app['bus']
    engine = request.app['db']

    body = request['body']

    task_id = body['task_id']
    language = body['language']
    code = body['code']

    task = await get_task(engine, task_id)
    if task is None:
        return web.json_response(
            {
                'error': f'there is no task with id {task_id}',
                'payload': {'task_id': task_id}
            },
            status=400
        )

    contest = await get_contest(engine, task.contest_id)

    solution = await bus.execute(
        CreateSolution(engine, contest, task, language, code)
    )

    is_passed = await bus.execute(VerifySolution(engine, solution, task))
    solution.is_passed = is_passed

    await update_solution(engine, solution)

    return web.json_response({
        'is_passed': is_passed
    })
