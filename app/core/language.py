from enum import Enum


class Language(Enum):
    Python = 'python'


def get_supported_languages():
    return [i.value for i in Language]
