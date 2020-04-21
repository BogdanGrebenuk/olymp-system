from aiohttp import web

from commandbus.commands.task import CreateTask
from db.procedures.contest import (
    get_contest,
    get_tasks as get_tasks_procedure
)
from db.procedures.task import (
    get_task as get_task_procedure
)
from transformers import transform_task
from utils.request import validate_body
from validators.request import CreateTaskBody


@validate_body(schema=CreateTaskBody)
async def create_task(request):
    bus = request.app['bus']
    engine = request.app['db']

    body = request['body']

    contest_id = body['contest_id']
    input_output = [tuple(i) for i in body['input_output']]
    description = body['description']
    max_cpu_time = body['max_cpu_time']
    max_memory = body['max_memory']

    contest = await get_contest(engine, contest_id)
    if contest is None:
        return web.json_response(
            {
                'error': f'there is no contest with id {contest_id}',
                'payload': {'contest_id': contest_id}
            },
            status=400
        )

    task = await bus.execute(
        CreateTask(
            engine,
            contest,
            input_output,
            description,
            max_cpu_time,
            max_memory
        )
    )

    return web.json_response({'task_id': task.id})


async def get_tasks(request):
    engine = request.app['db']

    contest_id = request.match_info.get('contest_id')

    contest = await get_contest(engine, contest_id)
    if contest is None:
        return web.json_response(
            {
                'error': f'there is no contest with id {contest_id}',
                'payload': {'contest_id': contest_id}
            },
            status=400
        )

    tasks = await get_tasks_procedure(engine, contest)
    return web.json_response({
        'tasks': [transform_task(i) for i in tasks]
    })


async def get_task(request):
    engine = request.app['db']

    contest_id = request.match_info.get('contest_id')
    # TODO: implement entity injector and get rid of all these "entity = ...; if entity is not None"
    contest = await get_contest(engine, contest_id)
    if contest is None:
        return web.json_response(
            {
                'error': f'there is no contest with id {contest_id}',
                'payload': {'contest_id': contest_id}
            },
            status=400
        )

    task_id = request.match_info.get('task_id')
    task = await get_task_procedure(engine, task_id)
    if task is None:
        return web.json_response(
            {
                'error': f'there is no task with id {task_id}'
            }
        )

    return web.json_response({
        'task': transform_task(task)
    })
