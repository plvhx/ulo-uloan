from app import app
from app.entity.item import Item
import grpc
import rpc.messages.item_pb2_grpc as item_service
import rpc.messages.item_pb2 as item_messages
from rpc.message.type.uuid_pb2 import uuid
import logging
import time
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp

class ItemService(item_service.ItemServicer):
	def GetItem(self, request, context):
		if request.id:
			with app.app_context():
				item = Item.query.filter_by(id=id).one_or_none()
				logging.debug(item)

				if item:
					return item_messages.ItemResponse( \
						id = self.convertIntoUUID(str(item.id)), \
						code = item.code, \
						name = item.name, \
						description = item.description, \
						on_sale = item.on_sale, \
						position = item.position, \
						price = item.price, \
						track_serial = item.track_serial, \
						unit = item.unit, \
						status = item.status, \
						created_at = self.convertIntoTimestamp(item.created_at), \
						updated_at = self.convertIntoTimestamp(item.updated_at))

				msg = "Item ID not found."
				context.set_details(msg)
				context.set_code(grpc.StatusCode.NOT_FOUND)
				return item_messages.ItemResponse()

		msg = "Must pass ID item."
		context.set_details(msg)
		context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
		return item_messages.ItemResponse()

	def GetItems(self, request, context):
		with app.app_context():
			for item in Item.query.all():
				yield item_messages.ItemResponse(
					id = self.convertIntoUUID(str(item.id)), \
					code = item.code, \
					name = item.name, \
					description = item.description, \
					on_sale = item.on_sale, \
					position = item.position, \
					price = item.price, \
					track_serial = item.track_serial, \
					unit = item.unit, \
					status = item.status, \
					created_at = self.convertIntoTimestamp(item.created_at), \
					updated_at = self.convertIntoTimestamp(item.updated_at))

	def convertIntoTimestamp(self, old_date):
		ts = Timestamp()
		new_date = datetime.combine(old_date, datetime.min.time())
		ts.FromDatetime(new_date)
		return ts

	def convertIntoUUID(self, value):
		new_uuid = uuid()
		new_uuid.value = value
		return new_uuid
