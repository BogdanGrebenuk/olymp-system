from aiohttp import web

import app.core.validators as domain_validator
from app.core.team_member import MemberStatus
from app.db import team_mapper, mappers_container
from app.transformers import transform_invite
from app.utils.injector import inject
from app.utils.injector.entity import Contest, Team


@inject(Contest, Team)
async def get_sent_invites_for_team(request):
    engine = request.app['db']

    user = request['user']
    contest = request['contest']
    team = request['team']

    await domain_validator.get_sent_invites_for_team(user, contest, team)

    invites = await team_mapper.get_members(
        engine, team, MemberStatus.PENDING
    )
    return web.json_response({
        'invites': [transform_invite(i) for i in invites]
    })


@inject(Contest)
async def get_received_invites_for_contest(request):
    # TODO: temporary solution, inject user_mapper after refactoring domain-related code
    user_mapper = mappers_container.user_mapper()

    engine = request.app['db']

    contest = request['contest']
    user = request['user']

    invites = await user_mapper.get_received_invites_for_contest(
        engine, user, contest
    )

    return web.json_response({
        'invites': [transform_invite(i) for i in invites]
    })
