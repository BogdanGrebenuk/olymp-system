import uuid

from app.commandbus.command_handlers.base_command_handler import CommandHandler
from app.core.team.commands import CreateTeam
from app.db import TeamMapper
from app.core.team.domain.entity import Team
from app.exceptions.domain import DomainException


class CreateTeamHandler(CommandHandler):

    def __init__(
            self,
            team_mapper: TeamMapper
            ):
        self.team_mapper = team_mapper

    async def handle(
            self,
            command: CreateTeam
            ):
        name = command.name
        contest_id = command.contest_id

        team = await self.team_mapper.find_one_by(name=name, contest_id=contest_id)
        if team is not None:
            raise DomainException(
                f'Team with name {name} already exists for contest {contest_id}!',
                {
                    'name': name,
                    'contest_id': contest_id
                }
            )

        team_id = str(uuid.uuid4())
        team = Team(
            id=team_id,
            name=command.name,
            contest_id=command.contest_id,
            trainer_id=command.trainer_id
        )

        return team
