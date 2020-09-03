from aiohttp import web

from app.core.user.transformers import UserTransformer
from app.db import UserMapper
from app.exceptions.entity import EntityNotFound


async def get_user(
        request,
        user_mapper: UserMapper,
        user_transformer: UserTransformer
        ):

    user_id = request.match_info.get('user_id')
    if user_id == 'me':
        return web.json_response({
            'user': await user_transformer.transform(request['user'])
        })

    user = await user_mapper.find(user_id)
    if user is None:
        raise EntityNotFound(
            f'There is no user with id {user_id}',
            {'user_id': user_id}
        )

    return web.json_response({
        'user': await user_transformer.transform(user)
    })


async def get_users(
        request,
        user_mapper,
        user_transformer: UserTransformer
        ):
    users = await user_mapper.find_all()

    return web.json_response({
        'users': await user_transformer.transform_many(users)
    })
