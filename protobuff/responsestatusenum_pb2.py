# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: responsestatusenum.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='responsestatusenum.proto',
  package='protobuff',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18responsestatusenum.proto\x12\tprotobuff\"B\n\x0eResponseTypePb\x12\x30\n\nstatusType\x18\x01 \x01(\x0e\x32\x1c.protobuff.ResponseSatusEnum*\x8d\x01\n\x11ResponseSatusEnum\x12\x1b\n\x17UNKNOWN_RESPONSE_STATUS\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\n\n\x06\x46\x41ILED\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\x0e\n\nUSER_EXIST\x10\x04\x12\x16\n\x12USER_NOT_REGISTRED\x10\x05\x12\x0f\n\x0bUNEXP_ERROR\x10\x06\x62\x06proto3')
)

_RESPONSESATUSENUM = _descriptor.EnumDescriptor(
  name='ResponseSatusEnum',
  full_name='protobuff.ResponseSatusEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_RESPONSE_STATUS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_EXIST', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_NOT_REGISTRED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNEXP_ERROR', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=108,
  serialized_end=249,
)
_sym_db.RegisterEnumDescriptor(_RESPONSESATUSENUM)

ResponseSatusEnum = enum_type_wrapper.EnumTypeWrapper(_RESPONSESATUSENUM)
UNKNOWN_RESPONSE_STATUS = 0
SUCCESS = 1
FAILED = 2
ERROR = 3
USER_EXIST = 4
USER_NOT_REGISTRED = 5
UNEXP_ERROR = 6



_RESPONSETYPEPB = _descriptor.Descriptor(
  name='ResponseTypePb',
  full_name='protobuff.ResponseTypePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='statusType', full_name='protobuff.ResponseTypePb.statusType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=39,
  serialized_end=105,
)

_RESPONSETYPEPB.fields_by_name['statusType'].enum_type = _RESPONSESATUSENUM
DESCRIPTOR.message_types_by_name['ResponseTypePb'] = _RESPONSETYPEPB
DESCRIPTOR.enum_types_by_name['ResponseSatusEnum'] = _RESPONSESATUSENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResponseTypePb = _reflection.GeneratedProtocolMessageType('ResponseTypePb', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSETYPEPB,
  '__module__' : 'responsestatusenum_pb2'
  # @@protoc_insertion_point(class_scope:protobuff.ResponseTypePb)
  })
_sym_db.RegisterMessage(ResponseTypePb)


# @@protoc_insertion_point(module_scope)
