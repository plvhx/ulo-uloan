from app import db
from sqlalchemy.dialects.postgresql import UUID

class ConvertRule(db.Model):
	__tablename__ = "convert_rule"
	id = db.Column(UUID(as_uuid=True), unique=True, primary_key=True)
	default_amount = db.Column(db.Integer, nullable=False)
	status = db.Column(db.String(50), nullable=False)
	created_at = db.Column(db.DateTime, nullable=False)
	updated_at = db.Column(db.DateTime, nullable=False)
	item_from_id = db.Column(UUID(as_uuid=True), db.ForeignKey('item.id'), nullable=False)
	item_to_id = db.Column(UUID(as_uuid=True), db.ForeignKey('item.id'), nullable=False)

	def __repr__(self):
		return "ConvertRule(id={})".format(self.id)
