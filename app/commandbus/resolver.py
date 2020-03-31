from commandbus.commands.base_command import Command
from commandbus.command_handlers.base_command_handler import CommandHandler
from commandbus.exceptions import HandlerNotFoundException


class DefaultResolver:

    def __init__(
            self,
            bus_tag,
            *,
            command_base_cls=Command,
            command_handler_base_cls=CommandHandler
            ):
        self.bus_tag = bus_tag
        self.command_base_cls = command_base_cls
        self.command_handler_base_cls = command_handler_base_cls

    def resolve(self, command_map):
        command_handlers = {
            cls.__name__: cls
            for cls in self.command_handler_base_cls.__subclasses__()
        }
        for cls in self.command_base_cls.__subclasses__():
            command_name = cls.__name__
            handler_name = f"{command_name}Handler"
            handler = command_handlers.get(handler_name)
            if handler is None:
                raise HandlerNotFoundException(
                    f'there is no handler for {command_name} command'
                )
            if handler.supports(self.bus_tag):
                command_map[cls] = handler
