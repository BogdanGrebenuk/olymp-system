from dependency_injector import providers, containers

import app.db.mappers.contest as contest_mapper
import app.db.mappers.solution as solution_mapper
import app.db.mappers.task as task_mapper
import app.db.mappers.task_io as task_io_mapper
import app.db.models as models
from app.containers import application_container
from app.db.mappers.team import TeamMapper
from app.db.mappers.team_member import TeamMemberMapper
from app.db.mappers.user import UserMapper
from app.core.team.domain.entity import Team as TeamEntity
from app.db.entities import TeamMember as TeamMemberEntity
from app.core.user.domain.entity import User as UserEntity


mappers_container = containers.DynamicContainer()
mappers_container.contest_mapper = providers.Object(contest_mapper)
mappers_container.solution_mapper = providers.Object(solution_mapper)
mappers_container.task_mapper = providers.Object(task_mapper)
mappers_container.task_io_mapper = providers.Object(task_io_mapper)
mappers_container.team_mapper = providers.Singleton(
    TeamMapper,
    engine=application_container.engine,
    model=models.Team,
    entity_cls=TeamEntity
)
mappers_container.team_member_mapper = providers.Singleton(
    TeamMemberMapper,
    team_mapper=mappers_container.team_mapper,
    engine=application_container.engine,
    model=models.TeamMember,
    entity_cls=TeamMemberEntity
)
mappers_container.user_mapper = providers.Singleton(
    UserMapper,
    engine=application_container.engine,
    model=models.User,
    entity_cls=UserEntity
)
