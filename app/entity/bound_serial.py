from app import db
from sqlalchemy.dialects.postgresql import UUID

class BoundSerial(db.Model):
	__tablename__ = "bound_serial"
	id = db.Column(UUID(as_uuid=True), unique=True, primary_key=True)
	inbound = db.Column(db.Integer, nullable=False)
	outbound = db.Column(db.Integer, nullable=False)
	balance = db.Column(db.Integer, nullable=False)
	comment = db.Column(db.String(255), nullable=False)
	created_at = db.Column(db.DateTime, nullable=False)
	updated_at = db.Column(db.DateTime, nullable=False)
	bound_id = db.Column(UUID(as_uuid=True), db.ForeignKey('bound.id'), nullable=False)
	serial_id = db.Column(UUID(as_uuid=True), db.ForeignKey('item_serial.id'), nullable=False)

	def __repr__(self):
		return "BoundSerial(id={})".format(self.id)