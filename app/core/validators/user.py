from app.core.user.domain.entity import User
from app.db.entities import Contest, Team
from app.exceptions.entity import EntityNotFound
from app.exceptions.role import PermissionException


async def get_sent_invites_for_team(user: User, contest: Contest, team: Team):
    if not team.from_contest(contest):
        raise EntityNotFound(
            'there is no this team in specified contest!',
            {'contest_id': contest.id, 'team_id': team.id}
        )
    if not team.is_trainer(user):
        raise PermissionException(
            'you are not allowed to view invites for this team!',
            {'team_id': team.id}
        )
