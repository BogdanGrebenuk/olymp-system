from functools import partial
from pathlib import Path

from aiohttp import web

import core.validators as domain_validator
import utils.executor as executor
from commandbus.commands.solution import (
    CreateSolution,
    VerifySolution
)
from db import (
    solution_mapper,
    user_mapper
)
from exceptions.role import PermissionException
from services.codesaver import DefaultCodeManager
from transformers import transform_solution
from utils.injector import inject
from utils.injector.entity import Task, Contest, Team, Solution


@inject(Contest, Task)
async def create_solution(request):
    bus = request.app['bus']
    engine = request.app['db']
    pool = request.app['process_pool']

    body = request['body']

    language = body['language']
    code = body['code']

    user = request['user']
    task = request['task']
    contest = request['contest']

    team = await user_mapper.get_accepted_team_for_contest(
        engine, user, contest
    )
    if team is None:
        raise PermissionException(
            f"you are not registered for this contest!",
            {'contest_id': contest.id}
        )

    await domain_validator.create_solution(contest, task)

    solution = await bus.execute(
        CreateSolution(
            engine=engine,
            contest=contest,
            user=user,
            task=task,
            team=team,
            language=language,
            code=code,
            pool=pool,
        )
    )

    is_passed = await bus.execute(
        VerifySolution(
            engine, solution, task, pool, request.app['config']['docker_meta']
        )
    )
    solution.is_passed = is_passed

    await solution_mapper.update(engine, solution)

    return web.json_response({
        'is_passed': is_passed
    })


@inject(Contest)
async def get_solutions_for_contest(request):
    engine = request.app['db']

    user = request['user']
    contest = request['contest']

    await domain_validator.get_solutions_for_contest(engine, user, contest)
    solutions = await solution_mapper.get_all_from_contest(engine, contest)

    return web.json_response({
        'solutions': [transform_solution(s) for s in solutions]
    })


@inject(Contest, Team)
async def get_solutions_for_team(request):
    engine = request.app['db']

    user = request['user']
    contest = request['contest']
    team = request['team']

    await domain_validator.get_solutions_for_team(
        engine, user, contest, team
    )
    solutions = await solution_mapper.get_all_from_team(engine, team)

    return web.json_response({
        'solutions': [transform_solution(s) for s in solutions]
    })


@inject(Contest, Solution)
async def get_solution_code(request):
    engine = request.app['db']
    process_pool = request.app['db']

    user = request['user']
    contest = request['contest']
    solution = request['solution']
    team = await solution_mapper.get_team(engine, solution)

    await domain_validator.get_solution_code(
        engine, user, contest, team, solution
    )

    code_manager = DefaultCodeManager.from_language(solution.language)
    task = partial(
        code_manager.load,

        Path(solution.get_full_path())
    )

    code = await executor.run(task, process_pool)
    return web.json_response({
        'code': code
    })
