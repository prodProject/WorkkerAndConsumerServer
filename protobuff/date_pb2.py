# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: time.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='time.proto',
  package='protobuff',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ntime.proto\x12\tprotobuff\"3\n\x06\x44\x61tePb\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\x05\x12\r\n\x05month\x18\x02 \x01(\x05\x12\x0c\n\x04year\x18\x03 \x01(\x05\x62\x06proto3')
)




_DATEPB = _descriptor.Descriptor(
  name='DatePb',
  full_name='protobuff.DatePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='protobuff.DatePb.date', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month', full_name='protobuff.DatePb.month', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='year', full_name='protobuff.DatePb.year', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=25,
  serialized_end=76,
)

DESCRIPTOR.message_types_by_name['DatePb'] = _DATEPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DatePb = _reflection.GeneratedProtocolMessageType('DatePb', (_message.Message,), {
  'DESCRIPTOR' : _DATEPB,
  '__module__' : 'date_pb2'
  # @@protoc_insertion_point(class_scope:protobuff.DatePb)
  })
_sym_db.RegisterMessage(DatePb)


# @@protoc_insertion_point(module_scope)
