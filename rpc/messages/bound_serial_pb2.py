# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bound_serial.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from type import uuid_pb2 as type_dot_uuid__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bound_serial.proto',
  package='inventory',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12\x62ound_serial.proto\x12\tinventory\x1a\x0ftype/uuid.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd6\x01\n\x12\x42oundSerialRequest\x12\x1b\n\x02id\x18\x01 \x01(\x0b\x32\x0f.inventory.uuid\x12\x0f\n\x07inbound\x18\x02 \x01(\x04\x12\x10\n\x08outbound\x18\x03 \x01(\x04\x12\x0f\n\x07\x62\x61lance\x18\x04 \x01(\x04\x12\x0f\n\x07\x63omment\x18\x05 \x01(\t\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xd7\x01\n\x13\x42oundSerialResponse\x12\x1b\n\x02id\x18\x01 \x01(\x0b\x32\x0f.inventory.uuid\x12\x0f\n\x07inbound\x18\x02 \x01(\x04\x12\x10\n\x08outbound\x18\x03 \x01(\x04\x12\x0f\n\x07\x62\x61lance\x18\x04 \x01(\x04\x12\x0f\n\x07\x63omment\x18\x05 \x01(\t\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp2\xb6\x01\n\x0b\x42oundSerial\x12Q\n\x0eGetBoundSerial\x12\x1d.inventory.BoundSerialRequest\x1a\x1e.inventory.BoundSerialResponse\"\x00\x12T\n\x0fGetBoundSerials\x12\x1d.inventory.BoundSerialRequest\x1a\x1e.inventory.BoundSerialResponse\"\x00\x30\x01\x62\x06proto3')
  ,
  dependencies=[type_dot_uuid__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_BOUNDSERIALREQUEST = _descriptor.Descriptor(
  name='BoundSerialRequest',
  full_name='inventory.BoundSerialRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='inventory.BoundSerialRequest.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inbound', full_name='inventory.BoundSerialRequest.inbound', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outbound', full_name='inventory.BoundSerialRequest.outbound', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='balance', full_name='inventory.BoundSerialRequest.balance', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comment', full_name='inventory.BoundSerialRequest.comment', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='inventory.BoundSerialRequest.created_at', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='inventory.BoundSerialRequest.updated_at', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=298,
)


_BOUNDSERIALRESPONSE = _descriptor.Descriptor(
  name='BoundSerialResponse',
  full_name='inventory.BoundSerialResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='inventory.BoundSerialResponse.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inbound', full_name='inventory.BoundSerialResponse.inbound', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outbound', full_name='inventory.BoundSerialResponse.outbound', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='balance', full_name='inventory.BoundSerialResponse.balance', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comment', full_name='inventory.BoundSerialResponse.comment', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='inventory.BoundSerialResponse.created_at', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='inventory.BoundSerialResponse.updated_at', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=301,
  serialized_end=516,
)

_BOUNDSERIALREQUEST.fields_by_name['id'].message_type = type_dot_uuid__pb2._UUID
_BOUNDSERIALREQUEST.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BOUNDSERIALREQUEST.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BOUNDSERIALRESPONSE.fields_by_name['id'].message_type = type_dot_uuid__pb2._UUID
_BOUNDSERIALRESPONSE.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BOUNDSERIALRESPONSE.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['BoundSerialRequest'] = _BOUNDSERIALREQUEST
DESCRIPTOR.message_types_by_name['BoundSerialResponse'] = _BOUNDSERIALRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BoundSerialRequest = _reflection.GeneratedProtocolMessageType('BoundSerialRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOUNDSERIALREQUEST,
  '__module__' : 'bound_serial_pb2'
  # @@protoc_insertion_point(class_scope:inventory.BoundSerialRequest)
  })
_sym_db.RegisterMessage(BoundSerialRequest)

BoundSerialResponse = _reflection.GeneratedProtocolMessageType('BoundSerialResponse', (_message.Message,), {
  'DESCRIPTOR' : _BOUNDSERIALRESPONSE,
  '__module__' : 'bound_serial_pb2'
  # @@protoc_insertion_point(class_scope:inventory.BoundSerialResponse)
  })
_sym_db.RegisterMessage(BoundSerialResponse)



_BOUNDSERIAL = _descriptor.ServiceDescriptor(
  name='BoundSerial',
  full_name='inventory.BoundSerial',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=519,
  serialized_end=701,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetBoundSerial',
    full_name='inventory.BoundSerial.GetBoundSerial',
    index=0,
    containing_service=None,
    input_type=_BOUNDSERIALREQUEST,
    output_type=_BOUNDSERIALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetBoundSerials',
    full_name='inventory.BoundSerial.GetBoundSerials',
    index=1,
    containing_service=None,
    input_type=_BOUNDSERIALREQUEST,
    output_type=_BOUNDSERIALRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BOUNDSERIAL)

DESCRIPTOR.services_by_name['BoundSerial'] = _BOUNDSERIAL

# @@protoc_insertion_point(module_scope)