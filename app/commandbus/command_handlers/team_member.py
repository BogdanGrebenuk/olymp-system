import uuid

from app.commandbus.commands.team_member import CreateTeamMember
from app.commandbus.command_handlers.base_command_handler import CommandHandler
from app.db import team_member_mapper
from app.db.entities.team_member import TeamMember


class CreateTeamMemberHandler(CommandHandler):

    async def handle(self, command: CreateTeamMember):
        member_id = str(uuid.uuid4())
        member = TeamMember(
            id=member_id,
            user_id=command.user.id,
            team_id=command.team.id,
            status=command.status.value
        )
        await team_member_mapper.create(command.engine, member)
        return member
