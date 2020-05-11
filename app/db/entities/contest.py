import dataclasses
import typing
from datetime import datetime


@dataclasses.dataclass
class Contest:
    id: str
    name: str
    description: str
    max_teams: typing.Union[int, None]
    max_participants_in_team: int
    image_path: str
    start_date: datetime
    end_date: datetime
    creator_id: str

    def is_started(self, t: datetime = None) -> bool:
        if t is None:
            t = datetime.now()
        return t >= self.start_date
