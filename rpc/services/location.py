from app import app
from app.entity.location import Location
import grpc
import rpc.messages.location_pb2_grpc as location_service
import rpc.messages.location_pb2 as location_messages
from rpc.messages.type.uuid_pb2 import uuid
import logging
import time
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp

class LocationService(location_service.LocationServicer):
	def GetLocation(self, request, context):
		if request.id:
			with app.app_context():
				location = Location.query.filter_by(id=request.id.value).one_or_none()
				logging.debug(location)

				if location:
					return location_messages.LocationResponse( \
						id = self.convertIntoUUID(str(location.id)), \
						type = location.type, \
						code = location.code, \
						name = location.name, \
						address = location.address, \
						latitude = location.latitude, \
						longitude = location.longitude, \
						phone = location.phone, \
						status = location.status, \
						created_at = self.convertIntoTimestamp(location.created_at), \
						updated_at = self.convertIntoTimestamp(location.updated_at))

				msg = "Location ID not found."
				context.set_details(msg)
				context.set_code(grpc.StatusCode.NOT_FOUND)
				return location_messages.UserResponse()

		msg = "Must pass ID location."
		context.set_details(msg)
		context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
		return location_messages.UserResponse()

	def GetLocations(self, request, context):
		with app.app_context():
			for location in Location.query.all():
				yield location_messages.LocationResponse(
					id = self.convertIntoUUID(str(location.id)), \
					type = location.type, \
					code = location.code, \
					name = location.name, \
					address = location.address, \
					latitude = location.latitude, \
					longitude = location.longitude, \
					phone = location.phone, \
					status = location.status, \
					created_at = self.convertIntoTimestamp(location.created_at), \
					updated_at = self.convertIntoTimestamp(location.updated_at))

	def convertIntoTimestamp(self, old_date):
		ts = Timestamp()
		new_date = datetime.combine(old_date, datetime.min.time())
		ts.FromDatetime(new_date)
		return ts

	def convertIntoUUID(self, value):
		new_uuid = uuid()
		new_uuid.value = value
		return new_uuid
