from dataclasses import dataclass

from commandbus.commands.base_command import Command


@dataclass
class CreateUser(Command):
    email: str
    password: str
    first_name: str
    last_name: str
    patronymic: str
    role: str
