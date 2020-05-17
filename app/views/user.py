from functools import partial

from aiohttp import web

import utils.executor as executor
from commandbus.commands.user import RegisterUser
from db import user_mapper, team_mapper
from exceptions.entity import EntityNotFound
from exceptions.role import PermissionException
from transformers import transform_invite, transform_user
from utils.injector import inject
from utils.injector.entity import Contest, Team
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


@inject(Team)  # TODO: also validate if this team in this contest
async def get_sent_invites_for_team(request):
    engine = request.app['db']

    user = request['user']
    team = request['team']

    if not team.is_trainer(user):
        raise PermissionException(
            'you are not allowed to view invites for this team!',
            {'team_id': team.id}
        )

    invites = await team_mapper.get_members(
        engine, team
    )
    return web.json_response({
        'invites': [
            transform_invite(i)
            for i in invites
            if i.is_status_pending()  # TODO: create sql query for it
        ]
    })


@inject(Contest)
async def get_received_invites_for_contest(request):
    engine = request.app['db']

    contest = request['contest']
    user = request['user']

    invites = await user_mapper.get_received_invites_for_contest(
        engine, user, contest
    )

    return web.json_response({
        'invites': [transform_invite(i) for i in invites]
    })


async def get_user(request):
    engine = request.app['db']

    user_id = request.match_info.get('user_id')
    if user_id == 'me':
        return web.json_response({
            'user': transform_user(request['user'])
        })

    user = await user_mapper.get(engine, user_id)
    if user is None:
        raise EntityNotFound(
            f'there is no user with id {user_id}',
            {'user_id': user_id}
        )
    return web.json_response({
        'user': transform_user(user)
    })


async def get_users(request):
    engine = request.app['db']

    users = await user_mapper.get_all(engine)

    return web.json_response({
        'users': [transform_user(p) for p in users]
    })
