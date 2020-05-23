import pathlib
from concurrent.futures import Executor

from functools import partial

import utils.executor as executor
from db.entities.solution import Solution
from services.docker.meta import DockerMeta
from services.docker.workers.interface import Compiler
from utils.docker.tag import create_tag


class DefaultCompiler(Compiler):

    def __init__(self, solution: Solution, meta: DockerMeta, pool: Executor):
        self.solution = solution
        self.meta = meta
        self.pool = pool
        self._compiler_tag = None

    async def build(self):
        if self._compiler_tag is not None:
            raise ValueError(
                f"Compiler already manages image {self._compiler_tag}"
            )

        solution_id = self.solution.id
        solution_path = self.solution.get_full_path()

        self._compiler_tag = create_tag(self.meta.compiler_tag, solution_id)

        task = partial(
            self._build,

            self._compiler_tag,
            self.meta.compiler_dockerfile,
            solution_path
        )

        return await executor.run(task, self.pool)

    async def run(self):
        if self._compiler_tag is None:
            raise ValueError("Image isn't specified! Build an image!")

        solution_path = self.solution.get_full_path()
        compiled_dir_path = str(pathlib.Path(solution_path) / 'code-compiled')

        task = partial(
            self._run,

            self._compiler_tag,
            volumes={compiled_dir_path: '/code-compiled'}
        )

        return await executor.run(task, self.pool)

    async def remove(self):
        if self._compiler_tag is None:
            raise ValueError("Image isn't specified! Build an image!")
        task = partial(
            self._remove,

            self._compiler_tag
        )
        return await executor.run(task, self.pool)
