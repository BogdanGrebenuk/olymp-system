from dataclasses import dataclass

from aiopg.sa import Engine

from app.commandbus.commands.base_command import Command


@dataclass
class CreateTeam(Command):
    name: str
    contest_id: str
    trainer_id: str
    engine: Engine
