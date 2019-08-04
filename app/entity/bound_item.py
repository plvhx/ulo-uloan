from app import db
from sqlalchemy.dialects.postgresql import UUID

class BoundItem(db.Model):
	__tablename__ = "bound_item"
	id = db.Column(UUID(as_uuid=True), unique=True, primary_key=True)
	inbound = db.Column(db.Integer, nullable=False)
	outbound = db.Column(db.Integer, nullable=False)
	balance = db.Column(db.Integer, nullable=False)
	comment = db.Column(db.String(255), nullable=False)
	created_at = db.Column(db.DateTime, nullable=False)
	updated_at = db.Column(db.DateTime, nullable=False)
	bound_id = db.Column(UUID(as_uuid=True), db.ForeignKey('bound.id'), nullable=False)
	item_id = db.Column(UUID(as_uuid=True), db.ForeignKey('item.id'), nullable=False)

	def __repr__(self):
		return "BoundItem(id={})".format(self.id)
