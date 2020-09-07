from asyncio import gather
from collections import defaultdict

from aiohttp import web

from app.core.score import get_total_score
from app.db import ContestMapper, solution_mapper
from app.transformers import (

    transform_team,
)

from app.core.contest.transformers import ContestTransformer

from app.utils.resolver import Resolver

from aiopg.sa import Engine


async def get_contests(
        contest_mapper: ContestMapper,
        contest_transformer: ContestTransformer
):
    contests = await contest_mapper.find_all()
    return web.json_response({
        'contests': [contest_transformer.transform(i) for i in contests]
    })


async def get_contest(
        request,
        contest_resolver: Resolver,
        contest_transformer: ContestTransformer
):
    contest = await contest_resolver.resolve(request)
    return web.json_response({
        'contest': contest_transformer.transform(contest)
    })


# todo: rewrite all this stuff

async def get_leader_board(
        request,
        contest_resolver: Resolver,
        contest_mapper: ContestMapper,
        engine: Engine
):

    contest = await contest_resolver.resolve(request)
    # todo: check if user has permission

    teams = await contest_mapper.get_teams(contest)
    solutions_info = await gather(*[
        solution_mapper.get_all_from_team(engine, team)
        for team in teams
    ])
    transformed_teams = []
    for team, solutions in zip(teams, solutions_info):
        transformed_teams.append(transform_team(team))
        transformed_teams[-1]['score'] = get_total_score(contest, solutions)

        solutions_by_tasks = defaultdict(list)
        for solution in solutions:
            solutions_by_tasks[solution.task_id].append(solution)

        transformed_teams[-1]['solvedTasksAmount'] = sum(
            any(s.is_passed for s in solutions_by_tasks[task_id])
            for task_id in solutions_by_tasks
        )

    transformed_teams.sort(
        key=lambda team: (
            team['solvedTasksAmount'], team['score']
        ),
        reverse=True
    )

    return web.json_response({
        'teamsInfo': transformed_teams
    })
