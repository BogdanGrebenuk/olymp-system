from marshmallow import (
    Schema,
    fields,
    ValidationError,
    validate
)

from common import get_supported_languages


def validate_language(lang):
    if lang not in get_supported_languages():
        raise ValidationError('unsupported language!')


def validate_task_io(task_ios):
    for io in task_ios:
        if len(io) != 2:
            raise ValidationError('io incorrect specified!')


class VerifyTaskBody(Schema):
    task_id = fields.String(required=True)
    language = fields.String(required=True, validate=validate_language)
    code = fields.String(required=True)


class CreateContestBody(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))
    description = fields.String(required=True, validate=validate.Length(min=1))


class CreateTaskBody(Schema):
    contest_id = fields.String(required=True)
    input_output = fields.List(
        fields.List(fields.String),
        validate=validate_task_io
    )
    description = fields.String(required=True)
    max_cpu_time = fields.Integer(
        required=True,
        validate=validate.Range(min=1)
    )
    max_memory = fields.Integer(
        required=True,
        validate=validate.Range(min=1)
    )
