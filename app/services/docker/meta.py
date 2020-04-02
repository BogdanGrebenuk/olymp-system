class PythonMeta:
    COMPILER_TAG = 'python-compiler'
    # TODO: remove path to config?
    COMPILER_DOCKERFILE = (
        '/home/bohdan/projects/olymp-dev/images/python/DockerfileCompiler'
    )
    RUNNER_TAG = 'python-runner'
    RUNNER_DOCKERFILE = (
        '/home/bohdan/projects/olymp-dev/images/python/DockerfileRunner'
    )
    RUNNER_COMMAND = "sh -c 'echo {} | python /code-compiled/main.pyc'"