import dataclasses


@dataclasses.dataclass
class Solution:
    id: str
    task_id: str
    path: str
    language: str
    is_passed: bool = False
