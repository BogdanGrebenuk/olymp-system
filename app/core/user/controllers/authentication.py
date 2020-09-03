from aiohttp import web

from app.core.user.services import PasswordChecker
from app.db import UserMapper
from app.exceptions.entity import EntityNotFound, EntityException
from app.utils.token import TokenGenerator


async def authenticate_user(
        request,
        password_checker: PasswordChecker,
        token_generator: TokenGenerator,
        user_mapper: UserMapper
        ):
    body = request['body']

    email = body['email']
    password = body['password']

    user = await user_mapper.find_one_by(email=email)
    if user is None:
        raise EntityNotFound(
            f'There is no user with email {email}',
            {'email': email}
        )

    if not password_checker.check(password, user.password):
        raise EntityException('Incorrect password')

    token = await token_generator.generate({'user_id': user.id})

    return web.json_response({'token': token})
