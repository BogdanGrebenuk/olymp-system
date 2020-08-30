from concurrent.futures import Executor

from docker.errors import APIError

from app.db.entities.solution import Solution
from app.services.docker.meta import get_language_meta
from app.services.docker.workers import DefaultCompiler, DefaultRunner


class DockerManager:

    def __init__(self, solution: Solution, compiler_manager, runner_manager):
        self.solution = solution
        self.compiler_manager = compiler_manager
        self.runner_manager = runner_manager

    @classmethod
    def default(cls, solution: Solution, pool: Executor, docker_meta: dict):
        meta = get_language_meta(solution.language, docker_meta)
        compiler_manager = DefaultCompiler(solution, meta, pool)
        runner_manager = DefaultRunner(solution, meta, pool)
        return cls(solution, compiler_manager, runner_manager)

    async def __aenter__(self):
        await self.prepare()

    async def __aexit__(self, *exc_info):
        await self.close()

    async def prepare(self):  # will prepare images for running solution
        await self.compiler_manager.build()
        await self.compiler_manager.run()
        await self.runner_manager.build()

    async def run(self, input_) -> str:  # will run runner image
        return await self.runner_manager.run(input_)

    async def close(self):
        errors = []
        try:
            await self.compiler_manager.remove()
        except APIError as e:
            errors.append(e)
        try:
            await self.runner_manager.remove()
        except APIError as e:
            errors.append(e)
        if errors:
            raise Exception(';'.join(map(str, errors)))  # TODO: implement exception
