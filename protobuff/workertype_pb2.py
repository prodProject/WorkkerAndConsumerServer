# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: workertype.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import entity_pb2 as entity__pb2
import names_pb2 as names__pb2
import summary_pb2 as summary__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='workertype.proto',
  package='protobuff',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10workertype.proto\x12\tprotobuff\x1a\x0c\x65ntity.proto\x1a\x0bnames.proto\x1a\rsummary.proto\"\x8a\x01\n\x0cWorkerTypePb\x12#\n\x06\x64\x62Info\x18\x01 \x01(\x0b\x32\x13.protobuff.EntityPb\x12-\n\nworkerType\x18\x02 \x01(\x0e\x32\x19.protobuff.WorkerTypeEnum\x12&\n\ncategories\x18\x03 \x03(\x0b\x32\x12.protobuff.NamesPb\"o\n\x19WorkerTypeSearchRequestPb\x12#\n\x06\x64\x62Info\x18\x01 \x01(\x0b\x32\x13.protobuff.EntityPb\x12-\n\nworkerType\x18\x02 \x01(\x0e\x32\x19.protobuff.WorkerTypeEnum\"m\n\x1aWorkerTypeSearchResponsePb\x12%\n\x07summary\x18\x01 \x01(\x0b\x32\x14.protobuff.SummaryPb\x12(\n\x07results\x18\x02 \x03(\x0b\x32\x17.protobuff.WorkerTypePb*\xe2\x01\n\x0eWorkerTypeEnum\x12\x17\n\x13UNKNOWN_WORKER_TYPE\x10\x00\x12\x0f\n\x0b\x43ONSTRUCTOR\x10\x01\x12\x0f\n\x0b\x45LECTRICIAN\x10\x02\x12\x0c\n\x08PAINTING\x10\x03\x12\x0c\n\x08\x43LEANING\x10\x04\x12\x0c\n\x08PLUMBING\x10\x05\x12\x08\n\x04MAID\x10\x06\x12\r\n\tCARPENTER\x10\x07\x12\x1d\n\x19LAUNDARY_AND_DRY_CLEANING\x10\x08\x12\x10\n\x0cPEST_CONTROL\x10\t\x12\x16\n\x12PACKERS_AND_MOVERS\x10\n\x12\t\n\x05SALON\x10\x0b\x62\x06proto3')
  ,
  dependencies=[entity__pb2.DESCRIPTOR,names__pb2.DESCRIPTOR,summary__pb2.DESCRIPTOR,])

_WORKERTYPEENUM = _descriptor.EnumDescriptor(
  name='WorkerTypeEnum',
  full_name='protobuff.WorkerTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_WORKER_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONSTRUCTOR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ELECTRICIAN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAINTING', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLEANING', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLUMBING', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAID', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CARPENTER', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LAUNDARY_AND_DRY_CLEANING', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PEST_CONTROL', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKERS_AND_MOVERS', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SALON', index=11, number=11,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=439,
  serialized_end=665,
)
_sym_db.RegisterEnumDescriptor(_WORKERTYPEENUM)

WorkerTypeEnum = enum_type_wrapper.EnumTypeWrapper(_WORKERTYPEENUM)
UNKNOWN_WORKER_TYPE = 0
CONSTRUCTOR = 1
ELECTRICIAN = 2
PAINTING = 3
CLEANING = 4
PLUMBING = 5
MAID = 6
CARPENTER = 7
LAUNDARY_AND_DRY_CLEANING = 8
PEST_CONTROL = 9
PACKERS_AND_MOVERS = 10
SALON = 11



_WORKERTYPEPB = _descriptor.Descriptor(
  name='WorkerTypePb',
  full_name='protobuff.WorkerTypePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbInfo', full_name='protobuff.WorkerTypePb.dbInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workerType', full_name='protobuff.WorkerTypePb.workerType', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='categories', full_name='protobuff.WorkerTypePb.categories', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=74,
  serialized_end=212,
)


_WORKERTYPESEARCHREQUESTPB = _descriptor.Descriptor(
  name='WorkerTypeSearchRequestPb',
  full_name='protobuff.WorkerTypeSearchRequestPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbInfo', full_name='protobuff.WorkerTypeSearchRequestPb.dbInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workerType', full_name='protobuff.WorkerTypeSearchRequestPb.workerType', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=214,
  serialized_end=325,
)


_WORKERTYPESEARCHRESPONSEPB = _descriptor.Descriptor(
  name='WorkerTypeSearchResponsePb',
  full_name='protobuff.WorkerTypeSearchResponsePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='summary', full_name='protobuff.WorkerTypeSearchResponsePb.summary', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='protobuff.WorkerTypeSearchResponsePb.results', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=327,
  serialized_end=436,
)

_WORKERTYPEPB.fields_by_name['dbInfo'].message_type = entity__pb2._ENTITYPB
_WORKERTYPEPB.fields_by_name['workerType'].enum_type = _WORKERTYPEENUM
_WORKERTYPEPB.fields_by_name['categories'].message_type = names__pb2._NAMESPB
_WORKERTYPESEARCHREQUESTPB.fields_by_name['dbInfo'].message_type = entity__pb2._ENTITYPB
_WORKERTYPESEARCHREQUESTPB.fields_by_name['workerType'].enum_type = _WORKERTYPEENUM
_WORKERTYPESEARCHRESPONSEPB.fields_by_name['summary'].message_type = summary__pb2._SUMMARYPB
_WORKERTYPESEARCHRESPONSEPB.fields_by_name['results'].message_type = _WORKERTYPEPB
DESCRIPTOR.message_types_by_name['WorkerTypePb'] = _WORKERTYPEPB
DESCRIPTOR.message_types_by_name['WorkerTypeSearchRequestPb'] = _WORKERTYPESEARCHREQUESTPB
DESCRIPTOR.message_types_by_name['WorkerTypeSearchResponsePb'] = _WORKERTYPESEARCHRESPONSEPB
DESCRIPTOR.enum_types_by_name['WorkerTypeEnum'] = _WORKERTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WorkerTypePb = _reflection.GeneratedProtocolMessageType('WorkerTypePb', (_message.Message,), {
  'DESCRIPTOR' : _WORKERTYPEPB,
  '__module__' : 'workertype_pb2'
  # @@protoc_insertion_point(class_scope:protobuff.WorkerTypePb)
  })
_sym_db.RegisterMessage(WorkerTypePb)

WorkerTypeSearchRequestPb = _reflection.GeneratedProtocolMessageType('WorkerTypeSearchRequestPb', (_message.Message,), {
  'DESCRIPTOR' : _WORKERTYPESEARCHREQUESTPB,
  '__module__' : 'workertype_pb2'
  # @@protoc_insertion_point(class_scope:protobuff.WorkerTypeSearchRequestPb)
  })
_sym_db.RegisterMessage(WorkerTypeSearchRequestPb)

WorkerTypeSearchResponsePb = _reflection.GeneratedProtocolMessageType('WorkerTypeSearchResponsePb', (_message.Message,), {
  'DESCRIPTOR' : _WORKERTYPESEARCHRESPONSEPB,
  '__module__' : 'workertype_pb2'
  # @@protoc_insertion_point(class_scope:protobuff.WorkerTypeSearchResponsePb)
  })
_sym_db.RegisterMessage(WorkerTypeSearchResponsePb)


# @@protoc_insertion_point(module_scope)
