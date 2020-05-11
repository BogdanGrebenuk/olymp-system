from asyncio import gather

from aiohttp import web

import utils.injector as injector
from db import (
    contest_mapper,
    team_mapper,
    team_member_mapper,
    user_mapper
)
from commandbus.commands.team_member import CreateTeamMember
from core.team_member import MemberStatus


@injector.inject(injector.TeamFromBody)
async def create_member(request):
    bus = request.app['bus']
    engine = request.app['db']
    body = request['body']

    team_id = body['team_id']
    user_id = body['user_id']

    team = await team_mapper.get(engine, team_id)
    if team is None:
        return web.json_response({
            'error': f'there is no team with id {team_id}',
            'payload': {'team_id': team_id}
        }, status=400)

    user = await user_mapper.get(engine, user_id)
    if user is None:
        return web.json_response({
            'error': f'there is no user with id {user_id}',
            'payload': {'user_id': user_id}
        }, status=400)

    team_members, contest = await gather(
        team_mapper.get_members(engine, team),
        contest_mapper.get(engine, team.contest_id)
    )

    if contest.is_started():
        return web.json_response({
            'error': "you can't add member for already running contest!",
            'payload': {'contest_id': contest.id}
        }, status=400)

    if len(team_members) + 1 > contest.max_participants_in_team:
        return web.json_response({
            'error': "team has reached members limit",
            'payload': {
                'max_participants_in_team': contest.max_participants_in_team
            }
        }, status=400)

    member = await bus.execute(
        CreateTeamMember(
            user=user,
            team=team,
            status=MemberStatus.PENDING,
            engine=engine
        )
    )

    return web.json_response({'member_id': member.id}, status=201)


async def delete_member(request):
    engine = request.app['db']
    body = request['body']

    member_id = body['member_id']
    member = await team_member_mapper.get(engine, member_id)

    if member is None:
        return web.json_response({
            'error': f'there is no team member with id {member_id}',
            'payload': {'member_id': member_id}
        }, status=403)

    contest = await team_member_mapper.get_contest(engine, member)
    if contest.is_started():
        return web.json_response({
            'error': f"you can't delete member from running contest!",
            'payload': {}
        }, status=400)

    team_member_mapper.delete(engine, member)
    return web.json_response({
        'message': 'successfully deleted'
    })


async def accept_invite(request):
    engine = request.app['db']
    body = request['body']

    member_id = body['member_id']
    user_id = request['user'].id

    member = await team_member_mapper.get(engine, member_id)
    if member is None:
        return web.json_response({
            'error': f'there is no team member with id {member_id}',
            'payload': {'member_id': member_id}
        }, status=403)

    if member.user_id != user_id:
        return web.json_response({
            'error': f'you have no permission to accept this invite!',
            'payload': {'member_id': member.id}
        }, status=403)

    if not member.is_status_pending():
        return web.json_response({
            'error': f"you can't accept invite with non-pending status",
            'payload': {'status': member.status}
        }, status=400)

    contest = await team_member_mapper.get_contest(engine, member)

    accepted_team = await user_mapper.get_accepted_team_for_contest(
        engine, request['user'], contest
    )

    if accepted_team is not None:
        return web.json_response({
            'error': f"you've already accepted invite for team {accepted_team.name}",
            'payload': {'team_id': accepted_team.id}

        }, status=400)

    if contest.is_started():
        return web.json_response({
            'error': f"you can't accept invite for running contest!",
            'payload': {}
        }, status=400)

    member.set_status(MemberStatus.ACCEPTED)
    await team_member_mapper.update(engine, member)
    # TODO: investigate if 'put' response has body
    return web.json_response({
        'status': 'changes applied successfully',
    }, status=200)


async def decline_accept(request):
    engine = request.app['db']
    body = request['body']

    member_id = body['member_id']
    user_id = request['user'].id

    member = await team_member_mapper.get(engine, member_id)
    if member is None:
        return web.json_response({
            'error': f'there is no team member with id {member_id}',
            'payload': {'member_id': member_id}
        }, status=403)

    if member.user_id != user_id:
        return web.json_response({
            'error': f'you have no permission to decline this invite!',
            'payload': {'member_id': member.id}
        }, status=403)

    if not member.is_status_pending():
        return web.json_response({
            'error': f"you can't decline invite with non-pending status",
            'payload': {'status': member.status}
        }, status=400)

    member.set_status(MemberStatus.DECLINED)
    await team_member_mapper.update(member)
    return web.json_response({
        'status': 'changes applied successfully',
    }, status=200)
