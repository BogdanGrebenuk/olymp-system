from db import (
    contest_mapper,
    team_mapper
)
from exceptions.entity import EntityNotFound


class Entity:

    def __init__(self, entity_description, id_extractor, mapper):
        self.entity_description = entity_description
        self.id_extractor = id_extractor
        self.mapper = mapper

    async def resolve(self, request):
        entity_id = self.id_extractor(request)
        entity = await self.mapper.get(request.app['db'], entity_id)
        if entity is None:
            raise EntityNotFound(
                f'there is no {self.entity_description} with id {entity_id}',
                {'entity_id': entity_id}
            )
        request[self.entity_description] = entity


def extract_from(source, id_attr_value):
    def wrapper(request):
        return request[source][id_attr_value]
    return wrapper


ContestFromBody = Entity(
    'contest',
    extract_from('body', 'contest_id'),
    contest_mapper
)


ContestFromParams = Entity(
    'contest',
    extract_from('params', 'contest_id'),
    contest_mapper
)


TeamFromBody = Entity(
    'team',
    extract_from('body', 'team_id'),
    team_mapper
)
