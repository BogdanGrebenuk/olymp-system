import dataclasses


def get_language_meta(language: str, docker_meta: dict):
    meta = docker_meta.get(language)
    if meta is None:
        raise ValueError(f"docker-meta isn't specified for '{language}'")
    return DockerMeta(language=language, **meta)


@dataclasses.dataclass
class DockerMeta:
    language: str
    compiler_tag: str
    compiler_dockerfile: str
    runner_tag: str
    runner_dockerfile: str
    runner_command: str


#
#
#     # if language == 'python':
#     #     return PythonMeta
#     # ...
#     # raise ValueError(f"there is no meta data for {language}")
#
#
# class PythonMeta:
#     COMPILER_TAG = 'python-compiler'
#     # TODO: remove path to config?
#     COMPILER_DOCKERFILE = (
#         '/home/bohdan/projects/olymp-dev/images/python/DockerfileCompiler'
#     )
#     RUNNER_TAG = 'python-runner'
#     RUNNER_DOCKERFILE = (
#         '/home/bohdan/projects/olymp-dev/images/python/DockerfileRunner'
#     )
#     RUNNER_COMMAND = "sh -c 'echo {} | python /code-compiled/main.pyc'"
