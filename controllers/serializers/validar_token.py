from marshmallow import Schema, fields


class ValidarTokenSerializer(Schema):
    token = fields.String(required=True)


class ResetPasswordSerializer(Schema):
    token = fields.String(required=True)
    password = fields.String(required=True)
