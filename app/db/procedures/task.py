from typing import List

from db.common import create, get
from db.entities.task import Task as TaskEntity
from db.entities.task_io import TaskIO as TaskIOEntity
from db.models import (
    Task as TaskModel,
    TaskIO as TaskIOModel
)


async def create_task(engine, task: TaskEntity):
    return await create(engine, task, TaskModel)


async def get_task(engine, id) -> TaskEntity:
    result = await get(engine, id, TaskModel)
    if result is None:
        return None
    return TaskEntity(**result)


async def get_task_ios(engine, task: TaskEntity) -> List[TaskIOEntity]:
    async with engine.acquire() as conn:
        result = await conn.execute(
            TaskIOModel
            .select()
            .where(TaskIOModel.c.task_id == task.id)
        )
        return [TaskIOEntity(**i) for i in await result.fetchall()]
