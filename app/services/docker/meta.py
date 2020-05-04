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
