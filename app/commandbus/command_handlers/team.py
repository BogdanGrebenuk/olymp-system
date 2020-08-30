import uuid

from app.commandbus.command_handlers.base_command_handler import CommandHandler
from app.commandbus.commands.team import CreateTeam
from app.db import team_mapper
from app.db.entities.team import Team


class CreateTeamHandler(CommandHandler):

    async def handle(self, command: CreateTeam):
        engine = command.engine
        team_id = str(uuid.uuid4())
        team = Team(
            id=team_id,
            name=command.name,
            contest_id=command.contest_id,
            trainer_id=command.trainer_id
        )
        await team_mapper.create(engine, team)
        return team
