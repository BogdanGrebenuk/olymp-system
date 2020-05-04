from concurrent.futures import Executor
from functools import partial

import utils.executor as executor
from db.entities.solution import Solution
from services.docker.meta import DockerMeta
from services.docker.workers.interface import Runner
from utils.docker.tag import create_tag


class DefaultRunner(Runner):

    def __init__(self, solution: Solution, meta: DockerMeta, pool: Executor):
        self.solution = solution
        self.meta = meta
        self.pool = pool
        self._runner_tag = None

    async def build(self):
        if self._runner_tag is not None:
            raise ValueError(
                f"Compiler already manages image {self._runner_tag}"
            )

        solution_id = self.solution.id
        solution_path = self.solution.path

        self._runner_tag = create_tag(self.meta.runner_tag, solution_id)

        task = partial(
            self._build,

            self._runner_tag,
            self.meta.runner_dockerfile,
            solution_path
        )

        return await executor.run(task, self.pool)

    async def run(self, input_):
        if self._runner_tag is None:
            raise ValueError("Image isn't specified! Build an image!")

        task = partial(
            self._run,

            self._runner_tag,
            command=self.meta.runner_command.format(input_)
        )

        result = await executor.run(task, self.pool)
        return result.decode()

    async def remove(self):
        if self._runner_tag is None:
            raise ValueError("Image isn't specified! Build an image!")
        task = partial(self._remove, self._runner_tag)
        return await executor.run(task, self.pool)
