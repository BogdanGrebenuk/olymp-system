from functools import partial

from db.common import create as _create, get as _get
from db.entities.task_io import TaskIO as TaskIOEntity
from db.models import TaskIO as TaskIOModel


create = partial(_create, model=TaskIOModel)


get = partial(_get, model=TaskIOModel, entity=TaskIOEntity)
