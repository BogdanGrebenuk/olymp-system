import dataclasses


@dataclasses.dataclass
class Contest:
    id: str
    name: str
    description: str
    img_path: str
