from app import ma
from marshmallow import fields

class ItemSchema(ma.Schema):
	id = fields.UUID()
	code = fields.String()
	name = fields.String()
	description = fields.String()
	on_sale = fields.Integer()
	position = fields.Integer()
	price = fields.Float()
	track_serial = fields.Integer()
	unit = fields.String()
	status = fields.String()
	created_at = fields.DateTime()
	updated_at = fields.DateTime()
