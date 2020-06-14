import dataclasses


@dataclasses.dataclass
class TaskIO:
    id: str
    task_id: str
    input: str
    output: str
    public: bool = False
