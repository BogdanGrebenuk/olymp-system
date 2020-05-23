from db import user_mapper
from db.entities import Contest, User
from exceptions.role import PermissionException


async def get_contest_resources(engine, user: User, contest: Contest):
    """Contest resources - tasks, solutions"""

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
        is_registered = await user_mapper.is_registered_for_contest_as_participant(
            engine, user, contest
        )
    elif user.is_trainer():
        is_registered = await user_mapper.is_registered_for_contest_as_trainer(
            engine, user, contest
        )

    if not is_registered:
        raise PermissionException(
            "you are not registered for this contest!",
            {'contest_id': contest.id}
        )
    if not contest.is_running():
        raise PermissionException(
            "contest isn't running, you can't see resources!",
            {'contest_id': contest.id}
        )
