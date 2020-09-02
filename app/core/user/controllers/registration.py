from aiohttp import web

from app.commandbus import Bus
from app.core.user.commands import CreateUser
from app.core.user.transformers import UserTransformer
from app.db import UserMapper


async def register_user(
        request: web.Request,
        bus: Bus,
        user_mapper: UserMapper,
        transformer: UserTransformer
        ):
    body = request['body']

    user = await bus.execute(
        CreateUser(
            email=body['email'],
            password=body['password'],
            first_name=body['first_name'],
            last_name=body['last_name'],
            patronymic=body['patronymic'],
            role=body['role']
        )
    )

    await user_mapper.create(user)

    return web.json_response(await transformer.transform(user))
