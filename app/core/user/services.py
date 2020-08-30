import bcrypt


class PasswordChecker:

    def __init__(self, client=bcrypt):
        self.client = client

    def check(self, password: str, hashed_password: str) -> bool:
        return self.client.checkpw(
            password.encode(encoding='utf-8'),
            hashed_password.encode(encoding='utf-8')
        )


class PasswordGenerator:

    def __init__(self, client=bcrypt):
        self.client = client

    def generate(self, password: str) -> str:
        password = password.encode(encoding='utf-8')
        salt = self.client.gensalt()
        hashed_password = self.client.hashpw(password, salt).decode()
        return hashed_password
