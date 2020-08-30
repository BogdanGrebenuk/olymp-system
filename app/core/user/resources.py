import app.core.user.schemas as schemas
from app.core.user.containers import controllers
from app.utils.request import RequestValidator, UrlVariableManager
from app.utils.resource import Resource


resources = [
    Resource(
        method='POST',
        url='/users',
        allowed_roles=None,
        validators=[RequestValidator(schemas.RegisterUserBody)],
        handler=controllers.register_user.as_view()
    ),
    Resource(
        method='POST',
        url='/login',
        allowed_roles=None,
        validators=[RequestValidator(schemas.AuthenticateUserBody)],
        handler=controllers.authenticate_user.as_view()
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
        handler=controllers.get_user.as_view()
    ),
    Resource(
        method='GET',
        url='/api/users',
        allowed_roles=None,
        validators=[],
        handler=controllers.get_users.as_view()
    )
]
