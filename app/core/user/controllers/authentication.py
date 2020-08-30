from aiohttp import web
from aiopg.sa import Engine

from core.user.services import PasswordChecker
from utils.token import TokenGenerator


async def authenticate_user(
        request,
        password_checker: PasswordChecker,
        token_generator: TokenGenerator,
        user_mapper,
        engine: Engine
        ):
    body = request['body']

    email = body['email']
    password = body['password']

    user = await user_mapper.get_user_by_email(engine, email)
    if user is None:
        return web.json_response(
            {
                'error': f'there is no user with email "{email}"',
                'payload': {
                    'email': email
                }
            },
            status=400
        )

    if not password_checker.check(password, user.password):
        return web.json_response(
            {
                'error': f'incorrect password!',
                'payload': {}
            },
            status=400
        )

    token = await token_generator.generate({'user_id': user.id})

    return web.json_response(
        {'token': token}
    )
