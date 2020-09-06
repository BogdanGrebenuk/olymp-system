from app.core.contest.domain.entity import Contest
from app.db.entities import Team
from app.exceptions.domain import DomainException
from app.exceptions.entity import EntityNotFound


async def create_team(contest: Contest):
    if contest.is_running():  # TODO: trainer can create team when contest is finished
        raise DomainException(
            "contest is already running!", {'contest_id': contest.id}
        )


async def get_team(contest: Contest, team: Team):
    if team.contest_id != contest.id:
        raise EntityNotFound(
            'there is no such team in specified contest!',
            {'team_id': team.id, 'contest_id': contest.id}
        )
