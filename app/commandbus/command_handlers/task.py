import asyncio
import uuid

from commandbus.command_handlers.base_command_handler import CommandHandler
from commandbus.commands.task import CreateTask
from db import (
    task_mapper,
    task_io_mapper
)
from db.entities.task import Task
from db.entities.task_io import TaskIO


class CreateTaskHandler(CommandHandler):

    async def handle(self, command: CreateTask):
        engine = command.engine
        task_id = str(uuid.uuid4())
        task = Task(
            task_id,
            command.contest.id,
            command.name,
            command.description,
            command.max_cpu_time,
            command.max_memory
        )
        await task_mapper.create(engine, task)
        tasks_io = [
            TaskIO(str(uuid.uuid4()), task.id, input_, output, public)
            for input_, output, public in command.input_output
        ]
        await asyncio.gather(*[
            task_io_mapper.create(engine, task_io)
            for task_io in tasks_io
        ])

        return task
