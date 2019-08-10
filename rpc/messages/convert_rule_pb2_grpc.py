# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import convert_rule_pb2 as convert__rule__pb2


class ConvertRuleStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetConvertRule = channel.unary_unary(
        '/inventory.ConvertRule/GetConvertRule',
        request_serializer=convert__rule__pb2.ConvertRuleRequest.SerializeToString,
        response_deserializer=convert__rule__pb2.ConvertRuleResponse.FromString,
        )
    self.GetConvertRules = channel.unary_unary(
        '/inventory.ConvertRule/GetConvertRules',
        request_serializer=convert__rule__pb2.ConvertRuleRequest.SerializeToString,
        response_deserializer=convert__rule__pb2.ConvertRuleResponse.FromString,
        )


class ConvertRuleServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetConvertRule(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetConvertRules(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ConvertRuleServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetConvertRule': grpc.unary_unary_rpc_method_handler(
          servicer.GetConvertRule,
          request_deserializer=convert__rule__pb2.ConvertRuleRequest.FromString,
          response_serializer=convert__rule__pb2.ConvertRuleResponse.SerializeToString,
      ),
      'GetConvertRules': grpc.unary_unary_rpc_method_handler(
          servicer.GetConvertRules,
          request_deserializer=convert__rule__pb2.ConvertRuleRequest.FromString,
          response_serializer=convert__rule__pb2.ConvertRuleResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'inventory.ConvertRule', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))