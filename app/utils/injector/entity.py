from app.db import (
    contest_mapper,
    task_mapper,
    team_mapper,
    # user_mapper,
    team_member_mapper,
    solution_mapper
)
# from app.db import mappers_container
from app.exceptions.entity import EntityNotFound
from app.utils.injector import default_extractor


# TODO: remove as soon all injects will be removed
class Entity:

    def __init__(
            self,
            entity_description,
            request_attr,
            mapper,
            id_extractor=default_extractor
            ):
        self.entity_description = entity_description
        self.request_attr = request_attr
        self.mapper = mapper
        self.id_extractor = id_extractor

    async def resolve(self, request):
        entity_id = self.id_extractor(request, self.request_attr)
        entity = await self.mapper.get(request.app['db'], entity_id)
        if entity is None:
            raise EntityNotFound(
                f'there is no {self.entity_description} with id {entity_id}',
                {'entity_id': entity_id}
            )
        request[self.entity_description] = entity


Contest = Entity('contest', 'contest_id', contest_mapper)
Task = Entity('task', 'task_id', task_mapper)
Team = Entity('team', 'team_id', team_mapper)
Member = Entity('member', 'member_id', team_member_mapper)
Invite = Entity('member', 'invite_id', team_member_mapper)
Solution = Entity('solution', 'solution_id', solution_mapper)
# Creator = Entity('creator', 'creator_id', mappers_container.user_mapper())
