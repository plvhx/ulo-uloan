from app import ma
from marshmallow import fields

class ItemSerialSchema(ma.Schema):
	id = fields.UUID()
	serial = fields.String()
	status = fields.String()
	created_at = fields.DateTime()
	updated_at = fields.DateTime()
