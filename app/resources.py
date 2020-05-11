from dataclasses import dataclass
from typing import Callable, List, Union, Awaitable

from aiohttp.web import BaseRequest

import validators.schemas as schemas
from core.user_role import UserRole
from validators import Validator
from validators.body import BodyValidator, form_data_loader
from views.contest import (
    create_contest,
    get_contests,
    get_contest
)
from views.solution import verify_task
from views.task import (
    create_task,
    get_tasks,
    get_task
)
from views.user import (
    authenticate_user,
    register_user
)
from views.team import (
    create_team
)
from views.team_member import (
    create_member,
    accept_invite,
    decline_accept,
    delete_member
)


@dataclass
class Resource:
    method: str
    url: str
    allowed_roles: Union[List[UserRole], None]  # if None, there is no restrictions
    validator: Union[Validator, None]
    handler: Callable[[BaseRequest], Awaitable]


resources = [
    Resource(
        method='POST',
        url='/users',
        allowed_roles=None,
        validator=BodyValidator(schemas.RegisterUserBody),
        handler=register_user
    ),
    Resource(
        method='POST',
        url='/login',
        allowed_roles=None,
        validator=BodyValidator(schemas.AuthenticateUserBody),
        handler=authenticate_user
    ),
    Resource(
        method='GET',
        url='/api/contests',
        allowed_roles=None,
        validator=None,
        handler=get_contests
    ),
    Resource(
        method='GET',
        url='/api/contests/{contest_id}',
        allowed_roles=None,
        validator=None,
        handler=get_contest
    ),
    Resource(
        method='POST',
        url='/api/contests',
        allowed_roles=[UserRole.ORGANIZER],
        validator=BodyValidator(
            schemas.CreateContestBody,
            data_loader=form_data_loader
        ),
        handler=create_contest
    ),
    Resource(
        method='GET',
        url='/api/contests/{contest_id}/tasks',
        allowed_roles=None,
        validator=None,
        handler=get_tasks
    ),
    Resource(
        method='GET',
        url='/api/contests/{contest_id}/tasks/{task_id}',
        allowed_roles=None,
        validator=None,
        handler=get_task
    ),
    Resource(
        method='POST',
        url='/api/tasks',
        allowed_roles=None,
        validator=BodyValidator(schemas.CreateTaskBody),
        handler=create_task
    ),
    Resource(
        method='POST',
        url='/api/solutions',
        allowed_roles=None,
        validator=BodyValidator(schemas.VerifyTaskBody),
        handler=verify_task
    ),
    Resource(
        method='POST',
        url='/api/teams',
        allowed_roles=[UserRole.TRAINER],
        validator=BodyValidator(schemas.CreateTeamBody),
        handler=create_team
    ),
    Resource(
        method='POST',
        url='/api/invites',
        allowed_roles=[UserRole.TRAINER],
        validator=BodyValidator(schemas.CreateMemberBody),
        handler=create_member
    ),
    Resource(
        method='DELETE',
        url='/api/invites/{invite_id}',
        allowed_roles=[UserRole.TRAINER],
        validator=BodyValidator(schemas.DeleteMemberBody),
        handler=delete_member
    ),
    Resource(
        method='PUT',
        url='/api/invites/{invite_id}/accept',
        allowed_roles=[UserRole.PARTICIPANT],
        validator=BodyValidator(schemas.AcceptInviteBody),
        handler=accept_invite
    ),
    Resource(
        method='PUT',
        url='/api/invites/{invite_id}/decline',
        allowed_roles=[UserRole.PARTICIPANT],
        validator=BodyValidator(schemas.DeclineInviteBody),
        handler=decline_accept
    )
]


resources_map = {
    (resource.method, resource.url): resource
    for resource in resources
}


def setup_routes(app, resources):
    for resource in resources:
        app.router.add_route(
            resource.method,
            resource.url,
            resource.handler
        )
    # app.router.add_post('/users', register_user)
    #
    # app.router.add_post('/login', authenticate_user)
    #
    # app.router.add_get('/api/contests', get_contests)
    # app.router.add_get('/api/contests/{contest_id}', get_contest)
    # app.router.add_post('/api/contests', create_contest)
    #
    # app.router.add_get('/api/contests/{contest_id}/tasks', get_tasks)
    # app.router.add_get('/api/contests/{contest_id}/tasks/{task_id}', get_task)
    # app.router.add_post('/api/tasks', create_task)
    #
    # app.router.add_post('/api/solutions', verify_task)
    #
    # app.router.add_post('/api/teams', create_team)
    #
    # app.router.add_post('/api/invites', create_member)
    # app.router.add_delete('/api/invites/{invite_id}', delete_member)
    # app.router.add_put('/api/invites/{invite_id}/accept', accept_invite)
    # app.router.add_put('/api/invites/{invite_id}/decline', decline_accept)
