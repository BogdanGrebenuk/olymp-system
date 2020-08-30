import dataclasses

from app.core.user.domain.role import UserRole


@dataclasses.dataclass
class User:
    id: str
    first_name: str
    last_name: str
    patronymic: str
    email: str
    password: str
    role: str

    def get_role(self):
        if self.role == UserRole.PARTICIPANT.value:
            return UserRole.PARTICIPANT
        if self.role == UserRole.TRAINER.value:
            return UserRole.TRAINER
        if self.role == UserRole.ORGANIZER.value:
            return UserRole.ORGANIZER
        raise ValueError(f'unknown role {self.role}')

    def is_organizer(self):
        return self.role == UserRole.ORGANIZER.value

    def is_participant(self):
        return self.role == UserRole.PARTICIPANT.value

    def is_trainer(self):
        return self.role == UserRole.TRAINER.value

    def is_creator(self, contest) -> bool:
        return self.id == contest.creator_id
