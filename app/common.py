import pathlib
from enum import Enum


ROOT_DIR = pathlib.Path(__file__).parent.parent
CODE_DIR = pathlib.Path(ROOT_DIR) / 'code'
PUBLIC_DIR = pathlib.Path(ROOT_DIR) / 'public'


class Language(Enum):
    Python = 'python'


class UserRole(Enum):
    PARTICIPANT = 'participant'
    TRAINER = 'trainer'
    ORGANIZER = 'organizer'


def get_supported_languages():
    return [i.value for i in Language]


def get_roles():
    return [i.value() for i in UserRole]


if __name__ == '__main__':
    print(ROOT_DIR)
    print(PUBLIC_DIR)
