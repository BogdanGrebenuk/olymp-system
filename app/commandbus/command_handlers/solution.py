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
from services.codesaver import manager
from services.docker import get_docker_manager
# from utils.docker import LANGUAGE_INFO
# from utils.docker.client import Client
from utils.executor import cpu_bound
from utils.filesystem import create_dir_chain


class CreateSolutionHandler(CommandHandler):

    async def handle(self, command: CreateSolution):
        solution_id = str(uuid.uuid4())
        solution_dir = await self.bus.execute(
            PrepareSolutionDir(
                command.user_id,
                command.contest_id,
                command.task_id,
                solution_id
            )
        )
        solution_dir_path = str(solution_dir.resolve())
        await self.bus.execute(
            SaveSolutionCode(solution_dir_path, command.language, command.code)
        )
        solution = {  # TODO: create entity
            'id': solution_id,
            'path': solution_dir_path,
            'language': command.language,
        }
        return solution


class PrepareSolutionDirHandler(CommandHandler):

    async def handle(self, command: PrepareSolutionDir):
        code_dir = pathlib.Path(__file__).parent.parent.parent.parent / 'code'

        user_dir = code_dir / str(command.user_id)
        contest_dir = user_dir / str(command.contest_id)
        task_dir = contest_dir / str(command.task_id)
        solution_dir = task_dir / command.solution_id

        task = partial(
            create_dir_chain,

            user_dir,
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
        solution_id = solution['id']  # TODO: create entity!
        solution_dir = pathlib.Path(solution['path'])
        language = solution['language']

        docker_manager = get_docker_manager(language)

        for input_, output in [('1', '1'), ('2', '4'), ('3', '9')]:  # TODO: take data from task
            task = partial(
                docker_manager.run_solution,

                solution,
                input_
            )
            answer = await cpu_bound(task)
            if answer != output:
                ...



        # result = await docker_manager.verify(solution)

        # docker_manager.build_compiler(solution)
        # docker_manager.build_runner(solution)
        #
        # docker_manager.run_compiler()
        # docker_manager.run_runner()


        docker_info = LANGUAGE_INFO[solution['language']]
        # TODO: remove dicts and introduce classes
        compiler_tag = f"{docker_info['compiler']['tag']}:{solution_id}"
        compiler_dockerfile = docker_info['compiler']['dockerfile']

        runner_tag = f"{docker_info['runner']['tag']}:{solution_id}"
        runner_dockerfile = docker_info['runner']['dockerfile']

        compiled_dir_path = str((solution_dir / 'code-compiled').resolve())

        client = Client.from_env()
        try:
            client.build(compiler_tag, compiler_dockerfile, solution['path'])
            client.run(
                compiler_tag,
                volumes={compiled_dir_path: '/code-compiled'}
            )
            client.build(runner_tag, runner_dockerfile, solution['path'])
            print(client.run(runner_tag))
            return True  # TODO: implement!
        finally:
            client.remove(compiler_tag)
            client.remove(runner_tag)



