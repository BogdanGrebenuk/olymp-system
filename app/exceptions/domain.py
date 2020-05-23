from exceptions import OlympException


class DomainException(OlympException):
    """Base exception for domain-related exceptions"""


class LanguageNotFound(DomainException):
    """Raised when requested language isn't presented in system"""
