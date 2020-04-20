from db.common import create, get, update
from db.entities.solution import Solution as SolutionEntity
from db.models import Solution as SolutionModel


async def create_solution(engine, solution: SolutionEntity):
    return await create(engine, solution, SolutionModel)


async def get_solution(engine, id) -> SolutionEntity:
    result = await get(engine, id, SolutionModel)
    if result is None:
        return None
    return SolutionEntity(**result)


async def update_solution(engine, solution: SolutionEntity):
    return await update(engine, solution, SolutionModel)
