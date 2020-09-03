from asyncio import gather

from aiohttp import web

from app.db import (
    contest_mapper,
    team_mapper,
    team_member_mapper,
    mappers_container
)
from app.commandbus.commands.team_member import CreateTeamMember
from app.core.team_member import MemberStatus
from app.exceptions.entity import EntityNotFound
from app.exceptions.role import PermissionException
from app.transformers import transform_member
from app.utils.injector import inject
from app.utils.injector.entity import Team, Contest, Invite


@inject(Team)
async def create_member(request):
    bus = request.app['bus']
    engine = request.app['db']

    user_email = request['body']['email']
    team = request['team']

    # TODO: temporary solution, inject user_mapper after refactoring domain-related code
    user_mapper = mappers_container.user_mapper()

    requested_user = await user_mapper.find_one_by(email=user_email)
    if requested_user is None:
        raise EntityNotFound(
            f'there is no user with email {user_email}',
            {'email': user_email}
        )

    if not requested_user.is_participant():
        raise PermissionException(
            "you can't invite this user!",
            {'user_id': requested_user.id}
        )

    team_members, contest = await gather(
        team_mapper.get_members(engine, team),
        contest_mapper.get(engine, team.contest_id)
    )

    if contest.is_running():
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

    if any(
            tm.user_id == requested_user.id
            and tm.team_id == team.id
            for tm in team_members
            ):
        return web.json_response({
            'error': "user already have invite for this team",
            'payload': {}
        }, status=400)

    member = await bus.execute(
        CreateTeamMember(
            user=requested_user,
            team=team,
            status=MemberStatus.PENDING,
            engine=engine
        )
    )

    return web.json_response({'member_id': member.id}, status=201)


@inject(Team, Contest)
async def get_accepted_members(request):
    engine = request.app['db']

    team = request['team']
    contest = request['contest']

    if not team.from_contest(contest):
        raise EntityNotFound(
            'there is no such team in requested contest',
            {'team_id': team.id, 'contest_id': contest.id}
        )

    team_members = await team_mapper.get_members(engine, team)

    # TODO: rewrite it to sql query. maybe change team_mapper.get_members function
    team_accepted_members = [
        tm
        for tm in team_members
        if tm.is_status_accepted()
    ]
    return web.json_response({
        'members': [transform_member(tm) for tm in team_accepted_members]
    })


@inject(Invite)
async def delete_member(request):
    engine = request.app['db']

    user = request['user']
    member = request['member']  # this is injected invite
    contest = await team_member_mapper.get_contest(engine, member)
    team = await team_member_mapper.get_team(engine, member)

    if not team.is_trainer(user):
        raise PermissionException('you are not allowed to delete this participant!')

    if contest.is_running():
        return web.json_response({
            'error': f"you can't delete member from running contest!",
            'payload': {}
        }, status=400)

    await team_member_mapper.delete(engine, member)
    return web.json_response({
        'message': 'successfully deleted'
    })


@inject(Invite)
async def accept_invite(request):
    # TODO: temporary solution, inject user_mapper after refactoring domain-related code
    user_mapper = mappers_container.user_mapper()

    engine = request.app['db']

    member = request['member']
    user_id = request['user'].id

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

    if contest.is_running():
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


@inject(Invite)
async def decline_accept(request):
    engine = request.app['db']
    member = request['member']
    user_id = request['user'].id

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

    # TODO: should i return this line back? should i remove DECLINED status?
    # TODO: REFACTOR THIS
    # member.set_status(MemberStatus.DECLINED)
    await team_member_mapper.delete(engine, member)
    return web.json_response({
        'status': 'changes applied successfully',
    }, status=200)
