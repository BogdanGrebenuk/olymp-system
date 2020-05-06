from functools import partial
from typing import Union

from db.common import create, get
from db.entities.role import Role as RoleEntity
from db.models import (
    Role as RoleModel
)


create_role = partial(create, model=RoleModel)


get_role = partial(get, model=RoleModel, entity=RoleEntity)


async def get_role_by_role(engine, role: str) -> Union[RoleEntity, None]:
    async with engine.acquire() as conn:
        result = await conn.execute(
            RoleModel.select().where(RoleModel.c.role == role)
        )
        entity = await result.fetchone()
        if entity is None:
            return None
        return RoleEntity(**entity)
