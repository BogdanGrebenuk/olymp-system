from services.docker.meta import get_language_meta
from services.docker.workers import DefaultCompiler, DefaultRunner


class DockerManager:

    def __init__(self, solution, compiler_manager, runner_manager):
        self.solution = solution
        self.compiler_manager = compiler_manager
        self.runner_manager = runner_manager

    @classmethod
    def from_solution(cls, solution):
        meta = get_language_meta(solution['language'])  # TODO: implement entity
        compiler_manager = DefaultCompiler(solution, meta)
        runner_manager = DefaultRunner(solution, meta)
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
        await self.compiler_manager.remove()
        await self.runner_manager.remove()
