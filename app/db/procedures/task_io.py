from functools import partial

from db.common import create, get
from db.entities.task_io import TaskIO as TaskIOEntity
from db.models import TaskIO as TaskIOModel


create_task_io = partial(create, model=TaskIOModel)


get_task_io = partial(get, model=TaskIOModel, entity=TaskIOEntity)
