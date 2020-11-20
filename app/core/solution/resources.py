import app.core.solution.schemas as schemas
from app.core.solution.containers import controllers
from app.utils.request import (
    RequestValidator,
    UrlVariableManager,
    ParamsManager
)
from app.utils.resource import Resource, SingleParamChooser


resources = [
    Resource(
        method='POST',
        url='/api/contests/{contest_id}/solutions',
        allowed_roles=None,
        validators=[
            RequestValidator(
                schemas.CreateSolutionUrlVars, data_manager=UrlVariableManager
            ),
            RequestValidator(schemas.CreateSolutionBody)
        ],
        handler=controllers.create_solution.as_view()
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
            controllers.get_solutions_for_team.as_view(),
            controllers.get_solutions_for_contest.as_view()
        ).handle
    ),
    Resource(
        method='GET',
        url='/api/contests/{contest_id}/solutions/{solution_id}/code',  # TODO: not restful
        allowed_roles=None,
        validators=[
            RequestValidator(
                schemas.GetSolutionCodeUrlVars,
                data_manager=UrlVariableManager
            )
        ],
        handler=controllers.get_solution_code.as_view()
    ),
]
