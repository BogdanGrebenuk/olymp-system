import uuid

from commandbus.command_handlers.base_command_handler import CommandHandler
from core.user.commands import CreateUser
from core.user.services import PasswordGenerator
from core.user.domain.entity import User


class CreateUserHandler(CommandHandler):

    def __init__(self, hash_client: PasswordGenerator, bus):
        self.hash_client = hash_client
        self.bus = bus

    async def handle(self, command: CreateUser):
        user_id = str(uuid.uuid4())
        hashed_password = self.hash_client.generate(command.password)

        user = User(
            id=user_id,
            first_name=command.first_name,
            last_name=command.last_name,
            patronymic=command.patronymic,
            email=command.email,
            password=hashed_password,
            role=command.role
        )

        return user
