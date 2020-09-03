from app.exceptions import OlympException


class MapperException(OlympException):
    """Base exception for mapper-related exceptions"""


class NotSingleResult(MapperException):
    """Raised in case multiple possible values while fetching single object"""
