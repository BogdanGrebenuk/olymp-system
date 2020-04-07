from marshmallow import Schema, fields, ValidationError

from services.docker import get_supported_languages


def validate_language(lang):
    if lang not in get_supported_languages():
        raise ValidationError('unsupported language!')


class VerifyTaskBody(Schema):
    user_id = fields.Integer(required=True)
    contest_id = fields.Integer(required=True)
    task_id = fields.Integer(required=True)
    language = fields.String(required=True, validate=validate_language)
    code = fields.String(required=True)
