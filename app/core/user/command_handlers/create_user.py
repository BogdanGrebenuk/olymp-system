import uuid

from app.commandbus.command_handlers.base_command_handler import CommandHandler
from app.core.user.commands import CreateUser
from app.core.user.services import PasswordGenerator
from app.core.user.domain.entity import User
from app.db import UserMapper
from app.exceptions.domain import DomainException


class CreateUserHandler(CommandHandler):

    def __init__(
            self,
            hash_client: PasswordGenerator,
            user_mapper: UserMapper
            ):
        self.hash_client = hash_client
        self.user_mapper = user_mapper

    async def handle(self, command: CreateUser):
        email = command.email

        user = await self.user_mapper.find_one_by(email=email)
        if user is not None:
            raise DomainException(
                f'User with email {email} already exists!',
                {'email': email}
            )

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
