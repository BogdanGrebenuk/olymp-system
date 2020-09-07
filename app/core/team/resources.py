import app.core.team.schemas as schemas
from app.core.team.containers import controllers
from app.core.user.domain.role import UserRole
from app.utils.request import RequestValidator, UrlVariableManager, ParamsManager
from app.utils.resource import Resource, SingleParamChooser

resources = [
    Resource(
        method='POST',  # TODO make this route restful
        url='/api/teams',
        allowed_roles=[UserRole.TRAINER],
        validators=[RequestValidator(schemas.CreateTeamBody)],
        handler=controllers.create_team
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
        handler=SingleParamChooser(
            'creator_id',
            controllers.get_teams_for_contest_and_creator,
            controllers.get_teams_for_contest
        ).handle
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
        handler=controllers.get_team
    )
]
