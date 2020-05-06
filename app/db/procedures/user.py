from functools import partial
from typing import Union

from sqlalchemy.sql.expression import select

from db.common import create, get
from db.entities.role import Role as RoleEntity
from db.entities.user import User as UserEntity
from db.models import (
    Role as RoleModel,
    User as UserModel
)


create_user = partial(create, model=UserModel)


get_user = partial(get, model=UserModel, entity=UserEntity)


async def get_user_by_email(engine, email: str) -> Union[UserEntity, None]:
    async with engine.acquire() as conn:
        result = await conn.execute(
            UserModel.select().where(UserModel.c.email == email)
        )
        entity = await result.fetchone()
        if entity is None:
            return None
        return UserEntity(**entity)


async def get_role(engine, user: UserEntity) -> RoleEntity:
    async with engine.acquire() as conn:
        join = UserModel.join(RoleModel)
        result = await conn.execute(
            select([RoleModel]).select_from(join).where(UserModel.c.id == user.id)
        )
        entity = await result.fetchone()
        return RoleEntity(**entity)
