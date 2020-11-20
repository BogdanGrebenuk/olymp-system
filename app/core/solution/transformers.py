from app.core.solution.domain.entity import Solution
from app.utils.transformer import Transformer


class SolutionTransformer(Transformer):

    async def transform(self, solution: Solution) -> dict:
        return {
            'id': solution.id,
            'taskId': solution.task_id,
            'language': solution.language,
            'isPassed': solution.is_passed,
            'teamId': solution.team_id,
            'userId': solution.user_id
        }
