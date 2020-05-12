from functools import partial

from aiohttp import web

import utils.executor as executor
from commandbus.commands.user import RegisterUser
from db import user_mapper
from transformers import transform_invite
from utils.injector import inject
from utils.injector.entity import Contest
from utils.token import create_token


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


async def authenticate_user(request):
    body = request['body']
    engine = request.app['db']
    pool = request.app['process_pool']

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


@inject(Contest)
async def get_sent_invites_for_contest(request):
    engine = request.app['db']

    contest = request['contest']
    user = request['user']

    invites = await user_mapper.get_sent_invites_for_contest(
        engine, user, contest
    )
    return web.json_response(
        {'invites': [transform_invite(i) for i in invites]}
    )


@inject(Contest)
async def get_received_invites_for_contest(request):
    engine = request.app['db']

    contest = request['contest']
    user = request['user']

    invites = await user_mapper.get_received_invites_for_contest(
        engine, user, contest
    )

    return web.json_response({
        {'invites', [transform_invite(i) for i in invites]}
    })
