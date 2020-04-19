from aiohttp import web

from commandbus.commands.task import CreateTask
from db.procedures.contest import get_contest
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
