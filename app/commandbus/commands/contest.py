from dataclasses import dataclass
from os import PathLike
from typing import Union

from aiohttp.web import FileField
from aiopg.sa import Engine

from commandbus.commands.base_command import Command


@dataclass
class CreateContest(Command):
    name: str
    description: str
    image: Union[FileField, None]
    engine: Engine


@dataclass
class SaveContestImage(Command):
    image_bytes: bytes
    image_path: PathLike

