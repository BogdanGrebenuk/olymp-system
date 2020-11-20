from dependency_injector import containers, providers
from dependency_injector.ext import aiohttp as ext_aiohttp

from app.containers import application_container
from app.core.solution.controllers import (
    create_solution,
    get_solutions_for_contest,
    get_solutions_for_team,
    get_solution_code
)
from app.core.solution.services.code import CodeSaver, CodeLoader
from app.core.solution.services.creator import SolutionCreator
from app.core.solution.services.runner import SolutionRunner, RexTesterRunner
from app.core.solution.transformers import SolutionTransformer
from app.db import mappers_container
from app.utils.resolver import resolvers_container


transformers = containers.DynamicContainer()
transformers.solution_transformer = providers.Singleton(
    SolutionTransformer
)


services = containers.DynamicContainer()
services.code_saver = providers.Singleton(
    CodeSaver,
    code_config=application_container.config.code,
    process_executor=application_container.process_executor
)
services.code_loader = providers.Singleton(
    CodeLoader,
    code_config=application_container.config.code,
    process_executor=application_container.process_executor
)
services.solution_creator = providers.Singleton(
    SolutionCreator,
    code_saver=services.code_saver
)
services.rextester_runner = providers.Singleton(
    RexTesterRunner,
    code_loader=services.code_loader
)
services.solution_runner = providers.Singleton(
    SolutionRunner,
    code_runner=services.rextester_runner,
    task_io_mapper=mappers_container.task_io_mapper
)


controllers = containers.DynamicContainer()
controllers.create_solution = ext_aiohttp.View(
    create_solution,
    contest_resolver=resolvers_container.contest_resolver,
    task_resolver=resolvers_container.task_resolver,
    user_mapper=mappers_container.user_mapper,
    solution_mapper=mappers_container.solution_mapper,
    solution_transformer=transformers.solution_transformer,
    solution_creator=services.solution_creator,
    solution_runner=services.solution_runner
)
controllers.get_solutions_for_contest = ext_aiohttp.View(
    get_solutions_for_contest,
    # TODO: remove engine in future (domain_validator)
    engine=application_container.engine,
    contest_resolver=resolvers_container.contest_resolver,
    solution_mapper=mappers_container.solution_mapper,
    solution_transformer=transformers.solution_transformer
)
controllers.get_solutions_for_team = ext_aiohttp.View(
    get_solutions_for_team,
    # TODO: remove engine in future (domain_validator)
    engine=application_container.engine,
    contest_resolver=resolvers_container.contest_resolver,
    team_resolver=resolvers_container.team_resolver,
    solution_mapper=mappers_container.solution_mapper,
    solution_transformer=transformers.solution_transformer
)
controllers.get_solution_code = ext_aiohttp.View(
    get_solution_code,
    # TODO: remove engine in future (domain_validator)
    engine=application_container.engine,
    contest_resolver=resolvers_container.contest_resolver,
    solution_resolver=resolvers_container.solution_resolver,
    team_mapper=mappers_container.team_mapper,
    code_loader=services.code_loader
)
