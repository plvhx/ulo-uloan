from app import ma
from marshmallow import fields

class BoundSerialSchema(ma.Schema):
	id = fields.UUID()
	inbound = fields.Integer()
	outbound = fields.Integer()
	balance = fields.Integer()
	comment = fields.String()
	created_at = fields.DateTime()
	updated_at = fields.DateTime()