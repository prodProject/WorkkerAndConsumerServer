# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: time.proto

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
  name='time.proto',
  package='protobuff',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ntime.proto\x12\tprotobuff\"\x8b\x01\n\x06TimePb\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\r\n\x05month\x18\x02 \x01(\t\x12\x0c\n\x04year\x18\x03 \x01(\t\x12\x14\n\x0cmilliseconds\x18\x04 \x01(\x03\x12\x15\n\rformattedDate\x18\x05 \x01(\t\x12)\n\x08timezone\x18\x06 \x01(\x0e\x32\x17.protobuff.TimeZoneEnum*7\n\x0cTimeZoneEnum\x12\x15\n\x11UNKNOWN_TIME_ZONE\x10\x00\x12\x07\n\x03IST\x10\x01\x12\x07\n\x03UTC\x10\x02\x62\x06proto3')
)

_TIMEZONEENUM = _descriptor.EnumDescriptor(
  name='TimeZoneEnum',
  full_name='protobuff.TimeZoneEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_TIME_ZONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IST', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UTC', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=167,
  serialized_end=222,
)
_sym_db.RegisterEnumDescriptor(_TIMEZONEENUM)

TimeZoneEnum = enum_type_wrapper.EnumTypeWrapper(_TIMEZONEENUM)
UNKNOWN_TIME_ZONE = 0
IST = 1
UTC = 2



_TIMEPB = _descriptor.Descriptor(
  name='TimePb',
  full_name='protobuff.TimePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='protobuff.TimePb.date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month', full_name='protobuff.TimePb.month', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='year', full_name='protobuff.TimePb.year', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='milliseconds', full_name='protobuff.TimePb.milliseconds', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='formattedDate', full_name='protobuff.TimePb.formattedDate', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timezone', full_name='protobuff.TimePb.timezone', index=5,
      number=6, type=14, cpp_type=8, label=1,
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
  serialized_start=26,
  serialized_end=165,
)

_TIMEPB.fields_by_name['timezone'].enum_type = _TIMEZONEENUM
DESCRIPTOR.message_types_by_name['TimePb'] = _TIMEPB
DESCRIPTOR.enum_types_by_name['TimeZoneEnum'] = _TIMEZONEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TimePb = _reflection.GeneratedProtocolMessageType('TimePb', (_message.Message,), {
  'DESCRIPTOR' : _TIMEPB,
  '__module__' : 'time_pb2'
  # @@protoc_insertion_point(class_scope:protobuff.TimePb)
  })
_sym_db.RegisterMessage(TimePb)


# @@protoc_insertion_point(module_scope)
