from functools import partial

from aiohttp import web

import utils.executor as executor
from commandbus.commands.user import RegisterUser
from db.procedures.user import get_user_by_email
from utils.request import validate_body
from utils.token import create_token
from validators.request import (
    AuthenticateUserBody,
    RegisterUserBody
)


@validate_body(schema=RegisterUserBody)
async def register_user(request):
    body = request['body']

    bus = request.app['bus']
    engine = request.app['db']

    email = body['email']
    first_name = body['first_name']
    last_name = body['last_name']
    patronymic = body['patronymic']
    password = body['password']
    role = body['role']

    user = await bus.execute(
        RegisterUser(
            email, password, first_name, last_name, patronymic, role, engine
        )
    )

    return web.json_response({'user_id': user.id})


@validate_body(schema=AuthenticateUserBody)
async def authenticate_user(request):
    body = request['body']
    engine = request.app['db']
    pool = request.app['process_pool']

    email = body['email']
    password = body['password']

    user = await get_user_by_email(engine, email)
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

    if not user.check_password(password):
        return web.json_response(
            {
                'error': f'incorrect password!',
                'payload': {}
            },
            status=400
        )

    token_config = request.app['config']['token']
    task = partial(
        create_token,

        {'user_id': user.id},
        token_config
    )
    token = await executor.run(task, pool)

    return web.json_response(
        {'token': token}
    )
