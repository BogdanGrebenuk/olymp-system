from commandbus.commands.base_command import Command
from commandbus.command_handlers.base_command_handler import CommandHandler
from commandbus.exceptions import HandlerNotFoundException


class DefaultResolver:

    def resolve(self, command_map):
        command_handlers = {
            cls.__name__: cls
            for cls in CommandHandler.__subclasses__()
        }
        for cls in Command.__subclasses__():
            command_name = cls.__name__
            handler_name = f"{command_name}Handler"
            handler = command_handlers.get(handler_name)
            if handler is None:
                raise HandlerNotFoundException(
                    f'there is no handler for {command_name} command'
                )
            command_map[cls] = handler


if __name__ == '__main__':
    r = DefaultResolver()
    map_ = {}
    r.resolve(map_)
    print(map_)
