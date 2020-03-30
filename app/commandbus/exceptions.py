class CommandBusException(Exception):
    """Base package exception"""


class HandlerNotFoundException(CommandBusException):
    """Exception for cases when commands has no handler"""
