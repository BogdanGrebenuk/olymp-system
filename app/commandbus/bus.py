from commandbus.resolver import DefaultResolver
from commandbus.exceptions import HandlerNotFoundException


class Bus:

    def __init__(self, tag, *, resolver=None, command_map=None):
        self.tag = tag
        if command_map is None:
            command_map = {}
        if resolver is None:
            resolver = DefaultResolver(self.tag)
        resolver.resolve(command_map)
        self._command_map = command_map

    async def execute(self, command):
        command_class = command.__class__
        handler = self._command_map.get(command_class)
        if handler is None:
            raise HandlerNotFoundException(
                f'there is no handler for {command_class.__name__}!'
            )
        return await handler().handle(command)


if __name__ == '__main__':
    import asyncio
    from commandbus.commands.solution import VerifySolution
    bus = Bus()
    asyncio.run(bus.execute(VerifySolution('')))
