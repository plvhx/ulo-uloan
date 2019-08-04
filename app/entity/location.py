from app import db
from sqlalchemy.dialects.postgresql import UUID

class Location(db.Model):
	__tablename__ = "location"
	id = db.Column(UUID(as_uuid=True), unique=True, primary_key=True)
	type = db.Column(db.String(50), nullable=False)
	code = db.Column(db.String(50), nullable=False)
	name = db.Column(db.String(100), nullable=False)
	address = db.Column(db.String(200), nullable=False)
	latitude = db.Column(db.Float, nullable=False)
	longitude = db.Column(db.Float, nullable=False)
	phone = db.Column(db.String(20), nullable=False)
	status = db.Column(db.String(50), nullable=False)
	created_at = db.Column(db.DateTime, nullable=False)
	updated_at = db.Column(db.DateTime, nullable=False)
	bounds = db.relationship('Bound', backref="location", lazy=True)

	def __repr__(self):
		return "Location(id={})".format(self.id)
