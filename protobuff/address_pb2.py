# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: address.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='address.proto',
  package='protobuff',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\raddress.proto\x12\tprotobuff\"\xb8\x01\n\tAddressPb\x12%\n\x07latlong\x18\x01 \x01(\x0b\x32\x14.protobuff.LatLongPb\x12\x0f\n\x07houseNo\x18\x02 \x01(\t\x12\x14\n\x0cstreetOrRoad\x18\x03 \x01(\t\x12\x0c\n\x04\x61rea\x18\x04 \x01(\t\x12\x10\n\x08landmark\x18\x05 \x01(\t\x12\x0c\n\x04\x63ity\x18\x06 \x01(\t\x12\r\n\x05state\x18\x07 \x01(\t\x12\x0f\n\x07pincode\x18\x08 \x01(\t\x12\x0f\n\x07\x63ountry\x18\t \x01(\t\"0\n\tLatLongPb\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x62\x06proto3')
)




_ADDRESSPB = _descriptor.Descriptor(
  name='AddressPb',
  full_name='protobuff.AddressPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latlong', full_name='protobuff.AddressPb.latlong', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='houseNo', full_name='protobuff.AddressPb.houseNo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='streetOrRoad', full_name='protobuff.AddressPb.streetOrRoad', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='area', full_name='protobuff.AddressPb.area', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='landmark', full_name='protobuff.AddressPb.landmark', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='city', full_name='protobuff.AddressPb.city', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='protobuff.AddressPb.state', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pincode', full_name='protobuff.AddressPb.pincode', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='country', full_name='protobuff.AddressPb.country', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=29,
  serialized_end=213,
)


_LATLONGPB = _descriptor.Descriptor(
  name='LatLongPb',
  full_name='protobuff.LatLongPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='protobuff.LatLongPb.latitude', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='protobuff.LatLongPb.longitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=215,
  serialized_end=263,
)

_ADDRESSPB.fields_by_name['latlong'].message_type = _LATLONGPB
DESCRIPTOR.message_types_by_name['AddressPb'] = _ADDRESSPB
DESCRIPTOR.message_types_by_name['LatLongPb'] = _LATLONGPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddressPb = _reflection.GeneratedProtocolMessageType('AddressPb', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESSPB,
  '__module__' : 'address_pb2'
  # @@protoc_insertion_point(class_scope:protobuff.AddressPb)
  })
_sym_db.RegisterMessage(AddressPb)

LatLongPb = _reflection.GeneratedProtocolMessageType('LatLongPb', (_message.Message,), {
  'DESCRIPTOR' : _LATLONGPB,
  '__module__' : 'address_pb2'
  # @@protoc_insertion_point(class_scope:protobuff.LatLongPb)
  })
_sym_db.RegisterMessage(LatLongPb)


# @@protoc_insertion_point(module_scope)
