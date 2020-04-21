from enum import Enum


def get_supported_languages():
    return [i.value for i in Language]


class Language(Enum):
    Python = 'python'
