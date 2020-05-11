import pathlib
import uuid
from functools import partial

import utils.executor as executor
from commandbus.command_handlers.base_command_handler import CommandHandler
from commandbus.commands.solution import (
    CreateSolution,
    SaveSolutionCode,
    PrepareSolutionDir,
    VerifySolution
)
from common import CODE_DIR
from db import (
    solution_mapper,
    task_mapper
)
from db.entities.solution import Solution
from services.codesaver import manager
from services.docker.manager import DockerManager


class CreateSolutionHandler(CommandHandler):

    async def handle(self, command: CreateSolution):
        solution_id = str(uuid.uuid4())
        solution_dir = await self.bus.execute(
            PrepareSolutionDir(
                command.contest.id,
                command.task.id,
                solution_id,
                command.pool
            )
        )
        solution_dir_path = str(solution_dir.resolve())
        await self.bus.execute(
            SaveSolutionCode(
                solution_dir_path, command.language, command.code, command.pool
            )
        )
        solution = Solution(
            solution_id, command.task.id, solution_dir_path, command.language
        )
        await solution_mapper.create(command.engine, solution)
        return solution


class PrepareSolutionDirHandler(CommandHandler):

    async def handle(self, command: PrepareSolutionDir):
        code_dir = CODE_DIR
        contest_dir = code_dir / command.contest_id
        task_dir = contest_dir / command.task_id
        solution_dir = task_dir / command.solution_id

        task = partial(
            solution_dir.mkdir,

            parents=True,
            exist_ok=True
        )
        await executor.run(task, command.pool)
        return solution_dir


class SaveSolutionCodeHandler(CommandHandler):

    async def handle(self, command: SaveSolutionCode):
        saver = manager.get_saver(command.language)
        task = partial(
            saver,

            pathlib.Path(command.solution_dir_path),
            command.code
        )
        return await executor.run(task, command.pool)


class VerifySolutionHandler(CommandHandler):

    async def handle(self, command: VerifySolution):
        solution = command.solution
        pool = command.pool
        docker_meta = command.docker_meta
        docker_manager = DockerManager.default(solution, pool, docker_meta)
        # TODO: introduce execution logic (for example parallel verification)
        try:
            await docker_manager.prepare()
            task_ios = await task_mapper.get_task_ios(command.engine, command.task)
            for task_io in task_ios:
                answer = await docker_manager.run(task_io.input)
                answer = answer.rstrip()
                if answer != task_io.output:
                    return False
            return True
        finally:
            await docker_manager.close()
