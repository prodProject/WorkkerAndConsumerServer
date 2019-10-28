# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: workersearch.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import entity_pb2 as entity__pb2
import summary_pb2 as summary__pb2
import worker_pb2 as worker__pb2
import mobile_pb2 as mobile__pb2
import contactdetails_pb2 as contactdetails__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='workersearch.proto',
  package='protobuff',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12workersearch.proto\x12\tprotobuff\x1a\x0c\x65ntity.proto\x1a\rsummary.proto\x1a\x0cworker.proto\x1a\x0cmobile.proto\x1a\x14\x63ontactdetails.proto\"\x9c\x01\n\x15WorkerSearchRequestPb\x12\'\n\x08lifeTime\x18\x01 \x01(\x0e\x32\x15.protobuff.StatusEnum\x12\x33\n\x0e\x63ontactDetails\x18\x02 \x01(\x0b\x32\x1b.protobuff.ContactDetailsPb\x12%\n\x08mobileNo\x18\x03 \x01(\x0b\x32\x13.protobuff.MobilePb\"e\n\x16WorkerSearchResponsePb\x12%\n\x07summary\x18\x01 \x01(\x0b\x32\x14.protobuff.SummaryPb\x12$\n\x07results\x18\x02 \x03(\x0b\x32\x13.protobuff.WorkerPbb\x06proto3')
  ,
  dependencies=[entity__pb2.DESCRIPTOR,summary__pb2.DESCRIPTOR,worker__pb2.DESCRIPTOR,mobile__pb2.DESCRIPTOR,contactdetails__pb2.DESCRIPTOR,])




_WORKERSEARCHREQUESTPB = _descriptor.Descriptor(
  name='WorkerSearchRequestPb',
  full_name='protobuff.WorkerSearchRequestPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lifeTime', full_name='protobuff.WorkerSearchRequestPb.lifeTime', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contactDetails', full_name='protobuff.WorkerSearchRequestPb.contactDetails', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mobileNo', full_name='protobuff.WorkerSearchRequestPb.mobileNo', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=113,
  serialized_end=269,
)


_WORKERSEARCHRESPONSEPB = _descriptor.Descriptor(
  name='WorkerSearchResponsePb',
  full_name='protobuff.WorkerSearchResponsePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='summary', full_name='protobuff.WorkerSearchResponsePb.summary', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='protobuff.WorkerSearchResponsePb.results', index=1,
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
  serialized_start=271,
  serialized_end=372,
)

_WORKERSEARCHREQUESTPB.fields_by_name['lifeTime'].enum_type = entity__pb2._STATUSENUM
_WORKERSEARCHREQUESTPB.fields_by_name['contactDetails'].message_type = contactdetails__pb2._CONTACTDETAILSPB
_WORKERSEARCHREQUESTPB.fields_by_name['mobileNo'].message_type = mobile__pb2._MOBILEPB
_WORKERSEARCHRESPONSEPB.fields_by_name['summary'].message_type = summary__pb2._SUMMARYPB
_WORKERSEARCHRESPONSEPB.fields_by_name['results'].message_type = worker__pb2._WORKERPB
DESCRIPTOR.message_types_by_name['WorkerSearchRequestPb'] = _WORKERSEARCHREQUESTPB
DESCRIPTOR.message_types_by_name['WorkerSearchResponsePb'] = _WORKERSEARCHRESPONSEPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WorkerSearchRequestPb = _reflection.GeneratedProtocolMessageType('WorkerSearchRequestPb', (_message.Message,), {
  'DESCRIPTOR' : _WORKERSEARCHREQUESTPB,
  '__module__' : 'workersearch_pb2'
  # @@protoc_insertion_point(class_scope:protobuff.WorkerSearchRequestPb)
  })
_sym_db.RegisterMessage(WorkerSearchRequestPb)

WorkerSearchResponsePb = _reflection.GeneratedProtocolMessageType('WorkerSearchResponsePb', (_message.Message,), {
  'DESCRIPTOR' : _WORKERSEARCHRESPONSEPB,
  '__module__' : 'workersearch_pb2'
  # @@protoc_insertion_point(class_scope:protobuff.WorkerSearchResponsePb)
  })
_sym_db.RegisterMessage(WorkerSearchResponsePb)


# @@protoc_insertion_point(module_scope)
