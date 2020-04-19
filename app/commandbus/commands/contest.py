from dataclasses import dataclass

from aiopg.sa import Engine

from commandbus.commands.base_command import Command


@dataclass
class CreateContest(Command):
    name: str
    engine: Engine
