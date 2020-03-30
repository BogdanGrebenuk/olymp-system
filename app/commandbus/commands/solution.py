from dataclasses import dataclass

from commandbus.commands.base_command import Command


@dataclass
class CreateSolution(Command):
    user_id: int
    contest_id: int
    task_id: int
    language: str
    code: str


@dataclass
class PrepareSolutionDir(Command):
    user_id: int
    contest_id: int
    task_id: int
    solution_id: str


@dataclass
class SaveSolutionCode(Command):
    solution_dir_path: str
    language: str
    code: str


@dataclass
class VerifySolution(Command):
    solution: dict  # TODO: pass Solution entity class




