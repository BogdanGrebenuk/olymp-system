import dataclasses


@dataclasses.dataclass
class User:
    id: str
    firstname: str
    lastname:str
    patronymic: str
    salt: str
    password: str
