import dataclasses

import bcrypt


@dataclasses.dataclass
class User:
    id: str
    first_name: str
    last_name: str
    patronymic: str
    email: str
    password: str
    role_id: str

    def check_password(self, password: str):
        return bcrypt.checkpw(
            password.encode(encoding='utf-8'),
            self.password.encode(encoding='utf-8')
        )
