from datetime import datetime
from uuid import uuid4

from dateutil.tz.tz import tzutc

from app.common import CODE_DIR, ROOT_DIR
from app.core.solution.domain.entity import Solution
from app.core.user.domain.entity import User
from app.db.entities import Contest, Task, Team


class SolutionCreator:

    def __init__(self, code_saver):
        self.code_saver = code_saver

    async def create(
            self,
            contest: Contest,
            task: Task,
            user: User,
            team: Team,
            language: str,
            code: str
            ) -> Solution:
        solution_id = str(uuid4())
        solution_dir = CODE_DIR / contest.id / task.id / solution_id
        await self.code_saver.save_code(solution_dir, language, code)
        solution = Solution(
            id=solution_id,
            task_id=task.id,
            team_id=team.id,
            user_id=user.id,
            language=language,
            path=str(solution_dir.relative_to(ROOT_DIR)),
            created_at=datetime.now(tzutc())
        )
        return solution
