import dataclasses
from datetime import datetime

@dataclasses.dataclass
class Contest:
    id: str
    name: str
    description: str
    image_path: str
    start_date: datetime
    end_date: datetime
