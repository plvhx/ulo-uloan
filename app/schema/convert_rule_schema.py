from app import ma
from marshmallow import fields

class ConvertRuleSchema(ma.Schema):
	id = fields.UUID()
	default_amount = fields.Integer()
	status = fields.String()
	created_at = fields.DateTime()
	updated_at = fields.DateTime()
