from app import app
from app.entity.bound_item import BoundItem
import grpc
import rpc.messages.bound_item_pb2_grpc as bound_item_service
import rpc.messages.bound_item_pb2 as bound_item_messages
from rpc.messages.type.uuid_pb2 as uuid
import logging
import time
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp

class BoundItemService(bound_item_service.BoundItemServicer):
    def GetBoundItem(self, request, context):
        if request.id:
            with app.app_context():
                bound_item_messages = BoundItem.query_filter_by(id=request.id.value).one_or_none()
                logging.debug(bound_item_messages)
                if bound_item:
                    return bound_item.messages.BoundItemResponse(
                            id = self.convertToUUID(str(bound_item.id)), \
                            inbound = bound_item.inbound, \
                            outbound = bound_item.outbound, \
                            balance = bound_item.balance, \
                            comment = bound_item.comment, \
                            created_at = self.convertIntoTimestamp(bound_item.created_at), \
                            updated_at = self.convertIntoTimestamp(bound_item.updated_at))
            
            msg = "Must pass ID Bound Item."
            context.set_detail(msg)
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return bound_item_messages.BoundItemResponse()

    def GetBoundItems(serlf, request, context):
        with app.app_context():
            for bound_item in BoundSerial.query.all():
                return bound_item.messages.BoundItemResponse(
                        id = self.convertToUUID(str(bound_item.id)), \
                        inbound = bound_item.inbound, \
                        outbound = bound_item.outbound, \
                        balance = bound_item.balance, \
                        comment = bound_item.comment, \
                        created_at = self.convertIntoTimestamp(bound_item.created_at), \
                        updated_at = self.convertIntoTimestamp(bound_item.updated_at))

    def convertIntoTimestamp(self, old_date):
        ts = Timestamp()
        new_date = datetime.combine(old_date, datetime.min.time())
        ts.FromDateTime(new_date)
        return ts

    def convertIntoUUID(self, value):
        new_uuid = uuid()
        new_uuid.value = value
        return new_uuid
