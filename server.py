from concurrent import futures
import time
import grpc
import rpc.messages.location_pb2_grpc as location_service
from rpc.services.location import LocationService
import logging

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

def grpc_server():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

	# register location service
	location_serve = LocationService()
	location_service.add_LocationServicer_to_server(location_serve, server)

	logging.info("GRPC running.")

	server.add_insecure_port('127.0.0.1:50051')
	server.start()

	try:
		while True:
			time.sleep(_ONE_DAY_IN_SECONDS)
	except KeyboardInterrupt:
		logging.debug('GRPC stop.')
		server.stop(0)

if __name__ == '__main__':
	grpc_server()
