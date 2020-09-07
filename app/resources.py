import app.validators.schemas as schemas
from app.core.team.resources import resources as team_resources
from app.core.user.resources import resources as user_resources
from app.core.user.domain.role import UserRole
from app.utils.resource import SingleParamChooser, combine_resources, Resource
from app.utils.request import (
    RequestValidator,
    DataFormManager,
    ParamsManager,
    UrlVariableManager
)
from app.views.contest import (
    create_contest,
    get_contests,
    get_contest,
    get_leader_board
)
from app.views.solution import (
    create_solution,
    get_solutions_for_contest,
    get_solutions_for_team,
    get_solution_code
)
from app.views.task import (
    create_task,
    get_tasks,
    get_task
)
# from app.views.team import (
#     create_team,
#     get_teams_for_contest,
#     get_teams_for_contest_and_creator,
#     get_team
# )
from app.views.team_member import (
    create_member,
    get_accepted_members,
    accept_invite,
    decline_accept,
    delete_member
)
from app.views.user import (
    get_sent_invites_for_team,
    get_received_invites_for_contest
)

resources = [
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
        url='/api/tasks',  # TODO make this route restful
        allowed_roles=None,
        validators=[RequestValidator(schemas.CreateTaskBody)],
        handler=create_task
    ),
    Resource(
        method='POST',
        url='/api/contests/{contest_id}/solutions',
        allowed_roles=[UserRole.PARTICIPANT],
        validators=[
            RequestValidator(
                schemas.CreateSolutionUrlVars, data_manager=UrlVariableManager
            ),
            RequestValidator(schemas.CreateSolutionBody)
        ],
        handler=create_solution
    ),
    Resource(
        method='GET',
        url='/api/contests/{contest_id}/solutions',
        allowed_roles=None,
        validators=[
            RequestValidator(
                schemas.GetSolutionsUrlVars,
                data_manager=UrlVariableManager
            ),
            RequestValidator(
                schemas.GetSolutionParams,
                data_manager=ParamsManager
            )
        ],
        handler=SingleParamChooser(
            'team_id',
            get_solutions_for_team,
            get_solutions_for_contest
        ).handle
    ),
    Resource(
        method='GET',
        url='/api/contests/{contest_id}/solutions/{solution_id}/code',  # is it restful?
        allowed_roles=None,
        validators=[
            RequestValidator(
                schemas.GetSolutionCodeUrlVars,
                data_manager=UrlVariableManager
            )
        ],
        handler=get_solution_code
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
        url='/api/invites',  # TODO make this route restful
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
        url='/api/invites/{invite_id}/accept',  # TODO make this route restful
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
        url='/api/invites/{invite_id}/decline',  # TODO make this route restful
        allowed_roles=[UserRole.PARTICIPANT],
        validators=[
            RequestValidator(
                schemas.DeclineInviteUrlVars,
                data_manager=UrlVariableManager
            )
        ],
        handler=decline_accept
    ),
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
        url='/api/invites/received',  # TODO make this route restful
        allowed_roles=[UserRole.PARTICIPANT],
        validators=[
            RequestValidator(
                schemas.GetReceivedInvitesParams,
                data_manager=ParamsManager
            )
        ],
        handler=get_received_invites_for_contest
    ),
    # TODO: reinvestigate this resource
    Resource(
        method='GET',
        url='/api/contests/{contest_id}/leader-board',
        allowed_roles=None,
        validators=[
            RequestValidator(
                schemas.GetContestLeaderBoardUrlVars,
                data_manager=UrlVariableManager  # TODO: make it enum-like field?
            )
        ],
        handler=get_leader_board
    )
]

resources = combine_resources(
    resources,
    user_resources, team_resources
)


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
