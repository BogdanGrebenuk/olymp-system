from app.core.team.domain.entity import Team


class TeamTransformer:

    async def transform(self, team: Team):
        return {
            'id': team.id,
            'name': team.name,
            'contestId': team.contest_id,
            'trainerId': team.trainer_id
        }
