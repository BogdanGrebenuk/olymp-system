from app.core.team.domain.entity import Team
from app.utils.transformer import Transformer


class TeamTransformer(Transformer):

    async def transform(self, team: Team):
        return {
            'id': team.id,
            'name': team.name,
            'contestId': team.contest_id,
            'trainerId': team.trainer_id
        }
