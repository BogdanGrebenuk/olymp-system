from functools import partial
from typing import List

from db.common import create as _create, get as _get
from db.entities.task import Task as TaskEntity
from db.entities.task_io import TaskIO as TaskIOEntity
from db.models import (
    Task as TaskModel,
    TaskIO as TaskIOModel
)


create = partial(_create, model=TaskModel)


get = partial(_get, model=TaskModel, entity=TaskEntity)


async def get_task_ios(engine, task: TaskEntity) -> List[TaskIOEntity]:
    async with engine.acquire() as conn:
        result = await conn.execute(
            TaskIOModel
            .select()
            .where(TaskIOModel.c.task_id == task.id)
        )
        return [TaskIOEntity(**i) for i in await result.fetchall()]
