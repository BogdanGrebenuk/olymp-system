from concurrent.futures import Executor
from dataclasses import dataclass
from pathlib import Path

from aiopg.sa import Engine

from app.commandbus.commands.base_command import Command
from app.core.user.domain.entity import User
from app.db.entities import (
    Contest,
    Solution,
    Task,
    Team
)


@dataclass
class CreateSolution(Command):
    engine: Engine
    contest: Contest
    task: Task
    user: User
    team: Team
    language: str
    code: str
    pool: Executor


@dataclass
class PrepareSolutionDir(Command):
    contest_id: str
    task_id: str
    solution_id: str
    pool: Executor


@dataclass
class SaveSolutionCode(Command):
    solution_dir_path: Path
    language: str
    code: str
    pool: Executor


@dataclass
class VerifySolution(Command):
    engine: Engine
    solution: Solution
    task: Task
    pool: Executor
    docker_meta: dict
