from db.common import create, get
from db.entities.task_io import TaskIO as TaskIOEntity
from db.models import TaskIO as TaskIOModel


async def create_task_io(engine, task: TaskIOEntity):
    return await create(engine, task, TaskIOModel)


async def get_task_io(engine, id) -> TaskIOEntity:
    result = await get(engine, id, TaskIOModel)
    if result is None:
        return None
    return TaskIOEntity(**result)
