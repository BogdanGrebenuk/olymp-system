from app.utils.transformer import Transformer, DatetimeTransformer
from app.core.contest.domain.entity import Contest


class ContestTransformer(Transformer):
    def __init__(
            self,
            datetime_transformer: DatetimeTransformer
            ):
        self.datetime_transformer = datetime_transformer

    async def transform(self, contest: Contest):
        return {
            'id': contest.id,
            'name': contest.name,
            'description': contest.description,
            'imagePath': contest.image_path,
            'endDate': self.datetime_transformer.transform(contest.end_date),
            'startDate': self.datetime_transformer.transform(contest.start_date),
            'creatorId': contest.creator_id,
            'maxParticipantsInTeam': contest.max_participants_in_team,
            'maxTeams': contest.max_teams
        }
