import dataclasses

import bcrypt

from core.user_role import UserRole


@dataclasses.dataclass
class User:
    id: str
    first_name: str
    last_name: str
    patronymic: str
    email: str
    password: str
    role: str

    def check_password(self, password: str):
        return bcrypt.checkpw(
            password.encode(encoding='utf-8'),
            self.password.encode(encoding='utf-8')
        )

    def get_user_role(self):
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
