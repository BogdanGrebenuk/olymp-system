from dataclasses import dataclass

from aiohttp.web import Request
from dependency_injector import containers, providers

from app.db import mappers_container
from app.db.common import Mapper
from app.exceptions import OlympException
from app.exceptions.entity import EntityNotFound


@dataclass
class EntityToResolve:
    slug: str
    name: str


class Resolver:

    def __init__(
            self,
            entity_to_resolve: EntityToResolve,
            mapper: Mapper
            ):
        self.entity_to_resolve = entity_to_resolve
        self.mapper = mapper

    async def resolve(self, request: Request):
        entity_id = self.extract_id(request)
        if entity_id is None:
            raise OlympException(
                f"Value for {entity_id} hasn't found in request!",
                {
                    'name': self.entity_to_resolve.name,
                    'entity_id': entity_id
                }
            )
        entity = await self.mapper.get(entity_id)
        if entity is None:
            raise EntityNotFound(
                f'There is no {self.entity_to_resolve.name} with id {entity_id}',
                {
                    'name': self.entity_to_resolve.name,
                    'entity_id': entity_id
                }
            )
        return entity

    def extract_id(self, request):
        body = request.get('body', {})
        params = request.get('params', {})
        vars = request.get('vars', {})
        for source in body, params, vars:
            id = source.get(self.entity_to_resolve.slug)
            if id is not None:
                return id


resolvers_container = containers.DynamicContainer()
resolvers_container.contest_resolver = providers.Singleton(
    Resolver,
    entity_to_resolve=EntityToResolve('contest_id', 'contest'),
    mapper=mappers_container.contest_mapper
)
resolvers_container.task_resolver = providers.Singleton(
    Resolver,
    entity_to_resolve=EntityToResolve('task_id', 'task'),
    mapper=mappers_container.task_mapper
)
resolvers_container.team_resolver = providers.Singleton(
    Resolver,
    entity_to_resolve=EntityToResolve('team_id', 'team'),
    mapper=mappers_container.team_mapper
)
resolvers_container.member_resolver = providers.Singleton(
    Resolver,
    entity_to_resolve=EntityToResolve('member_id', 'member'),
    mapper=mappers_container.team_member_mapper
)
resolvers_container.invite_resolver = providers.Singleton(
    Resolver,
    entity_to_resolve=EntityToResolve('invite_id', 'invite'),
    mapper=mappers_container.team_member_mapper
)
resolvers_container.solution_resolver = providers.Singleton(
    Resolver,
    entity_to_resolve=EntityToResolve('solution_id', 'solution'),
    mapper=mappers_container.team_member_mapper
)
resolvers_container.creator_resolver = providers.Singleton(
    Resolver,
    entity_to_resolve=EntityToResolve('creator_id', 'user'),
    mapper=mappers_container.user_mapper
)
