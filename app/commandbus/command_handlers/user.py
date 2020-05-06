import bcrypt
import uuid

from commandbus.command_handlers.base_command_handler import CommandHandler
from commandbus.commands.user import RegisterUser
from db.entities.user import User
from db.procedures.user import create_user


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
            command.role.id
        )
        await create_user(engine, user)
        return user
