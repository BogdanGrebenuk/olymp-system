import dataclasses

from app.db.common import Entity


@dataclasses.dataclass
class Team(Entity):
    id: str
    name: str
    contest_id: str
    trainer_id: str

    def is_trainer(self, user):
        return user.id == self.trainer_id

    def from_contest(self, contest):
        return self.contest_id == contest.id
