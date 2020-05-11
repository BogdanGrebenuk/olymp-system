from exceptions import OlympException


class RoleException(OlympException):
    """Base exception for role-related exceptions"""


class PermissionException(RoleException):
    """Raised in case lack of permissions"""
    HTTP_STATUS = 403
