from dataclasses import dataclass
from typing import List

import aiohttp

from core.solution.services.code import CodeLoader


@dataclass
class Stats:
    absolute_running_time: float
    cpu_time: float
    memory_peak: int


@dataclass
class CodeRunnerResult:
    warnings: str
    errors: str
    result: str
    stats: Stats


@dataclass
class SolutionRunnerResult:
    is_passed: bool
    code_runner_results: List[CodeRunnerResult]


class SolutionRunner:

    def __init__(
            self,
            code_runner,
            task_io_mapper
            ):
        self.code_runner = code_runner
        self.task_io_mapper = task_io_mapper

    async def run(self, solution):
        task_ios = await self.task_io_mapper.find_by(
            task_id=solution.task_id
        )
        code_runner_results = []
        for task_io in task_ios:
            code_runner_result = await self.code_runner.run(solution, task_io)
            code_runner_results.append(code_runner_result)
            if code_runner_result.output != task_io.output:
                return SolutionRunnerResult(
                    is_passed=False, code_runner_results=code_runner_results
                )
        return SolutionRunnerResult(
            is_passed=True,
            code_runner_results=code_runner_results
        )


class RexTesterRunner:

    LANGUAGE_ID_MAP = {
        'python': '5'
    }

    def __init__(self, code_loader: CodeLoader):
        self.code_loader = code_loader

    async def run(self, solution, task_io):
        data = await self.get_data_from_response(solution, task_io)
        stats = self.prepare_stats(data["Stats"])
        code_runner_result = CodeRunnerResult(
            warnings=data["Warnings"],
            errors=data["Errors"],
            result=data["Result"],
            stats=stats,
        )
        return code_runner_result

    async def get_data_from_response(self, solution, task_io):
        language_id = self.LANGUAGE_ID_MAP.get(solution.language)
        if language_id is None:
            raise ValueError("Runner doesn't support specified language!")
        async with aiohttp.ClientSession() as session:
            request = session.post(
                'https://rextester.com/rundotnet/api',
                json={
                    "LanguageChoice": language_id,
                    "Program": await self.code_loader.load_code(solution),
                    "Input": task_io.input,
                    "CompilerArgs": ""
                }
            )
            async with request as response:
                data = await response.json()
        return data

    def prepare_stats(self, raw_stats):
        temp_stats = []
        for part in raw_stats.split(',')[:-2]:
            _, payload = part.split(': ')
            temp_stats.append(payload)
        if len(temp_stats) != 3:
            raise ValueError(f"Invalid stats format: {raw_stats}")
        stats = Stats(
            absolute_running_time=temp_stats[0],
            cpu_time=temp_stats[1],
            memory_peak=temp_stats[2]
        )
        return stats
