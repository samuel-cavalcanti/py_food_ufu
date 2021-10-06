# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crud_client.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='crud_client.proto',
  package='client',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x63rud_client.proto\x12\x06\x63lient\"J\n\nGrpcClient\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x63pf\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x15\n\rfavorite_food\x18\x04 \x01(\t2\xef\x01\n\x11\x43rudClientService\x12\x32\n\x06insert\x12\x12.client.GrpcClient\x1a\x12.client.GrpcClient\"\x00\x12\x32\n\x06update\x12\x12.client.GrpcClient\x1a\x12.client.GrpcClient\"\x00\x12\x38\n\x0csearch_by_id\x12\x12.client.GrpcClient\x1a\x12.client.GrpcClient\"\x00\x12\x38\n\x0c\x64\x65lete_by_id\x12\x12.client.GrpcClient\x1a\x12.client.GrpcClient\"\x00\x62\x06proto3'
)




_GRPCCLIENT = _descriptor.Descriptor(
  name='GrpcClient',
  full_name='client.GrpcClient',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='client.GrpcClient.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cpf', full_name='client.GrpcClient.cpf', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='client.GrpcClient.id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='favorite_food', full_name='client.GrpcClient.favorite_food', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_end=103,
)

DESCRIPTOR.message_types_by_name['GrpcClient'] = _GRPCCLIENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GrpcClient = _reflection.GeneratedProtocolMessageType('GrpcClient', (_message.Message,), {
  'DESCRIPTOR' : _GRPCCLIENT,
  '__module__' : 'crud_client_pb2'
  # @@protoc_insertion_point(class_scope:client.GrpcClient)
  })
_sym_db.RegisterMessage(GrpcClient)



_CRUDCLIENTSERVICE = _descriptor.ServiceDescriptor(
  name='CrudClientService',
  full_name='client.CrudClientService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=106,
  serialized_end=345,
  methods=[
  _descriptor.MethodDescriptor(
    name='insert',
    full_name='client.CrudClientService.insert',
    index=0,
    containing_service=None,
    input_type=_GRPCCLIENT,
    output_type=_GRPCCLIENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='update',
    full_name='client.CrudClientService.update',
    index=1,
    containing_service=None,
    input_type=_GRPCCLIENT,
    output_type=_GRPCCLIENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='search_by_id',
    full_name='client.CrudClientService.search_by_id',
    index=2,
    containing_service=None,
    input_type=_GRPCCLIENT,
    output_type=_GRPCCLIENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='delete_by_id',
    full_name='client.CrudClientService.delete_by_id',
    index=3,
    containing_service=None,
    input_type=_GRPCCLIENT,
    output_type=_GRPCCLIENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CRUDCLIENTSERVICE)

DESCRIPTOR.services_by_name['CrudClientService'] = _CRUDCLIENTSERVICE

# @@protoc_insertion_point(module_scope)