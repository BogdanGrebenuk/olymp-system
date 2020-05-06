from functools import partial

from db.common import create, get
from db.entities.user import User as UserEntity
from db.models import (
    User as UserModel
)


create_user = partial(create, model=UserModel)


get_user = partial(get, model=UserModel, entity=UserEntity)
