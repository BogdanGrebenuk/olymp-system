import bcrypt
import uuid

from commandbus.command_handlers.base_command_handler import CommandHandler
from commandbus.commands.user import RegisterUser
from db import user_mapper
from db.entities.user import User


class RegisterUserHandler(CommandHandler):

    async def handle(self, command: RegisterUser):
        engine = command.engine

        user_id = str(uuid.uuid4())
        password = command.password.encode(encoding='utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password, salt).decode()

        user = User(
            user_id,
            command.first_name,
            command.last_name,
            command.patronymic,
            command.email,
            hashed_password,
            command.role
        )
        await user_mapper.create(engine, user)
        return user
