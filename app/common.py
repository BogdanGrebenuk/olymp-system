import pathlib
from enum import Enum


ROOT_DIR = pathlib.Path(__file__).parent.resolve()
CODE_DIR = (pathlib.Path(ROOT_DIR).parent / 'code').resolve()


class Language(Enum):
    Python = 'python'


def get_supported_languages():
    return [i.value for i in Language]


if __name__ == '__main__':
    print(ROOT_DIR)
