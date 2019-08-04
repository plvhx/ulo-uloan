from app import db
from sqlalchemy.dialects.postgresql import UUID

class Bound(db.Model):
	__tablename__ = "bound"
	id = db.Column(UUID(as_uuid=True), unique=True, primary_key=True)
	type = db.Column(db.String(50), nullable=False)
	description = db.Column(db.String(255), nullable=False)
	status = db.Column(db.String(50), nullable=False)
	created_at = db.Column(db.DateTime, nullable=False)
	updated_at = db.Column(db.DateTime, nullable=False)
	location_id = db.Column(UUID(as_uuid=True), db.ForeignKey('location.id'), nullable=False)
	bound_serials = db.relationship('BoundSerial', backref="bound", lazy=True)
	bound_items = db.relationship("BoundItem", backref="bound", lazy=True)

	def __repr__(self):
		return "Bound(id={})".format(self.id)
