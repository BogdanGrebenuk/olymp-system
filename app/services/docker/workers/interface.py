import abc

from utils.docker.client import Client


class WorkerABC(abc.ABC):

    @staticmethod
    def _build(*args, **kwargs):
        client = Client.from_env()
        client.build(*args, **kwargs)

    @staticmethod
    def _run(*args, **kwargs):
        client = Client.from_env()
        return client.run(*args, **kwargs)

    @staticmethod
    def _remove(*args, **kwargs):
        client = Client.from_env()
        client.remove(*args, **kwargs)


class CompilerABC(WorkerABC):

    @abc.abstractmethod
    def build(self):
        ...

    @abc.abstractmethod
    def run(self):
        ...


class RunnerABC(WorkerABC):

    @abc.abstractmethod
    def build(self):
        ...

    @abc.abstractmethod
    def run(self, input_):
        ...
