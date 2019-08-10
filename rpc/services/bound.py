from app import app
from app.entity.bound import Bound
import grpc
import rpc.messages.bound_pb2_grpc as bound_service
import rpc.messages.bound_pb2 as bound_messages
import rpc.messages.type.uuid_pb2 as uuid
import logging
import time
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp

class BoundService(bound_service.BoundServicer):
    def GetBound(self, request, context):
        if.request.id:
            with app.app_context():
                bound = Bound.query_filter_by(id=request.id.value).one_or_none()
                logging.debug(bound)

                if bound:
                        return bound.messages.BoundResponse(
                                id = self.convertToUUID(str(bound.id)), \
                                type = bound.type, \
                                description = bound.description, \
                                status = bound.status, \
                                created_at = self.convertIntoTimestamp(bound.created_at), \
                                updated_at = self.convertIntoTimestamp(bound.updated_at))
                
                msg = "Must pass ID Bound."
                context.set_detail(msg)
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                return bound_messages.BoundResponse()

    def GetBounds(self, request, context):
        with app.app_context():
            for bound in Bound.query.all():
                return bound.messages.BoundResponse(
                        id = self.convertToUUID(str(bound.id)), \
                        type = bound.type, \
                        description = bound.description, \
                        status = bound.status, \
                        created_at = self.convertIntoTimestamp(bound.created_at), \
                        updated_at = self.convertIntoTimestamp(bound.updated_at))

    def convertIntoTimestamp(self, old_date):
        ts = Timestamp()
        new_date = datetime.combine(old_date, datetime.min.time())
        ts.FromDateTime(new_date)
        return ts

    def convertIntoUUID(self, value):
        new_uuid = uuid()
        new_uuid.value = value
        return new_uuid