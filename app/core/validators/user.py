from db import user_mapper
from db.entities import User, Contest, Team
from exceptions.domain import DomainException
from exceptions.entity import EntityNotFound
from exceptions.role import PermissionException


# actually this is not the domain..
async def create_user(engine, email):
    user = await user_mapper.get_user_by_email(engine, email)
    if user is not None:
        raise DomainException(
            'there is already a user with such email!',
            {'email': email}
        )


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
