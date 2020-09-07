from marshmallow import (
    Schema,
    fields,
    validate
)


class CreateTeamBody(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))
    contest_id = fields.String(required=True)


class GetTeamsForContestUrlVars(Schema):
    contest_id = fields.String(required=True)


class GetTeamsForContestParams(Schema):
    creator_id = fields.String(required=False)


class GetTeamUrlVars(Schema):
    contest_id = fields.String(required=True)
    team_id = fields.String(required=True)
