from services.docker.python import PythonManager


def get_docker_manager(language):
    if language == 'python':  # TODO: introduce some enum
        return PythonManager()
    ...
    raise ValueError(f'there is no docker manager for {language}!')
