from dataclasses import dataclass

from aiopg.sa import Engine

from app.commandbus.commands.base_command import Command
from app.core.team.domain.entity import Team
from app.core.user.domain.entity import User
from app.core.team_member import MemberStatus


@dataclass
class CreateTeamMember(Command):
    user: User
    team: Team
    status: MemberStatus
    engine: Engine
