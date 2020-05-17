import dataclasses

from core.team_member import MemberStatus


@dataclasses.dataclass
class TeamMember:
    id: str
    user_id: str
    team_id: str
    status: str

    def set_status(self, status: MemberStatus):
        self.status = status.value

    def is_status_pending(self):
        return self.status == MemberStatus.PENDING.value

    def is_status_accepted(self):
        return self.status == MemberStatus.ACCEPTED.value
