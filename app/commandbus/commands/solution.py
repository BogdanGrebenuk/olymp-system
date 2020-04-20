from dataclasses import dataclass

from aiopg.sa import Engine

from commandbus.commands.base_command import Command
from db.entities.contest import Contest
from db.entities.solution import Solution
from db.entities.task import Task


@dataclass
class CreateSolution(Command):
    engine: Engine
    contest: Contest
    task: Task
    language: str
    code: str


@dataclass
class PrepareSolutionDir(Command):
    contest_id: str
    task_id: str
    solution_id: str


@dataclass
class SaveSolutionCode(Command):
    solution_dir_path: str
    language: str
    code: str


@dataclass
class VerifySolution(Command):
    engine: Engine
    solution: Solution
    task: Task
