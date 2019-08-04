from app import db
from sqlalchemy.dialects.postgresql import UUID

class Item(db.Model):
	__tablename__ = "item"
	id = db.Column(UUID(as_uuid=True), unique=True, primary_key=True)
	code = db.Column(db.String(50), nullable=False)
	name = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(200), nullable=False)
	on_sale = db.Column(db.Integer, nullable=False)
	position = db.Column(db.Integer, nullable=False)
	price = db.Column(db.Float, nullable=False)
	track_serial = db.Column(db.Integer, nullable=False)
	unit = db.Column(db.String(50), nullable=False)
	status = db.Column(db.String(50), nullable=False)
	created_at = db.Column(db.DateTime, nullable=False)
	updated_at = db.Column(db.DateTime, nullable=False)
	item_serials = db.relationship('ItemSerial', backref="item", lazy=True)
	bound_items = db.relationship('BoundItem', backref="item", lazy=True)

	def __repr__(self):
		return "Item(id={})".format(self.id)