from marshmallow import (
    Schema,
    fields,
    validate
)

from app.core.user.domain.role import get_roles


class RegisterUserBody(Schema):
    first_name = fields.String(required=True, validate=validate.Length(min=1))
    last_name = fields.String(required=True, validate=validate.Length(min=1))
    patronymic = fields.String(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=1))
    role = fields.String(required=True, validate=validate.OneOf(get_roles()))


class AuthenticateUserBody(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=1))


class GetUserUrlVars(Schema):
    user_id = fields.String(required=True)
