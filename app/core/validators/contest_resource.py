from app.core.user.domain.entity import User
from app.db import mappers_container
from app.db.entities import Contest
from app.exceptions.role import PermissionException


async def get_contest_resources(engine, user: User, contest: Contest):
    """Contest resources - tasks, solutions"""

    # TODO: temporary solution, inject user_mapper after refactoring domain-related code
    user_mapper = mappers_container.user_mapper()
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
