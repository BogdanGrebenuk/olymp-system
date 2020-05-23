from db import (
    user_mapper
)
from db.entities import User, Team, Contest
from exceptions.role import PermissionException


async def get_team_resources(
        engine,
        user: User,
        contest: Contest,
        team: Team
        ):
    """Team resources - solutions of the team, invites to the team"""
    if user.is_organizer():
        if user.is_creator(contest):
            return
        else:  # organizer that didn't create this contest can't see its resources
            raise PermissionException(
                "you can't access resources of this contest",
                {'contest_id': contest.id}
            )

    is_registered = False
    if user.is_participant():
        is_registered = await user_mapper.is_registered_for_team_as_participant(
            engine, user, team
        )
    elif user.is_trainer():
        is_registered = await user_mapper.is_registered_for_team_as_trainer(
            engine, user, team
        )

    if not is_registered:
        raise PermissionException(
            'you are not allowed to access solutions of this team!',
            {'team_id': team.id}
        )
