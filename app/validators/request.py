import typing

from marshmallow import (
    Schema,
    fields,
    ValidationError,
    validate,
    validates_schema
)

from common import (
    get_supported_languages,
    get_roles,
    MAX_NUMBER_OF_PARTICIPANTS,
    DEFAULT_NUMBER_OF_PARTICIPANTS
)


def validate_role(role):
    if role not in get_roles():
        raise ValidationError('there is not such role!')


def validate_language(lang):
    if lang not in get_supported_languages():
        raise ValidationError('unsupported language!')


def validate_task_io(task_ios):
    for io in task_ios:
        if len(io) != 2:
            raise ValidationError('io incorrect specified!')


class MaxParticipantsField(fields.Field):

    def _deserialize(self, value: typing.Any, attr: str, obj: typing.Any, **kwargs):
        if value == 'null':
            return DEFAULT_NUMBER_OF_PARTICIPANTS
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


class VerifyTaskBody(Schema):
    task_id = fields.String(required=True)
    language = fields.String(required=True, validate=validate_language)
    code = fields.String(required=True)


class CreateContestBody(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))
    description = fields.String(required=True, validate=validate.Length(min=1))
    max_participants = MaxParticipantsField(
        required=True,
        validate=validate.Range(1, MAX_NUMBER_OF_PARTICIPANTS)
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
        fields.List(fields.String),
        validate=validate_task_io
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


class RegisterUserBody(Schema):
    first_name = fields.String(required=True, validate=validate.Length(min=1))
    last_name = fields.String(required=True, validate=validate.Length(min=1))
    patronymic = fields.String(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=1))
    role = fields.String(required=True, validate=validate_role)


class AuthenticateUserBody(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=1))
