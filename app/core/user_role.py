from enum import Enum


class UserRole(Enum):
    PARTICIPANT = 'participant'
    TRAINER = 'trainer'
    ORGANIZER = 'organizer'


def get_roles():
    return [i.value for i in UserRole]
