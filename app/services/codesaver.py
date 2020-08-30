import abc
from os import PathLike
from pathlib import Path

from app.db.entities import Solution
from app.core.language import Language
from app.exceptions.domain import LanguageNotFound


class CodeManager(abc.ABC):

    @abc.abstractmethod
    def save(self, path: PathLike, code: str):
        ...

    @abc.abstractmethod
    def load(self, path: PathLike):
        ...


class DefaultCodeManager(CodeManager):

    def __init__(self, file_name: str):
        self.file_name = file_name

    def get_file_path(self, path):
        code_dir = path / 'code'
        code_dir.mkdir()
        file_path = str(code_dir / self.file_name)
        return file_path

    def save(self, path: Path, code: str):
        file_path = self.get_file_path(path)
        with open(file_path, 'w') as file:
            file.write(code)

    def load(self, path: Path) -> str:
        path = path / 'code' / self.file_name
        with open(str(path)) as file:
            return file.read()

    @classmethod
    def from_language(cls, language):
        if language == Language.Python.value:
            return cls('main.py')
        raise LanguageNotFound(
            "this language isn't supported!",
            {'language': language}
        )


def get_code(solution: Solution) -> str:
    code_manager = DefaultCodeManager.from_language(solution.language)
    return code_manager.load(Path(solution.get_full_path()))
