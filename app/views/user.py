from aiohttp import web

import app.core.validators as domain_validator
from app.core.contest.domain.entity import Contest
from app.core.team_member import MemberStatus
from app.db import mappers_container
from app.transformers import transform_invite
from app.utils.injector import inject
from app.utils.resolver import resolvers_container


async def get_sent_invites_for_team(request):
    engine = request.app['db']
    contest_resolver = resolvers_container.contest_resolver()
    team_resolver = resolvers_container.team_resolver()
    team_mapper = mappers_container.team_mapper()

    user = request['user']
    contest = await contest_resolver.resolve(request)
    team = await team_resolver.resolve(request)

    await domain_validator.get_sent_invites_for_team(user, contest, team)

    invites = await team_mapper.get_members(
        team, MemberStatus.PENDING
    )
    return web.json_response({
        'invites': [transform_invite(i) for i in invites]
    })


async def get_received_invites_for_contest(request):
    # TODO: temporary solution, inject user_mapper after refactoring domain-related code
    user_mapper = mappers_container.user_mapper()
    contest_resolver = resolvers_container.contest_resolver()

    engine = request.app['db']

    contest = await contest_resolver.resolve(request)
    user = request['user']

    invites = await user_mapper.get_received_invites_for_contest(
        user, contest
    )

    return web.json_response({
        'invites': [transform_invite(i) for i in invites]
    })
