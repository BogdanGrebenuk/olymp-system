from datetime import datetime

from db.entities import (
    Contest,
    Task,
    TeamMember,
    User,
    Team,
    Solution
)
from services.codesaver import get_code


def transform_datetime(dt: datetime):
    return dt.strftime('%Y-%m-%dT%H:%M:%S.000Z')


def transform_task(task: Task):
    return {
        'id': task.id,
        'contestId': task.contest_id,
        'description': task.description,
        'maxCpuTime': task.max_cpu_time,
        'maxMemory': task.max_memory,
        'name': task.name
    }


def transform_contest(contest: Contest):
    return {
        'id': contest.id,
        'name': contest.name,
        'description': contest.description,
        'imagePath': contest.image_path,
        'endDate': transform_datetime(contest.end_date),
        'startDate': transform_datetime(contest.start_date),
        'creatorId': contest.creator_id,
        'maxParticipantsInTeam': contest.max_participants_in_team,
        'maxTeams': contest.max_teams
    }


def transform_invite(invite: TeamMember):
    return {
        'id': invite.id,
        'userId': invite.user_id,
        'teamId': invite.team_id,
        'status': invite.status
    }


def transform_member(member: TeamMember):
    return {
        'id': member.id,
        'userId': member.user_id,
        'teamId': member.team_id,
        'status': member.status
    }


def transform_user(user: User):
    return {
        'id': user.id,
        'email': user.email,
        'firstName': user.first_name,
        'lastName': user.last_name,
        'role': user.role,
        'patronymic': user.patronymic
    }


def transform_team(team: Team):
    return {
        'id': team.id,
        'name': team.name,
        'contestId': team.contest_id,
        'trainerId': team.trainer_id
    }


def transform_solution(solution: Solution):
    return {
        'id': solution.id,
        'taskId': solution.task_id,
        'language': solution.language,
        'isPassed': solution.is_passed,
        'teamId': solution.team_id,
        'userId': solution.user_id
    }
