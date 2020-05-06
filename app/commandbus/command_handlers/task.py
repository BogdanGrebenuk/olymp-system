import asyncio
import uuid

from commandbus.command_handlers.base_command_handler import CommandHandler
from commandbus.commands.task import CreateTask
from db.entities.task import Task
from db.entities.task_io import TaskIO
from db.procedures.task import create_task
from db.procedures.task_io import create_task_io


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
        await create_task(engine, task)
        tasks_io = [
            TaskIO(str(uuid.uuid4()), task.id, input_, output)
            for input_, output in command.input_output
        ]
        await asyncio.gather(*[
            create_task_io(engine, task_io)
            for task_io in tasks_io
        ])

        return task
