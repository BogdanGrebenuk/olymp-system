from core.validators.contest_resource import get_contest_resources
from core.validators.team_resource import get_team_resources
from db.entities import User, Contest, Team, Task, Solution
from exceptions.entity import EntityNotFound
from exceptions.role import PermissionException


async def create_solution(contest: Contest, task: Task):
    if not task.from_contest(contest):
        raise EntityNotFound(
            f'there is no specified task in this contest!',
            {'task_id': task.id, 'contest_id': contest.id}
        )
    if not contest.is_running():
        raise PermissionException(
            "contest isn't running, you create a solution!",
            {'contest_id': contest.id}
        )


async def get_solutions_for_contest(engine, user: User, contest: Contest):
    await get_contest_resources(engine, user, contest)


async def get_solutions_for_team(
        engine,
        user: User,
        contest: Contest,
        team: Team
        ):
    if not team.from_contest(contest):
        raise EntityNotFound(
            f'there is no such team in specified contest!',
            {'team_id': team.id, 'contest_id': contest.id}
        )
    await get_team_resources(engine, user, contest, team)


async def get_solution_code(
        engine,
        user: User,
        contest: Contest,
        team: Team,
        solution: Solution
        ):
    if not team.from_contest(contest):
        raise EntityNotFound(
            f'there is no such team in specified contest!',
            {'team_id': team.id, 'contest_id': contest.id}
        )
    if not solution.from_team(team):
        raise EntityNotFound(
            f'there is no such solution from specified team',
            {'solution_id': solution.id, 'team_id': team.id}
        )

    await get_team_resources(engine, user, contest, team)
