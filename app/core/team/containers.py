import dependency_injector.containers as containers
import dependency_injector.providers as providers
from dependency_injector.ext import aiohttp as ext_aiohttp

from app.containers import application_container
from app.core.team.command_handlers import CreateTeamHandler
from app.core.team.controllers import (
    create_team,
    get_team,
    get_teams_for_contest,
    get_teams_for_contest_and_creator
)

from app.core.team.transformers import TeamTransformer
from app.db import mappers_container
from app.utils.resolver import resolvers_container


transformers = containers.DynamicContainer()
transformers.team_transformer = providers.Singleton(
    TeamTransformer
)

controllers = containers.DynamicContainer()
controllers.create_team = ext_aiohttp.View(
    create_team,
    bus=application_container.bus,
    contest_resolver=resolvers_container.contest_resolver,
    team_mapper=mappers_container.team_mapper
)
controllers.get_team = ext_aiohttp.View(
    get_team,
    team_resolver=resolvers_container.team_resolver,
    contest_resolver=resolvers_container.contest_resolver,
    team_transformer=transformers.team_transformer
)
controllers.get_teams_for_contest = ext_aiohttp.View(
    get_teams_for_contest,
    contest_resolver=resolvers_container.contest_resolver,
    user_mapper=mappers_container.user_mapper,
    team_transformer=transformers.team_transformer
)
controllers.get_teams_for_contest_and_creator = ext_aiohttp.View(
    get_teams_for_contest_and_creator,
    contest_resolver=resolvers_container.contest_resolver,
    user_mapper=mappers_container.user_mapper,
    team_transformer=transformers.team_transformer
)

command_handlers = containers.DynamicContainer()
command_handlers.create_team = providers.Singleton(
    CreateTeamHandler,
    team_mapper=mappers_container.team_mapper
)
