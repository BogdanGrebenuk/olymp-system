from asyncio import gather

from db import user_mapper
from db.entities import User, Contest, Task
from exceptions.domain import DomainException
from exceptions.entity import EntityNotFound
from exceptions.role import PermissionException


async def get_tasks(engine, user: User, contest: Contest):
    if contest.is_creator(user):
        return
    is_registered = await gather(
        user_mapper.is_registered_for_contest_as_participant(
            engine, user, contest
            ),
        user_mapper.is_registered_for_contest_as_trainer(
            engine, user, contest
        )
    )
    if not any(is_registered):
        raise PermissionException(
            "you are not registered in this contest!",
            {'contest_id': contest.id}
        )
    elif not contest.is_running():
        raise PermissionException(
            "contest isn't started yet, you can't see the tasks!",
            {'contest_id': contest.id}
        )


async def get_task(engine, user: User, contest: Contest, task: Task):
    if task.contest_id != contest.id:
        raise EntityNotFound(
            f'there is no such task in contest {contest.id}!',
            {'task_id': task.id, 'contest_id': contest.id}
        )
    await get_tasks(engine, user, contest)


async def create_task(contest: Contest):
    if contest.is_running():
        raise DomainException(
            "contest is already running!", {'contest_id': contest.id}
        )
