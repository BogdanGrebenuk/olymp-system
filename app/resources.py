from dataclasses import dataclass
from typing import Callable, List, Union, Awaitable

from aiohttp.web import BaseRequest

import validators.schemas as schemas
from core.user_role import UserRole
from validators import Validator
from validators.request import (
    RequestValidator,
    DataFormManager,
    ParamsManager,
    UrlVariableManager
)
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
from views.team import (
    create_team,
    get_teams,
    get_team
)
from views.team_member import (
    create_member,
    get_accepted_members,
    accept_invite,
    decline_accept,
    delete_member
)
from views.user import (
    authenticate_user,
    register_user,
    get_sent_invites_for_contest,
    get_sent_invites_for_team,
    get_received_invites_for_contest,
    get_users,
    get_user
)


@dataclass
class Resource:
    method: str
    url: str
    allowed_roles: Union[List[UserRole], None]  # if None, there is no restrictions
    validators: List[Validator]
    handler: Callable[[BaseRequest], Awaitable]


resources = [
    Resource(
        method='POST',
        url='/users',
        allowed_roles=None,
        validators=[RequestValidator(schemas.RegisterUserBody)],
        handler=register_user
    ),
    Resource(
        method='POST',
        url='/login',
        allowed_roles=None,
        validators=[RequestValidator(schemas.AuthenticateUserBody)],
        handler=authenticate_user
    ),
    Resource(
        method='GET',
        url='/api/contests',
        allowed_roles=None,
        validators=[],
        handler=get_contests
    ),
    Resource(
        method='GET',
        url='/api/contests/{contest_id}',
        allowed_roles=None,
        validators=[
            RequestValidator(
                schemas.GetContestUrlVars,
                data_manager=UrlVariableManager
            )
        ],
        handler=get_contest
    ),
    Resource(
        method='POST',
        url='/api/contests',
        allowed_roles=[UserRole.ORGANIZER],
        validators=[
            RequestValidator(
                schemas.CreateContestBody,
                data_manager=DataFormManager
            )
        ],
        handler=create_contest
    ),
    Resource(
        method='GET',
        url='/api/contests/{contest_id}/tasks',
        allowed_roles=None,
        validators=[
            RequestValidator(
                schemas.GetTasksUrlVars,
                data_manager=UrlVariableManager
            )
        ],
        handler=get_tasks
    ),
    Resource(
        method='GET',
        url='/api/contests/{contest_id}/tasks/{task_id}',
        allowed_roles=None,
        validators=[
            RequestValidator(
                schemas.GetTaskUrlVars,
                data_manager=UrlVariableManager
            )
        ],
        handler=get_task
    ),
    Resource(
        method='POST',
        url='/api/tasks',
        allowed_roles=None,
        validators=[RequestValidator(schemas.CreateTaskBody)],
        handler=create_task
    ),
    Resource(
        method='POST',
        url='/api/solutions',
        allowed_roles=None,  # TODO: allow only for participants
        validators=[RequestValidator(schemas.VerifyTaskBody)],
        handler=verify_task
    ),
    Resource(
        method='POST',
        url='/api/teams',
        allowed_roles=[UserRole.TRAINER],
        validators=[RequestValidator(schemas.CreateTeamBody)],
        handler=create_team
    ),
    Resource(
        method='GET',
        url='/api/contests/{contest_id}/teams',
        allowed_roles=None,
        validators=[
            RequestValidator(
                schemas.GetTeamsForContestUrlVars,
                data_manager=UrlVariableManager
            ),
            RequestValidator(
                schemas.GetTeamsForContestParams,
                data_manager=ParamsManager
            )
        ],
        handler=get_teams
    ),
    Resource(
        method='GET',
        url='/api/contests/{contest_id}/teams/{team_id}',
        allowed_roles=None,
        validators=[
            RequestValidator(
                schemas.GetTeamUrlVars,
                data_manager=UrlVariableManager
            )
        ],
        handler=get_team
    ),
    Resource(
        method='GET',
        url='/api/contests/{contest_id}/teams/{team_id}/members',
        allowed_roles=None,
        validators=[
            RequestValidator(
                schemas.GetAcceptedMembersUrlVars,
                data_manager=UrlVariableManager
            )
        ],
        handler=get_accepted_members
    ),
    Resource(
        method='POST',
        url='/api/invites',
        allowed_roles=[UserRole.TRAINER],
        validators=[RequestValidator(schemas.CreateMemberBody)],
        handler=create_member
    ),
    Resource(
        method='DELETE',
        url='/api/invites/{invite_id}',
        allowed_roles=[UserRole.TRAINER],
        validators=[
            RequestValidator(
                schemas.DeleteMemberUrlVars,
                data_manager=UrlVariableManager
            )
        ],
        handler=delete_member
    ),
    Resource(
        method='PUT',
        url='/api/invites/{invite_id}/accept',
        allowed_roles=[UserRole.PARTICIPANT],
        validators=[
            RequestValidator(
                schemas.AcceptInviteUrlVars,
                data_manager=UrlVariableManager
            )
        ],
        handler=accept_invite
    ),
    Resource(
        method='PUT',
        url='/api/invites/{invite_id}/decline',
        allowed_roles=[UserRole.PARTICIPANT],
        validators=[
            RequestValidator(
                schemas.DeclineInviteUrlVars,
                data_manager=UrlVariableManager
            )
        ],
        handler=decline_accept
    ),
    # Resource(
    #     method='GET',
    #     url='/api/invites/sent',
    #     allowed_roles=[UserRole.TRAINER],
    #     validators=[
    #         RequestValidator(
    #             schemas.GetSentInvitesParams,
    #             data_manager=ParamsManager
    #         ),
    #     ],
    #     handler=get_sent_invites_for_contest
    # ),
    Resource(
        method='GET',
        url='/api/contests/{contest_id}/teams/{team_id}/invites',
        allowed_roles=[UserRole.TRAINER],
        validators=[
            RequestValidator(
                schemas.GetInvitesForTeamUrlVars,
                data_manager=UrlVariableManager
            )
        ],
        handler=get_sent_invites_for_team
    ),
    Resource(
        method='GET',
        url='/api/invites/received',
        allowed_roles=[UserRole.PARTICIPANT],
        validators=[
            RequestValidator(
                schemas.GetReceivedInvitesParams,
                data_manager=ParamsManager
            )
        ],
        handler=get_received_invites_for_contest
    ),
    Resource(
        method='GET',
        url='/api/users/{user_id}',
        allowed_roles=None,
        validators=[
            RequestValidator(
                schemas.GetUserUrlVars,
                data_manager=UrlVariableManager
            )
        ],
        handler=get_user
    ),
    Resource(
        method='GET',
        url='/api/users',
        allowed_roles=None,
        validators=[],
        handler=get_users
    ),
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
