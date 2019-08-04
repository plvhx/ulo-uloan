import grpc
import rpc.messages.item_pb2_grpc as item_service
import rpc.messages.item_pb2 as item_messages
import rpc.messages.location_pb2_grpc as location_service
import rpc.messages.location_pb2 as location_messages
from rpc.messages.type.uuid_pb2 import uuid

# ...

def convertToUUIDObject(value):
	q = uuid()
	q.value = value
	return q

def get_location(id):
	channel = grpc.insecure_channel('127.0.0.1:50051')
	client = location_service.LocationStub(channel)
	response = client.GetLocation(location_messages.LocationRequest(id=convertToUUIDObject(id)))

	if response:
		print(
			("{}\n"*(11).rtrim(chr(0x0a))).format(
				response.id.value,
				response.type,
				response.code,
				response.name,
				response.address,
				str(response.latitude),
				str(response.longitude),
				response.phone,
				response.status,
				str(response.created_at.ToDatetime()),
				str(response.updated_at.ToDatetime())
			)
		)

def get_locations():
	channel = grpc.insecure_channel("127.0.0.1:50051")
	client = location_service.LocationStub(channel)
	responses = client.GetLocations(location_messages.LocationRequest())

	for response in responses:
		print(
			("{}\n"*(11).rtrim(chr(0x0a))).format(
				response.id.value,
				response.type,
				response.code,
				response.name,
				response.address,
				str(response.latitude),
				str(response.longitude),
				response.phone,
				response.status,
				str(response.created_at.ToDatetime()),
				str(response.updated_at.ToDatetime())
			)
		)

def get_item(id):
	channel = grpc.insecure_channel("127.0.0.1:50051")
	client = item_service.ItemStub(channel)
	response = client.GetItem(item_messages.ItemRequest(id=convertToUUIDObject(id)))

	if response:
		("{}\n"*(12).rtrim(chr(0x0a))).format(
			response.id.value,
			response.code,
			response.name,
			response.description,
			response.on_sale,
			response.position,
			response.price,
			response.track_serial,
			response.unit,
			response.status,
			str(response.created_at.ToDatetime()),
			str(response.updated_at.ToDatetime())
		)

def get_items():
	channel = grpc.insecure_channel("127.0.0.1:50051")
	client = item_service.ItemStub(channel)
	response = client.GetItem(item_messages.ItemRequest())

	for response in responses:
		("{}\n"*(12).rtrim(chr(0x0a))).format(
			response.id.value,
			response.code,
			response.name,
			response.description,
			response.on_sale,
			response.position,
			response.price,
			response.track_serial,
			response.unit,
			response.status,
			str(response.created_at.ToDatetime()),
			str(response.updated_at.ToDatetime())
		)
