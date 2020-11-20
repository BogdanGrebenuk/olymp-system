from pathlib import Path

from app.common import ROOT_DIR
from app.core.solution.domain.entity import Solution
from app.utils.executor import Executor
from app.utils.filesystem import save_file, load_file


class CodeSaver:

    def __init__(
            self,
            code_config,
            process_executor: Executor,
            ):
        self.code_config = code_config
        self.executor = process_executor

    async def save_code(self, path: Path, language: str, code: str):
        file_name = self.code_config.get(language)
        if file_name is None:
            raise ValueError(
                f"Code configuration file doesn't contain information"
                f"about '{language}' language"
            )
        destination_dir = path / 'code'
        await self.executor.run(
            destination_dir.mkdir,
            parents=True,
            exist_ok=True
        )
        await self.executor.run(
            save_file,
            str(destination_dir / file_name),
            code
        )


class CodeLoader:

    def __init__(
            self,
            code_config,
            process_executor: Executor
            ):
        self.code_config = code_config
        self.executor = process_executor

    async def load_code(self, solution: Solution):
        file_name = self.code_config.get(solution.language)
        if file_name is None:
            raise ValueError(
                f"Code configuration file doesn't contain information"
                f"about '{solution.language}' language"
            )
        destination = ROOT_DIR / 'code' / file_name
        return await self.executor.run(load_file, str(destination))
