from commandbus.middlewares import Resolver


def _create_closure(middleware, execution_chain):
    async def handle_command(command):
        return await middleware(command, execution_chain)
    return handle_command


def _build_chain(middlewares):
    execution_chain = lambda *args: None

    for middleware in reversed(middlewares):
        execution_chain = _create_closure(middleware, execution_chain)

    return execution_chain


class Bus:

    def __init__(self, middlewares):
        self._middlewares = middlewares
        self._chain = _build_chain(middlewares)

    async def execute(self, command):
        return await self._chain(command)

    @classmethod
    def from_default(cls):
        return Bus([Resolver()])

