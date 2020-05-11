from dataclasses import asdict

from db.entities.task import Task
from db.entities.contest import Contest
from db.entities.team_member import TeamMember


def transform_task(task: Task):
    return asdict(task)


def transform_contest(contest: Contest):
    return asdict(contest)


def transform_invite(invite: TeamMember):
    return asdict(invite)
