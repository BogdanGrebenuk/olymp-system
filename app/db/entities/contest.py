import dataclasses


@dataclasses.dataclass
class Contest:
    id: str
    name: str
    description: str
    image_path: str
