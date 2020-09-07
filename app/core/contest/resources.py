import app.core.contest.schemas as schemas
from app.core.contest.containers import controllers
from app.utils.resource import Resource
from app.utils.request import RequestValidator, UrlVariableManager, DataFormManager
from app.core.user.domain.role import UserRole


resources = [
    Resource(
        method='GET',
        url='/api/contests',
        allowed_roles=None,
        validators=[],
        handler=controllers.get_contests.as_view()
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
        handler=controllers.get_contest.as_view()
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
        handler=controllers.create_contest.as_view()
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
        handler=controllers.get_leader_board.as_view()
    )
]