import typing

from marshmallow import (
    Schema,
    fields,
    ValidationError,
    validate,
    validates_schema
)

from common import (
    MAX_NUMBER_OF_PARTICIPANTS,
    DEFAULT_NUMBER_OF_PARTICIPANTS
)
from core.language import get_supported_languages


class MaxParticipantsField(fields.Field):

    def _deserialize(self, value: typing.Any, attr: str, obj: typing.Any, **kwargs):
        if value == 'null':
            return DEFAULT_NUMBER_OF_PARTICIPANTS
        return int(value)


class MaxTeamsField(fields.Field):

    def _deserialize(self, value: typing.Any, attr: str, obj: typing.Any, **kwargs):
        if value == 'null':
            return None
        return int(value)


class ImageField(fields.Field):

    def _deserialize(
        self,
        value: typing.Any,
        attr: typing.Optional[str],
        data: typing.Optional[typing.Mapping[str, typing.Any]],
        **kwargs
    ):
        if value == 'null':
            return None
        return value


class CreateSolutionUrlVars(Schema):
    contest_id = fields.String(required=True)


class CreateSolutionBody(Schema):
    task_id = fields.String(required=True)
    language = fields.String(
        required=True,
        validate=validate.OneOf(get_supported_languages())
    )
    code = fields.String(required=True)


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


class CreateTaskBody(Schema):
    contest_id = fields.String(required=True)
    input_output = fields.List(
        fields.Tuple(
            (fields.String(), fields.String(), fields.Bool())
        ),
        validate=validate.Length(1)
    )
    name = fields.String(required=True, validate=validate.Length(min=1))
    description = fields.String(required=True)
    max_cpu_time = fields.Integer(
        required=True,
        validate=validate.Range(min=1)
    )
    max_memory = fields.Integer(
        required=True,
        validate=validate.Range(min=1)
    )


class CreateTeamBody(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))
    contest_id = fields.String(required=True)


class CreateMemberBody(Schema):
    email = fields.Email(required=True)
    team_id = fields.String(required=True)


class AcceptInviteUrlVars(Schema):
    invite_id = fields.String(required=True)


class DeclineInviteUrlVars(Schema):
    invite_id = fields.String(required=True)


class DeleteMemberUrlVars(Schema):
    invite_id = fields.String(required=True)


class GetSentInvitesParams(Schema):
    contest_id = fields.String(required=True)


class GetReceivedInvitesParams(Schema):
    contest_id = fields.String(required=True)


class GetTasksUrlVars(Schema):
    contest_id = fields.String(required=True)


class GetTaskUrlVars(Schema):
    contest_id = fields.String(required=True)
    task_id = fields.String(required=True)


class GetContestUrlVars(Schema):
    contest_id = fields.String(required=True)


class GetTeamsForContestUrlVars(Schema):
    contest_id = fields.String(required=True)


class GetTeamsForContestParams(Schema):
    creator_id = fields.String(required=False)


class GetTeamUrlVars(Schema):
    contest_id = fields.String(required=True)
    team_id = fields.String(required=True)


class GetAcceptedMembersUrlVars(Schema):
    contest_id = fields.String(required=True)
    team_id = fields.String(required=True)


class GetInvitesForTeamUrlVars(Schema):
    contest_id = fields.String(required=True)
    team_id = fields.String(required=True)


class GetSolutionsUrlVars(Schema):
    contest_id = fields.String(required=True)


class GetSolutionParams(Schema):
    team_id = fields.String(required=False)


class GetSolutionCodeUrlVars(Schema):
    contest_id = fields.String(required=True)
    solution_id = fields.String(required=True)


class GetContestLeaderBoardUrlVars(Schema):
    contest_id = fields.String(required=True)
