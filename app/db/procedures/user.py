from functools import partial
from typing import Union

from db.common import create, get
from db.entities.user import User as UserEntity
from db.models import (
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
