from app.core.user.domain.entity import User
from app.core.contest.domain.entity import Contest
from app.core.validators.contest_resource import get_contest_resources
from app.db.entities import Task
from app.exceptions.domain import DomainException
from app.exceptions.entity import EntityNotFound
from app.exceptions.role import PermissionException


async def get_tasks(engine, user: User, contest: Contest):
    await get_contest_resources(engine, user, contest)


async def get_task(engine, user: User, contest: Contest, task: Task):
    if not task.from_contest(contest):
        raise EntityNotFound(
            f'there is no such task in contest {contest.id}!',
            {'task_id': task.id, 'contest_id': contest.id}
        )
    await get_tasks(engine, user, contest)


async def create_task(user: User, contest: Contest):
    if not user.is_creator(contest):
        raise PermissionException(
            "you are not organizer of this contest!",
            {'contest': contest.id}
        )
    if contest.is_running():  # TODO: user can create task if contest is finished
        raise DomainException(
            "contest is already running!",
            {'contest_id': contest.id}
        )
