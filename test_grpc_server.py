import grpc
import rpc.messages.location_pb2_grpc as location_service
import rpc.messages.location_pb2 as location_messages

# ...

def get_location(id):
	channel = grpc.insecure_channel('127.0.0.1:50051')
	client = location_service.LocationStub(channel)
	response = client.GetLocation(location_messages.LocationRequest(id=id))

	if response:
		print(
			("{}\n"*(11)).format(
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
			("{}\n"*(11)).format(
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

#get_location("f75e9dd5-c6ba-4212-b6c6-b2616492723c")
get_locations()