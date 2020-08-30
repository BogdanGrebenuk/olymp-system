from functools import partial

from app.db.common import create as _create, get as _get
from app.db.entities.task_io import TaskIO as TaskIOEntity
from app.db.models import TaskIO as TaskIOModel


create = partial(_create, model=TaskIOModel)


get = partial(_get, model=TaskIOModel, entity=TaskIOEntity)
