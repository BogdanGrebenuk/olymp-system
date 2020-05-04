import abc

from utils.docker.client import Client


class Worker(abc.ABC):

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


class Compiler(Worker):

    @abc.abstractmethod
    def build(self):
        ...

    @abc.abstractmethod
    def run(self):
        ...


class Runner(Worker):

    @abc.abstractmethod
    def build(self):
        ...

    @abc.abstractmethod
    def run(self, input_):
        ...
