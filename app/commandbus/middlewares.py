import abc

from commandbus.exceptions import HandlerNotFoundException


class Middleware(abc.ABC):

    @abc.abstractmethod
    async def __call__(self, command, next_):
        ...


class Resolver(Middleware):

    def __init__(self, command_handler_containers=None):
        if command_handler_containers is None:
            command_handler_containers = []
        self.command_handler_containers = command_handler_containers

    async def __call__(self, command, next):
        command_cls = type(command).__name__
        handler_name = f"{command_cls}Handler"
        for container in self.command_handler_containers:
            for _, provider in container.providers.items():
                if provider.cls.__name__ == handler_name:
                    return await provider().handle(command)
        raise HandlerNotFoundException(f'there is no handler for {command_cls}!')
