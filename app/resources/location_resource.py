from flask import request
from flask_restful import Resource
from app import db
from app.entity.location import Location
from app.schema.location_schema import LocationSchema

location_schema = LocationSchema()
locations_schema = LocationSchema(many=True)

class LocationResource(Resource):
	def get(self):
		locations = Location.query.all()
		locations = locations_schema.dump(locations).data
		return {'status': 'success', 'data': locations}, 200

	def post(self):
		json_data = request.get_json(force=True)

		if not json_data:
			return {'message': 'No input data provided.'}, 400

		data, errors = location_schema.load(json_data)

		if errors:
			return errors, 422

		location = Location.query.filter_by(id=data['id']).first()

		if location:
			return {'message': 'Category already exists.'}, 400

		location = Location(
			id=json_data['id'],
			type=json_data['type'],
			code=json_data['code'],
			name=json_data['name'],
			address=json_data['address'],
			latitude=json_data['latitude'],
			longitude=json_data['longitude'],
			phone=json_data['phone'],
			status=json_data['status'],
			created_at=json_data['created_at'],
			updated_at=json_data['updated_at']
		)

		db.session.add(location)
		db.session.commit()

		result = location_schema.dump(location).data

		return {'status': 'ok', 'data': result}, 201
