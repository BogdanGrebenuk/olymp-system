from functools import partial

from db.common import (
    create as _create,
    get as _get,
    update
)
from db.entities.solution import Solution as SolutionEntity
from db.models import Solution as SolutionModel


create = partial(_create, model=SolutionModel)


get = partial(_get, model=SolutionModel, entity=SolutionEntity)


# TODO: create it via partial
async def update_solution(engine, solution: SolutionEntity):
    return await update(engine, solution, SolutionModel)
