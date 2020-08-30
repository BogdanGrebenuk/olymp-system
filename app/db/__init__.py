from dependency_injector import providers, containers

import db.procedures.contest as contest_mapper
import db.procedures.solution as solution_mapper
import db.procedures.task as task_mapper
import db.procedures.task_io as task_io_mapper
import db.procedures.team as team_mapper
import db.procedures.team_member as team_member_mapper
import db.procedures.user as user_mapper


mappers_container = containers.DynamicContainer()
mappers_container.contest_mapper = providers.Object(contest_mapper)
mappers_container.solution_mapper = providers.Object(solution_mapper)
mappers_container.task_mapper = providers.Object(task_mapper)
mappers_container.task_io_mapper = providers.Object(task_io_mapper)
mappers_container.team_mapper = providers.Object(team_mapper)
mappers_container.team_member_mapper = providers.Object(team_member_mapper)
mappers_container.user_mapper = providers.Object(user_mapper)
