from asyncio import gather

from aiohttp import web
from aiopg.sa import Engine

import app.core.validators as domain_validator
from app.core.solution.services.code import CodeLoader
from app.core.solution.transformers import SolutionTransformer
from app.db import SolutionMapper
from app.utils.resolver import Resolver


async def get_solutions_for_contest(
        request,
        engine: Engine,  # TODO: remove engine in future (domain_validator)
        contest_resolver: Resolver,
        solution_mapper: SolutionMapper,
        solution_transformer: SolutionTransformer
        ):
    user = request['user']
    contest = await contest_resolver.resolve(request)

    # TODO: refactor domain_validator, use DI
    await domain_validator.get_solutions_for_contest(engine, user, contest)
    solutions = await solution_mapper.get_all_from_contest(contest)

    return web.json_response({
        'solutions': await solution_transformer.transform_many(solutions)
    })


async def get_solutions_for_team(
        request,
        engine: Engine,
        contest_resolver: Resolver,
        team_resolver: Resolver,
        solution_mapper: SolutionMapper,
        solution_transformer: SolutionTransformer
        ):
    user = request['user']

    contest, team = await gather(
        contest_resolver.resolve(request),
        team_resolver.resolve(request)
    )

    # TODO: refactor domain_validator, use DI
    await domain_validator.get_solutions_for_team(
        engine, user, contest, team
    )
    solutions = await solution_mapper.get_all_from_team(team)

    return web.json_response({
        'solutions': await solution_transformer.transform_many(solutions)
    })


# TODO: move code to solution transformer?
async def get_solution_code(
        request,
        engine: Engine,
        contest_resolver: Resolver,
        solution_resolver: Resolver,
        team_mapper,
        code_loader: CodeLoader
        ):
    user = request['user']
    contest, solution = await gather(
        contest_resolver.resolve(request),
        solution_resolver.resolve(request)
    )

    team = await team_mapper.get(solution.team_id)

    # TODO: refactor domain_validator, use DI
    await domain_validator.get_solution_code(
        engine, user, contest, team, solution
    )

    code = await code_loader.load_code(solution)
    return web.json_response({
        'code': code
    })
