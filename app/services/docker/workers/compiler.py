import pathlib

from functools import partial

from services.docker.workers.interface import CompilerABC
from utils.docker.tag import create_tag
from utils.executor import cpu_bound


class DefaultCompiler(CompilerABC):

    def __init__(self, solution, meta):
        self.solution = solution
        self.meta = meta
        self._compiler_tag = None

    async def build(self):
        if self._compiler_tag is not None:
            raise ValueError(
                f"Compiler already manages image {self._compiler_tag}"
            )

        solution_id = self.solution['id']
        solution_path = self.solution['path']

        self._compiler_tag = create_tag(self.meta.COMPILER_TAG, solution_id)

        task = partial(
            self._build,

            self._compiler_tag,
            self.meta.COMPILER_DOCKERFILE,
            solution_path
        )

        return await cpu_bound(task)

    async def run(self):
        if self._compiler_tag is None:
            raise ValueError("Image isn't specified! Build an image!")

        solution_path = self.solution['path']  # TODO: implement entity!
        compiled_dir_path = str(pathlib.Path(solution_path) / 'code-compiled')

        task = partial(
            self._run,

            self._compiler_tag,
            volumes={compiled_dir_path: '/code-compiled'}
        )

        return await cpu_bound(task)

    async def remove(self):
        if self._compiler_tag is None:
            raise ValueError("Image isn't specified! Build an image!")
        task = partial(
            self._remove,

            self._compiler_tag
        )
        return await cpu_bound(task)
