# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bound.proto

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
  name='bound.proto',
  package='inventory',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0b\x62ound.proto\x12\tinventory\x1a\x0ftype/uuid.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xbe\x01\n\x0c\x42oundRequest\x12\x1b\n\x02id\x18\x01 \x01(\x0b\x32\x0f.inventory.uuid\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xbf\x01\n\rBoundResponse\x12\x1b\n\x02id\x18\x01 \x01(\x0b\x32\x0f.inventory.uuid\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp2\x8c\x01\n\x05\x42ound\x12?\n\x08GetBound\x12\x17.inventory.BoundRequest\x1a\x18.inventory.BoundResponse\"\x00\x12\x42\n\tGetBounds\x12\x17.inventory.BoundRequest\x1a\x18.inventory.BoundResponse\"\x00\x30\x01\x62\x06proto3')
  ,
  dependencies=[type_dot_uuid__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_BOUNDREQUEST = _descriptor.Descriptor(
  name='BoundRequest',
  full_name='inventory.BoundRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='inventory.BoundRequest.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='inventory.BoundRequest.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='inventory.BoundRequest.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='inventory.BoundRequest.status', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='inventory.BoundRequest.created_at', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='inventory.BoundRequest.updated_at', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=77,
  serialized_end=267,
)


_BOUNDRESPONSE = _descriptor.Descriptor(
  name='BoundResponse',
  full_name='inventory.BoundResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='inventory.BoundResponse.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='inventory.BoundResponse.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='inventory.BoundResponse.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='inventory.BoundResponse.status', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='inventory.BoundResponse.created_at', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='inventory.BoundResponse.updated_at', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=270,
  serialized_end=461,
)

_BOUNDREQUEST.fields_by_name['id'].message_type = type_dot_uuid__pb2._UUID
_BOUNDREQUEST.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BOUNDREQUEST.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BOUNDRESPONSE.fields_by_name['id'].message_type = type_dot_uuid__pb2._UUID
_BOUNDRESPONSE.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BOUNDRESPONSE.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['BoundRequest'] = _BOUNDREQUEST
DESCRIPTOR.message_types_by_name['BoundResponse'] = _BOUNDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BoundRequest = _reflection.GeneratedProtocolMessageType('BoundRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOUNDREQUEST,
  '__module__' : 'bound_pb2'
  # @@protoc_insertion_point(class_scope:inventory.BoundRequest)
  })
_sym_db.RegisterMessage(BoundRequest)

BoundResponse = _reflection.GeneratedProtocolMessageType('BoundResponse', (_message.Message,), {
  'DESCRIPTOR' : _BOUNDRESPONSE,
  '__module__' : 'bound_pb2'
  # @@protoc_insertion_point(class_scope:inventory.BoundResponse)
  })
_sym_db.RegisterMessage(BoundResponse)



_BOUND = _descriptor.ServiceDescriptor(
  name='Bound',
  full_name='inventory.Bound',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=464,
  serialized_end=604,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetBound',
    full_name='inventory.Bound.GetBound',
    index=0,
    containing_service=None,
    input_type=_BOUNDREQUEST,
    output_type=_BOUNDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetBounds',
    full_name='inventory.Bound.GetBounds',
    index=1,
    containing_service=None,
    input_type=_BOUNDREQUEST,
    output_type=_BOUNDRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BOUND)

DESCRIPTOR.services_by_name['Bound'] = _BOUND

# @@protoc_insertion_point(module_scope)