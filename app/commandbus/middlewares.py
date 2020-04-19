from commandbus.command_handlers.base_command_handler import CommandHandler
from commandbus.exceptions import HandlerNotFoundException


class Resolver:

    def __init__(self, command_handler_base=CommandHandler):
        self.command_handler_base = command_handler_base

    async def __call__(self, command, next_):
        command_cls = type(command).__name__
        handler_name = f"{command_cls}Handler"
        for cls in self.command_handler_base.__subclasses__():
            if cls.__name__ == handler_name:
                return await cls().handle(command)
        raise HandlerNotFoundException(f'there is no handler for {command_cls}!')
