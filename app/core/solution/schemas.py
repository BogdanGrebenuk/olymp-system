from marshmallow import Schema, fields, validate

from app.core.language import get_supported_languages


class CreateSolutionUrlVars(Schema):
    contest_id = fields.String(required=True)


class CreateSolutionBody(Schema):
    task_id = fields.String(required=True)
    language = fields.String(
        required=True,
        validate=validate.OneOf(get_supported_languages())
    )
    code = fields.String(required=True)


class GetSolutionsUrlVars(Schema):
    contest_id = fields.String(required=True)


class GetSolutionParams(Schema):
    team_id = fields.String(required=False)


class GetSolutionCodeUrlVars(Schema):
    contest_id = fields.String(required=True)
    solution_id = fields.String(required=True)