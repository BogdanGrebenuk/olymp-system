from dependency_injector import providers, containers

import app.db.mappers.contest as contest_mapper
import app.db.mappers.task as task_mapper
import app.db.mappers.task_io as task_io_mapper
import app.db.mappers.team as team_mapper
import app.db.mappers.team_member as team_member_mapper
import app.db.models as models
from app.containers import application_container
from app.core.solution.domain.entity import Solution as SolutionEntity
from app.core.user.domain.entity import User as UserEntity
from app.db.mappers.contest import ContestMapper
from app.db.mappers.solution import SolutionMapper
from app.db.mappers.user import UserMapper


mappers_container = containers.DynamicContainer()
mappers_container.contest_mapper = providers.Object(contest_mapper)
mappers_container.solution_mapper = providers.Singleton(
    SolutionMapper,
    engine=application_container.engine,
    model=models.Solution,
    entity_cls=SolutionEntity
)
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
