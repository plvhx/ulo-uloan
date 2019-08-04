from flask import request
from flask_restful import Resource
from app import db
from app.entity.item import Item
from app.schema.item_schema import ItemSchema

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)

class ItemResource(Resource):
	def get(self):
		items = Item.query.all()
		items = items_schema.dump(items).data
		return {'status': 'ok', 'data': items}, 200

	def post(self):
		json_data = request.get_json(force=True)

		if not json_data:
			return {'message': 'No input data provided.'}, 400

		data, errors = item_schema.load(json_data)

		if errors:
			return errors, 422

		item = Item.query.filter_by(id=data['id']).first()

		if item:
			return {'message': 'Item already exists.'}, 400

		item = Item(
			id=data['id'],
			code=data['code'],
			name=data['name'],
			description=data['description'],
			on_sale=data['on_sale'],
			position=data['position'],
			price=data['price'],
			track_serial=data['track_serial'],
			unit=data['unit'],
			status=data['status'],
			created_at=data['created_at'],
			updated_at=data['updated_at']
		)

		db.session.add(item)
		db.session.commit()

		result = item_schema.dump(item).data

		return {'status': 'ok', 'data': result}, 201

	def put(self):
		json_data = request.get_json(force=True)

		if not json_data:
			return {'message': 'No input data provided.'}, 400

		data, errors = item_schema.load(json_data)

		if errors:
			return errors, 422

		item = Item.query.filter_by(id=data['id']).first()

		if not item:
			return {'message': 'Item does not exist.'}, 400

		item.code = data['code']
		item.name = data['name']
		item.description = data['description']
		item.on_sale = data['on_sale']
		item.position = data['position']
		item.price = data['price']
		item.track_serial = data['track_serial']
		item.unit = data['unit']
		item.status = data['status']
		item.created_at = data['created_at']
		item.updated_at = data['updated_at']

		# commit update
		db.session.commit()

		result = item_schema.dump(item).data

		return {'status': 'ok', 'data': result}, 204

	def delete(self):
		json_data = request.get_json(force=True)

		if not json_data:
			return {'message': 'No input data provided.'}, 400

		data, errors = item_schema.load(json_data)

		if errors:
			return errors, 422

		item = Item.query.filter_by(id=data['id']).delete()

		db.session.commit()

		return {'status': 'ok', 'data': result}, 204
