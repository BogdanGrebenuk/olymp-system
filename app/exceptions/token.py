from exceptions import OlympException


class TokenException(OlympException):
    """Base exception for token-related exceptions"""


class TokenHeaderNotFound(TokenException):
    """Raised when authorization header isn't presented in request"""


class InvalidTokenHeaderFormat(TokenException):
    """Raised when token header has wrong format"""


class InvalidTokenContent(TokenException):
    """Raised when token contains invalid information

    For example, token contains id of non-existent user
    """
