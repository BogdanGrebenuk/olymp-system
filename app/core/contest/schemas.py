from marshmallow import (
    Schema,
    fields,
    ValidationError,
    validate,
    validates_schema
)

from app.common import (
    MAX_NUMBER_OF_PARTICIPANTS,
)

from app.validators.schemas import MaxParticipantsField, MaxTeamsField, ImageField


class CreateContestBody(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))
    description = fields.String(required=True, validate=validate.Length(min=1))
    max_participants_in_team = MaxParticipantsField(
        required=True,
        validate=validate.Range(1, MAX_NUMBER_OF_PARTICIPANTS)
    )
    max_teams = MaxTeamsField(
        required=True,
        validate=validate.Range(1),
        allow_none=True
    )
    image = ImageField(required=True)
    start_date = fields.DateTime(required=True)
    end_date = fields.DateTime(required=True)

    @validates_schema
    def validate_date(self, data, **kwargs):
        errors = {}
        if data['start_date'] >= data['end_date']:
            errors['start_date'] = ['start_date is greater then end_date!']
        if errors:
            raise ValidationError(errors)


class GetContestUrlVars(Schema):
    contest_id = fields.String(required=True)


class GetContestLeaderBoardUrlVars(Schema):
    contest_id = fields.String(required=True)
