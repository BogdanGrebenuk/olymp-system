import abc


class CommandHandler(abc.ABC):
    """Abstract class for command handlers"""
    @abc.abstractmethod
    def handle(self, command):
        ...
