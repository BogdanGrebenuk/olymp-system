from asyncio import gather
from collections import defaultdict

from aiohttp import web

from commandbus.commands.contest import CreateContest
from core.score import get_total_score
from db import contest_mapper, solution_mapper
from transformers import (
    transform_contest,
    transform_team,
    transform_solution
)
from utils.injector import inject
from utils.injector.entity import Contest


async def create_contest(request):
    bus = request.app['bus']
    engine = request.app['db']
    thread_pool = request.app['thread_pool']
    body = request['body']

    creator_id = request['user'].id

    contest = await bus.execute(
        CreateContest(
            name=body['name'],
            description=body['description'],
            max_teams=body['max_teams'],
            max_participants_in_team=body['max_participants_in_team'],
            image=body['image'],
            start_date=body['start_date'],
            end_date=body['end_date'],
            creator_id=creator_id,
            engine=engine,
            pool=thread_pool
        )
    )
    return web.json_response({'contest_id': contest.id})


async def get_contests(request):
    engine = request.app['db']
    contests = await contest_mapper.get_contests(engine)
    return web.json_response({
        'contests': [transform_contest(i) for i in contests]
    })


@inject(Contest)
async def get_contest(request):
    contest = request['contest']
    return web.json_response({
        'contest': transform_contest(contest)
    })


# todo: rewrite all this stuff
@inject(Contest)
async def get_leader_board(request):
    engine = request.app['db']
    contest = request['contest']
    # todo: check if user has permission
    teams = await contest_mapper.get_teams(engine, contest)
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
