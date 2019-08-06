from app import ma
from marshmallow import fields

class BoundSchema(ma.Schema):
    id = fields.UUID()
    type  = fields.String()
    description = fields.String()
    status = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()