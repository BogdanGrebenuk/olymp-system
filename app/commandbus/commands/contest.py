from dataclasses import dataclass

from aiopg.sa import Engine

from commandbus.commands.base_command import Command


@dataclass
class CreateContest(Command):
    name: str
    description: str
    image: bytes
    engine: Engine


@dataclass
class SaveContestImage(Command):
    img: bytes
    img_path: str

