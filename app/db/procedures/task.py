from db.common import create, get
from db.entities.task import Task as TaskEntity
from db.models import Task as TaskModel


async def create_task(engine, task: TaskEntity):
    return await create(engine, task, TaskModel)


async def get_task(engine, id) -> TaskEntity:
    result = await get(engine, id, TaskModel)
    if result is None:
        return None
    return TaskEntity(**result)
