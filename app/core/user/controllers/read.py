from aiohttp import web
from aiopg.sa import Engine

from core.user.transformers import UserTransformer
from exceptions.entity import EntityNotFound


async def get_user(
        request,
        user_mapper,
        user_transformer: UserTransformer
        ):
    engine = request.app['db']

    user_id = request.match_info.get('user_id')
    if user_id == 'me':
        return web.json_response({
            'user': await user_transformer.transform(request['user'])
        })

    user = await user_mapper.get(engine, user_id)
    if user is None:
        raise EntityNotFound(
            f'there is no user with id {user_id}',
            {'user_id': user_id}
        )
    return web.json_response({
        'user': await user_transformer.transform(user)
    })


async def get_users(
        request,
        engine: Engine,
        user_mapper,
        user_transformer: UserTransformer
        ):
    users = await user_mapper.get_all(engine)

    return web.json_response({
        'users': [await user_transformer.transform(p) for p in users]
    })
