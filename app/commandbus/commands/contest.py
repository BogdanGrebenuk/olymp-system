from concurrent.futures import Executor
from dataclasses import dataclass
from datetime import datetime
from typing import Union

from aiohttp.web import FileField
from aiopg.sa import Engine

from app.commandbus.commands.base_command import Command


@dataclass
class CreateContest(Command):
    name: str
    description: str
    max_teams: Union[int, None]
    max_participants_in_team: int
    image: Union[FileField, None]
    start_date: datetime
    end_date: datetime
    creator_id: str
    engine: Engine
    pool: Executor


@dataclass
class GenerateContestImagePath(Command):
    image: Union[FileField]
