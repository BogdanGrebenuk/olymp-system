from aiohttp import web

from commandbus.commands.solution import (
    CreateSolution,
    VerifySolution
)
from db import (
    contest_mapper,
    task_mapper,
    solution_mapper
)


async def verify_task(request):
    bus = request.app['bus']
    engine = request.app['db']
    pool = request.app['process_pool']

    body = request['body']

    task_id = body['task_id']
    language = body['language']
    code = body['code']

    task = await task_mapper.get(engine, task_id)
    if task is None:
        return web.json_response(
            {
                'error': f'there is no task with id {task_id}',
                'payload': {'task_id': task_id}
            },
            status=400
        )

    contest = await contest_mapper.get(engine, task.contest_id)

    solution = await bus.execute(
        CreateSolution(engine, contest, task, language, code, pool)
    )

    is_passed = await bus.execute(
        VerifySolution(
            engine, solution, task, pool, request.app['config']['docker_meta']
        )
    )
    solution.is_passed = is_passed

    await solution_mapper.update_solution(engine, solution)

    return web.json_response({
        'is_passed': is_passed
    })
