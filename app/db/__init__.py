from dependency_injector import providers, containers

import app.db.mappers.solution as solution_mapper
import app.db.mappers.task as task_mapper
import app.db.mappers.task_io as task_io_mapper
import app.db.mappers.team as team_mapper
import app.db.mappers.team_member as team_member_mapper
import app.db.models as models
from app.containers import application_container
from app.db.mappers.user import UserMapper
from app.db.mappers.contest import ContestMapper
from core.user.domain.entity import User as UserEntity
from core.contest.domain.entity import Contest as ContestEntity

mappers_container = containers.DynamicContainer()
mappers_container.contest_mapper = providers.Singleton(
    ContestMapper,
    engine=application_container.engine,
    model=models.Contest,
    entity_cls=ContestEntity
)
mappers_container.solution_mapper = providers.Object(solution_mapper)
mappers_container.task_mapper = providers.Object(task_mapper)
mappers_container.task_io_mapper = providers.Object(task_io_mapper)
mappers_container.team_mapper = providers.Object(team_mapper)
mappers_container.team_member_mapper = providers.Object(team_member_mapper)
mappers_container.user_mapper = providers.Singleton(
    UserMapper,
    engine=application_container.engine,
    model=models.User,
    entity_cls=UserEntity
)
