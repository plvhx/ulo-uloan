from app import ma
from marshmallow import fields

class LocationSchema(ma.Schema):
	id = fields.UUID()
	type = fields.String()
	code = fields.String()
	name = fields.String()
	address = fields.String()
	latitude = fields.Float()
	longitude = fields.Float()
	phone = fields.String()
	status = fields.String()
	created_at = fields.DateTime()
	updated_at = fields.DateTime()