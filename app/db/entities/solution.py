from common import ROOT_DIR

import dataclasses


@dataclasses.dataclass
class Solution:
    id: str
    path: str
    language: str
    task_id: str
    user_id: str
    team_id: str
    is_passed: bool = False

    def get_full_path(self) -> str:
        return str(ROOT_DIR / self.path)

    def from_team(self, team) -> bool:
        return self.team_id == team.id
