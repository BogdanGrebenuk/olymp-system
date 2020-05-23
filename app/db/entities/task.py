import dataclasses


@dataclasses.dataclass
class Task:
    id: str
    contest_id: str
    name: str
    description: str
    max_cpu_time: int
    max_memory: int

    def from_contest(self, contest) -> bool:
        return self.contest_id == contest.id
