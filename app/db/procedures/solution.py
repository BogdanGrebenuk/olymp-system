from functools import partial

from db.common import create, get, update
from db.entities.solution import Solution as SolutionEntity
from db.models import Solution as SolutionModel


create_solution = partial(create, model=SolutionModel)


get_solution = partial(get, model=SolutionModel, entity=SolutionEntity)


async def update_solution(engine, solution: SolutionEntity):
    return await update(engine, solution, SolutionModel)
