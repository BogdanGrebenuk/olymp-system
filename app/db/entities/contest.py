import dataclasses
import typing
from datetime import datetime
from dateutil.tz import tzutc


@dataclasses.dataclass
class Contest:
    id: str
    name: str
    description: str
    max_teams: typing.Union[int, None]
    max_participants_in_team: int
    image_path: str
    start_date: datetime  # TODO: there is a 'UTC' locale in postgresql.conf,
    # how to specify timezone only for connection?
    end_date: datetime  
    creator_id: str

    def is_running(self, t: datetime = None) -> bool:
        if t is None:
            t = datetime.now(tzutc())
        return self.start_date <= t <= self.end_date

    def can_view_tasks(self, user) -> bool:
        if self.is_running():
            return True
        return user.id == self.creator_id
