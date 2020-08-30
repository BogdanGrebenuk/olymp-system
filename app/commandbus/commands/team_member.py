from dataclasses import dataclass

from aiopg.sa import Engine

from commandbus.commands.base_command import Command
from db.entities.team import Team
from core.user.domain.entity import User
from core.team_member import MemberStatus


@dataclass
class CreateTeamMember(Command):
    user: User
    team: Team
    status: MemberStatus
    engine: Engine
