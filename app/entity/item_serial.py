from app import db
from sqlalchemy.dialects.postgresql import UUID

class ItemSerial(db.Model):
	__tablename__ = "item_serial"
	id = db.Column(UUID(as_uuid=True), unique=True, primary_key=True)
	serial = db.Column(db.String(255), nullable=False)
	status = db.Column(db.String(50), nullable=False)
	created_at = db.Column(db.DateTime, nullable=False)
	updated_at = db.Column(db.DateTime, nullable=False)
	item_id = db.Column(UUID(as_uuid=True), db.ForeignKey('item.id'), nullable=False)
	bound_serials = db.relationship('BoundSerial', backref="item_serial", lazy=True)

	def __repr__(self):
		return "ItemSerial(id={})".format(self.id)