import pathlib

from utils.docker.client import Client
from utils.docker.tag import create_tag

from services.docker.meta import PythonMeta


class PythonManager:

    @staticmethod
    def run_solution(solution, input_):
        solution_id = solution['id']
        solution_path = solution['path']

        compiler_tag = create_tag(PythonMeta.COMPILER_TAG, solution_id)
        runner_tag = create_tag(PythonMeta.RUNNER_TAG, solution_id)

        compiled_dir_path = str(pathlib.Path(solution_path) / 'code-compiled')

        client = Client.from_env()
        try:
            client.build(
                compiler_tag,
                PythonMeta.COMPILER_DOCKERFILE,
                solution_path
            )

            client.run(
                compiler_tag,
                volumes={compiled_dir_path: '/code-compiled'}
            )

            client.build(
                runner_tag,
                PythonMeta.RUNNER_DOCKERFILE,
                solution_path
            )

            result = client.run(
                runner_tag,
                command=PythonMeta.RUNNER_COMMAND.format(input_)
            )
            decoded_result = result.decode()
            print(decoded_result)
            return decoded_result
        finally:
            client.remove(compiler_tag)
            client.remove(runner_tag)
