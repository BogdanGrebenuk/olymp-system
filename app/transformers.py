from dataclasses import asdict

from db.entities.task import Task
from db.entities.contest import Contest


def transform_task(task: Task):
    return asdict(task)


def transform_contest(contest: Contest):
    return asdict(contest)
