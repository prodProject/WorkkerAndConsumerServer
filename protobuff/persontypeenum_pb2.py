# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: persontypeenum.proto

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
  name='persontypeenum.proto',
  package='protobuff',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14persontypeenum.proto\x12\tprotobuff\"=\n\x0cPersonTypePb\x12-\n\npersonType\x18\x01 \x01(\x0e\x32\x19.protobuff.PersonTypeEnum*C\n\x0ePersonTypeEnum\x12\x17\n\x13UNKNOWN_PERSON_TYPE\x10\x00\x12\n\n\x06WORKER\x10\x01\x12\x0c\n\x08\x43ONSUMER\x10\x02\x62\x06proto3')
)

_PERSONTYPEENUM = _descriptor.EnumDescriptor(
  name='PersonTypeEnum',
  full_name='protobuff.PersonTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_PERSON_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORKER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONSUMER', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=98,
  serialized_end=165,
)
_sym_db.RegisterEnumDescriptor(_PERSONTYPEENUM)

PersonTypeEnum = enum_type_wrapper.EnumTypeWrapper(_PERSONTYPEENUM)
UNKNOWN_PERSON_TYPE = 0
WORKER = 1
CONSUMER = 2



_PERSONTYPEPB = _descriptor.Descriptor(
  name='PersonTypePb',
  full_name='protobuff.PersonTypePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='personType', full_name='protobuff.PersonTypePb.personType', index=0,
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
  serialized_start=35,
  serialized_end=96,
)

_PERSONTYPEPB.fields_by_name['personType'].enum_type = _PERSONTYPEENUM
DESCRIPTOR.message_types_by_name['PersonTypePb'] = _PERSONTYPEPB
DESCRIPTOR.enum_types_by_name['PersonTypeEnum'] = _PERSONTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PersonTypePb = _reflection.GeneratedProtocolMessageType('PersonTypePb', (_message.Message,), {
  'DESCRIPTOR' : _PERSONTYPEPB,
  '__module__' : 'persontypeenum_pb2'
  # @@protoc_insertion_point(class_scope:protobuff.PersonTypePb)
  })
_sym_db.RegisterMessage(PersonTypePb)


# @@protoc_insertion_point(module_scope)
