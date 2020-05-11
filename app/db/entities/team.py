import dataclasses


@dataclasses.dataclass
class Team:
    id: str
    name: str
    contest_id: str
    trainer_id: str

