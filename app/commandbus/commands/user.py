from dataclasses import dataclass

from aiopg.sa import Engine

from commandbus.commands.base_command import Command


@dataclass
class RegisterUser(Command):
    email: str
    password: str
    first_name: str
    last_name: str
    patronymic: str
    role: str
    engine: Engine
