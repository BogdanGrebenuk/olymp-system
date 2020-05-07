from dataclasses import dataclass
from typing import List, Tuple

from aiopg.sa import Engine

from commandbus.commands.base_command import Command
from db.entities.contest import Contest


@dataclass
class CreateTask(Command):
    engine: Engine
    contest: Contest
    input_output: List[Tuple[str, str]]
    name: str
    description: str
    max_cpu_time: int
    max_memory: int
