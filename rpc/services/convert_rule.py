from app import app
from app.entity.convert_rule import ConvertRule
import grpc
import rpc.messages.convert_rule_pb2_grpc as convert_rule_service
import rpc.messages.convert_rule_pb2 as convert_rule_messages
from rpc.messages.type.uuid_pb2 as uuid
import logging
import time
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp

class ConvertRuleService(convert_rule_service.ConvertRuleServicer):
    def GetConvertRule(self, request, context):
        if request.id:
            with app.app_context(:
                convert_rule = ConvertRule.query_filter_by_id(id=request.id.value).one_or_none()
                logging.debug(convert_rule)

                if convert_rule:
                        return convert_rule.messages.ConvertRuleResponse(
                                id = self.convertIntoUUID(str(convert_rule.id)), \
                                default_amount = convert_rule.default_amount, \
                                status = convert_rule.status, \
                                created_at = self.convertIntoTimestamp(convert_rule.created_at), \
                                updated_at = self.convertIntoTimestamp(convert_rule.updated_at))

                msg = "Must pass ID Convert Rule."
                context.set_detail(msg)
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                return convert_rule.ConvertRuleResponse()

    def convertIntoTimestamp(self, old_date):
        ts = Timestamp()
        new_date = datetime.combine(old_date, datetime.min.time())
        ts.FromDateTime(new_date)
        return ts

    def convertIntoUUID(self, value):
        new_uuid = uuid()
        new_uuid.value = value
        return new_uuid