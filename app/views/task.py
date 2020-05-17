from aiohttp import web

from commandbus.commands.task import CreateTask
from db import (
    contest_mapper
)
from exceptions.entity import EntityNotFound
from transformers import transform_task, transform_datetime
from utils.injector import inject
from utils.injector.entity import Contest, Task


async def create_task(request):
    bus = request.app['bus']
    engine = request.app['db']

    body = request['body']

    contest_id = body['contest_id']
    input_output = [tuple(i) for i in body['input_output']]
    name = body['name']
    description = body['description']
    max_cpu_time = body['max_cpu_time']
    max_memory = body['max_memory']

    contest = await contest_mapper.get(engine, contest_id)
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
            name,
            description,
            max_cpu_time,
            max_memory
        )
    )

    return web.json_response({'task_id': task.id})


@inject(Contest)
async def get_tasks(request):
    engine = request.app['db']

    contest = request['contest']
    user = request['user']

    if not contest.can_view_tasks(user):
        return web.json_response({
            'error': "you can't see tasks of this contest",
            'payload': {
                'contest_id': contest.id,
                'start_date': transform_datetime(contest.start_date)
            }
        }, status=400)

    tasks = await contest_mapper.get_tasks(engine, contest)
    return web.json_response({
        'tasks': [transform_task(i) for i in tasks]
    })


@inject(Contest, Task)
async def get_task(request):
    contest = request['contest']
    user = request['user']
    task = request['task']

    if task.contest_id != contest.id:
        raise EntityNotFound(
            f'there is no such task in contest {contest.id}!',
            {'task_id': task.id, 'contest_id': contest.id}
        )

    if not contest.can_view_tasks(user):
        return web.json_response({
            'error': "the contest is't start yet!",
            'payload': {
                'contest_id': contest.id,
                'start_date': contest.start_date
            }
        })

    return web.json_response({
        'task': transform_task(task)
    })
