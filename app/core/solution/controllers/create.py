from asyncio import gather

from aiohttp import web

import app.core.validators as domain_validator
from app.core.solution.services.creator import SolutionCreator
from app.core.solution.services.runner import SolutionRunner, SolutionRunnerResult
from app.core.solution.transformers import SolutionTransformer
from app.db import UserMapper, SolutionMapper
from app.exceptions.role import PermissionException
from app.utils.resolver import Resolver


async def create_solution(
        request,
        contest_resolver: Resolver,
        task_resolver: Resolver,
        user_mapper: UserMapper,
        solution_mapper: SolutionMapper,
        solution_transformer: SolutionTransformer,
        solution_creator: SolutionCreator,
        solution_runner: SolutionRunner
        ):
    user = request['user']
    task, contest = await gather(
        task_resolver.resolve(request),
        contest_resolver.resolve(request)
    )

    team = await user_mapper.find_accepted_team_for_contest(user, contest)
    if team is None:
        raise PermissionException(
            "You are not registered for this contest!",
            {"contest_id": contest.id}
        )

    # TODO: refactor domain_validator, use DI
    await domain_validator.create_solution(contest, task)

    solution = await solution_creator.create(
        contest=contest,
        task=task,
        user=user,
        team=team,
        language=request['body']['language'],
        code=request['body']['code']
    )

    result = await solution_runner.run(solution)
    solution.is_passed = result.is_passed

    await solution_mapper.create(solution)

    # TODO: change handler on FE
    return web.json_response({
        'solution': await solution_transformer.transform(solution)
    })
