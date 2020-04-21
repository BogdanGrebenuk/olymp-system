import dataclasses


@dataclasses.dataclass
class Task:
    id: str
    contest_id: str
    description: str
    max_cpu_time: int
    max_memory: int