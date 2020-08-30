from app.exceptions import OlympException


class EntityException(OlympException):
    """Base exception for entity-related exceptions"""


class EntityNotFound(EntityException):
    """Raised in case entity isn't found"""
    HTTP_STATUS = 404


class EntityCredentialsNotFound(EntityException):
    """Raised in case some credentials of entity isn't provided"""
