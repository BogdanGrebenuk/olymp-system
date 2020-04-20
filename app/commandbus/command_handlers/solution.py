import pathlib
import uuid
from functools import partial

from commandbus.command_handlers.base_command_handler import CommandHandler
from commandbus.commands.solution import (
    CreateSolution,
    SaveSolutionCode,
    PrepareSolutionDir,
    VerifySolution
)
from db.entities.solution import Solution
from db.procedures.solution import create_solution
from db.procedures.task import get_task_ios
from services.codesaver import manager
from services.docker.manager import DockerManager
from utils.executor import cpu_bound
from utils.filesystem import create_dir_chain


class CreateSolutionHandler(CommandHandler):

    async def handle(self, command: CreateSolution):
        solution_id = str(uuid.uuid4())
        solution_dir = await self.bus.execute(
            PrepareSolutionDir(
                command.contest.id,
                command.task.id,
                solution_id
            )
        )
        solution_dir_path = str(solution_dir.resolve())
        await self.bus.execute(
            SaveSolutionCode(solution_dir_path, command.language, command.code)
        )
        solution = Solution(
            solution_id, command.task.id, solution_dir_path, command.language
        )
        await create_solution(command.engine, solution)
        return solution


class PrepareSolutionDirHandler(CommandHandler):

    async def handle(self, command: PrepareSolutionDir):
        # TODO: how to get root dir of project?
        code_dir = pathlib.Path(__file__).parent.parent.parent.parent / 'code'
        # TODO: introduce user folder
        contest_dir = code_dir / command.contest_id
        task_dir = contest_dir / command.task_id
        solution_dir = task_dir / command.solution_id

        task = partial(
            create_dir_chain,

            contest_dir,
            task_dir,
            solution_dir
        )
        await cpu_bound(task)
        return solution_dir


class SaveSolutionCodeHandler(CommandHandler):

    async def handle(self, command: SaveSolutionCode):
        saver = manager.get_saver(command.language)
        task = partial(
            saver,

            pathlib.Path(command.solution_dir_path),
            command.code
        )
        return await cpu_bound(task)


class VerifySolutionHandler(CommandHandler):

    async def handle(self, command: VerifySolution):
        solution = command.solution
        docker_manager = DockerManager.from_solution(solution)
        # TODO: introduce execution logic (for example parallel verification)
        try:
            await docker_manager.prepare()
            task_ios = await get_task_ios(command.engine, command.task)
            for task_io in task_ios:
                answer = await docker_manager.run(task_io.input)
                answer = answer.rstrip()
                if answer != task_io.output:
                    return False
            return True
        finally:
            await docker_manager.close()
