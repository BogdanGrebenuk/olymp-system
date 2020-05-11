from db import (
    contest_mapper,
    team_mapper
)
from exceptions.entity import EntityNotFound


class Entity:

    def __init__(self, entity_description, id_field, mapper):
        self.entity_description = entity_description
        self.id_field = id_field
        self.mapper = mapper

    async def resolve(self, request):
        entity_id = request['body'][self.id_field]
        entity = await self.mapper.get(request.app['db'], entity_id)
        if entity is None:
            raise EntityNotFound(
                f'there is no {self.entity_description} with id {entity_id}',
                {self.id_field: entity_id}
            )
        request[self.entity_description] = entity


Contest = Entity('contest', 'contest_id', contest_mapper)
Team = Entity('team', 'team_id', team_mapper)
