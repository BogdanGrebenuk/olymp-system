from functools import partial

from utils.executor import cpu_bound
from utils.docker.client import Client
from utils.docker.tag import create_tag
from services.docker.workers.interface import RunnerABC


class DefaultRunner(RunnerABC):

    def __init__(self, solution, meta):
        self.solution = solution
        self.meta = meta
        self._runner_tag = None

    async def build(self):
        if self._runner_tag is not None:
            raise ValueError(
                f"Compiler already manages image {self._runner_tag}"
            )

        solution_id = self.solution['id']
        solution_path = self.solution['path']

        self._runner_tag = create_tag(self.meta.RUNNER_TAG, solution_id)

        task = partial(
            self._build,

            self._runner_tag,
            self.meta.RUNNER_DOCKERFILE,
            solution_path
        )

        return await cpu_bound(task)

    async def run(self, input_):
        if self._runner_tag is None:
            raise ValueError("Image isn't specified! Build an image!")

        task = partial(
            self._run,

            self._runner_tag,
            command=self.meta.RUNNER_COMMAND.format(input_)
        )

        result = await cpu_bound(task)
        return result.decode()

    async def remove(self):
        if self._runner_tag is None:
            raise ValueError("Image isn't specified! Build an image!")
        task = partial(self._remove, self._runner_tag)
        return await cpu_bound(task)
