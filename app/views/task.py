from aiohttp import web

import app.core.validators as domain_validator
from app.commandbus.commands.task import CreateTask
from app.db import contest_mapper
from app.transformers import transform_task
from app.utils.injector import inject
from app.utils.injector.entity import Contest, Task


@inject(Contest)
async def create_task(request):
    bus = request.app['bus']
    engine = request.app['db']

    body = request['body']

    user = request['user']
    contest = request['contest']

    input_output = [tuple(i) for i in body['input_output']]

    await domain_validator.create_task(user, contest)

    task = await bus.execute(
        CreateTask(
            engine=engine,
            contest=contest,
            input_output=body["input_output"],
            name=body['name'],
            description=body['description'],
            max_cpu_time=body['max_cpu_time'],
            max_memory=body['max_memory']
        )
    )

    return web.json_response({'task_id': task.id})


@inject(Contest)
async def get_tasks(request):
    engine = request.app['db']

    contest = request['contest']
    user = request['user']

    await domain_validator.get_tasks(engine, user, contest)

    tasks = await contest_mapper.get_tasks(engine, contest)
    return web.json_response({
        'tasks': [transform_task(i) for i in tasks]
    })  # TODO: create middleware that will return web.json_response


@inject(Contest, Task)
async def get_task(request):
    engine = request.app['db']
    contest = request['contest']
    user = request['user']
    task = request['task']

    await domain_validator.get_task(engine, user, contest, task)

    return web.json_response({
        'task': transform_task(task)
    })
