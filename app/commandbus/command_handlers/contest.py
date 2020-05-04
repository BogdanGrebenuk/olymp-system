import uuid

from commandbus.command_handlers.base_command_handler import CommandHandler
from commandbus.commands.contest import CreateContest
from db.entities.contest import Contest
from db.procedures.contest import create_contest


class CreateContestHandler(CommandHandler):

    async def handle(self, command: CreateContest):
        engine = command.engine
        contest_id = str(uuid.uuid4())
        contest = Contest(contest_id, command.name, command.description)
        await create_contest(engine, contest)
        return contest
