import uuid
from datetime import datetime
from dateutil.tz import tzutc
from functools import partial

import app.utils.executor as executor
from app.commandbus.command_handlers.base_command_handler import CommandHandler
from app.commandbus.commands.solution import (
    CreateSolution,
    SaveSolutionCode,
    PrepareSolutionDir,
    VerifySolution
)
from app.common import CODE_DIR, ROOT_DIR
from app.db import (
    solution_mapper,
    task_mapper
)
from app.db.entities.solution import Solution
from app.services.codesaver import DefaultCodeManager
from app.services.docker.manager import DockerManager


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
        await self.bus.execute(
            SaveSolutionCode(
                solution_dir, command.language, command.code, command.pool
            )
        )
        solution = Solution(
            id=solution_id,
            task_id=command.task.id,
            path=str(solution_dir.relative_to(ROOT_DIR)),
            language=command.language,
            user_id=command.user.id,
            team_id=command.team.id,
            created_at=datetime.now(tzutc())
        )
        await solution_mapper.create(command.engine, solution)
        return solution


class PrepareSolutionDirHandler(CommandHandler):

    async def handle(self, command: PrepareSolutionDir):
        solution_dir = (
            CODE_DIR
            / command.contest_id
            / command.task_id
            / command.solution_id
        )

        task = partial(
            solution_dir.mkdir,

            parents=True,
            exist_ok=True
        )
        await executor.run(task, command.pool)
        return solution_dir


class SaveSolutionCodeHandler(CommandHandler):

    async def handle(self, command: SaveSolutionCode):
        code_manager = DefaultCodeManager.from_language(command.language)
        task = partial(
            code_manager.save,

            command.solution_dir_path,
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
        except Exception as e:  # todo: refactor
            return False
        finally:
            await docker_manager.close()
