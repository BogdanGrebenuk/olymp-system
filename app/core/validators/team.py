from db.entities import Contest, Team
from exceptions.domain import DomainException
from exceptions.entity import EntityNotFound


async def create_team(contest: Contest):
    if contest.is_running():
        raise DomainException(
            "contest is already running!", {'contest_id': contest.id}
        )


async def get_team(contest: Contest, team: Team):
    if team.contest_id != contest.id:
        raise EntityNotFound(
            'there is no such team in specified contest!',
            {'team_id': team.id, 'contest_id': contest.id}
        )
