from db.common import create, get
from db.entities.contest import Contest as ContestEntity
from db.models import Contest as ContestModel


async def create_contest(engine, contest: ContestEntity):
    return await create(engine, contest, ContestModel)


async def get_contest(engine, id) -> ContestEntity:
    result = await get(engine, id, ContestModel)
    if result is None:
        return None
    return ContestEntity(**result)
