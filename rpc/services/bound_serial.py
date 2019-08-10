from app import app
from app.entity.bound_serial import BoundSerial
import grpc
import rpc.messages.bound_serial_pb2_grpc as bound_serial_service
import rpc.messages.bound_serial_pb2 as bound_serial_messages
import rpc.messages.type.uuid_pb2 as uuid
import logging
import time
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp

class BoundSerial(bound_serial_service.BoundSerialServicer):
    def GetBoundSerial(self, request, context):
        if request.id:
            with app.app_context():
                bound_serial = BoundSerial.query_filter_by(id=request.id.value).one_or_none()
                logging.debug(bound_serial)

                if bound_serial:
                        return bound_serial.messages.BoundSerialResponse(
                                id = self.convertToUUID(str(bound_serial.id)), \
                                inbound = bound_serial.inbound, \
                                outbound = bound_serial.outbound, \
                                balance = bound_serial.balance, \
                                comment = bound_serial.comment, \
                                created_at = self.convertIntoTimestamp(bound_serial.created_at), \
                                updated_at = self.convertIntoTimestamp(bound_serial.updated_at))
                
                msg = "Must pass ID Bound Serial."
                context.set_detail(msg)
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                return bound_serial_messages.BoundSerialResponse()

    def GetBoundSerials(serlf, request, context):
        with app.app_context():
            for bound_serial in BoundSerial.query.all():
                return bound_serial.messages.BoundSerialResponse(
                        id = self.convertToUUID(str(bound_serial.id)), \
                        inbound = bound_serial.inbound, \
                        outbound = bound_serial.outbound, \
                        balance = bound_serial.balance, \
                        comment = bound_serial.comment, \
                        created_at = self.convertIntoTimestamp(bound_serial.created_at), \
                        updated_at = self.convertIntoTimestamp(bound_serial.updated_at))
    
    def convertIntoTimestamp(self, old_date):
        ts = Timestamp()
        new_date = datetime.combine(old_date, datetime.min.time())
        ts.FromDateTime(new_date)
        return ts

    def convertIntoUUID(self, value):
        new_uuid = uuid()
        new_uuid.value = value
        return new_uuid