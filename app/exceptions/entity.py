from exceptions import OlympException


class EntityException(OlympException):
    """Base exception for entity-related exceptions"""


class EntityNotFound(EntityException):
    """Raised in case entity isn't found"""
    HTTP_STATUS = 404
