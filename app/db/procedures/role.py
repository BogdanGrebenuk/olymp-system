from functools import partial

from db.common import create, get
from db.entities.role import Role as RoleEntity
from db.models import (
    Role as RoleModel
)


create_role = partial(create, model=RoleModel)


get_role = partial(get, model=RoleModel, entity=RoleEntity)
