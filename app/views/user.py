from aiohttp import web

import core.validators as domain_validator
from core.team_member import MemberStatus
from db import user_mapper, team_mapper
from transformers import transform_invite
from utils.injector import inject
from utils.injector.entity import Contest, Team


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
    engine = request.app['db']

    contest = request['contest']
    user = request['user']

    invites = await user_mapper.get_received_invites_for_contest(
        engine, user, contest
    )

    return web.json_response({
        'invites': [transform_invite(i) for i in invites]
    })
