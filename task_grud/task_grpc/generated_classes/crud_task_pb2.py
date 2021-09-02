# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crud_task.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='crud_task.proto',
  package='task',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x63rud_task.proto\x12\x04task\"-\n\x0cGrpcTaskList\x12\x1d\n\x05tasks\x18\x01 \x03(\x0b\x32\x0e.task.GrpcTask\"G\n\x08GrpcTask\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03\x63id\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t2\xd2\x01\n\x0f\x43rudTaskService\x12*\n\x06insert\x12\x0e.task.GrpcTask\x1a\x0e.task.GrpcTask\"\x00\x12*\n\x06update\x12\x0e.task.GrpcTask\x1a\x0e.task.GrpcTask\"\x00\x12\x35\n\rsearch_by_cid\x12\x0e.task.GrpcTask\x1a\x12.task.GrpcTaskList\"\x00\x12\x30\n\x0c\x64\x65lete_by_id\x12\x0e.task.GrpcTask\x1a\x0e.task.GrpcTask\"\x00\x62\x06proto3'
)




_GRPCTASKLIST = _descriptor.Descriptor(
  name='GrpcTaskList',
  full_name='task.GrpcTaskList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tasks', full_name='task.GrpcTaskList.tasks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=25,
  serialized_end=70,
)


_GRPCTASK = _descriptor.Descriptor(
  name='GrpcTask',
  full_name='task.GrpcTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='task.GrpcTask.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cid', full_name='task.GrpcTask.cid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='task.GrpcTask.title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='task.GrpcTask.description', index=3,
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
  serialized_start=72,
  serialized_end=143,
)

_GRPCTASKLIST.fields_by_name['tasks'].message_type = _GRPCTASK
DESCRIPTOR.message_types_by_name['GrpcTaskList'] = _GRPCTASKLIST
DESCRIPTOR.message_types_by_name['GrpcTask'] = _GRPCTASK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GrpcTaskList = _reflection.GeneratedProtocolMessageType('GrpcTaskList', (_message.Message,), {
  'DESCRIPTOR' : _GRPCTASKLIST,
  '__module__' : 'crud_task_pb2'
  # @@protoc_insertion_point(class_scope:task.GrpcTaskList)
  })
_sym_db.RegisterMessage(GrpcTaskList)

GrpcTask = _reflection.GeneratedProtocolMessageType('GrpcTask', (_message.Message,), {
  'DESCRIPTOR' : _GRPCTASK,
  '__module__' : 'crud_task_pb2'
  # @@protoc_insertion_point(class_scope:task.GrpcTask)
  })
_sym_db.RegisterMessage(GrpcTask)



_CRUDTASKSERVICE = _descriptor.ServiceDescriptor(
  name='CrudTaskService',
  full_name='task.CrudTaskService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=146,
  serialized_end=356,
  methods=[
  _descriptor.MethodDescriptor(
    name='insert',
    full_name='task.CrudTaskService.insert',
    index=0,
    containing_service=None,
    input_type=_GRPCTASK,
    output_type=_GRPCTASK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='update',
    full_name='task.CrudTaskService.update',
    index=1,
    containing_service=None,
    input_type=_GRPCTASK,
    output_type=_GRPCTASK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='search_by_cid',
    full_name='task.CrudTaskService.search_by_cid',
    index=2,
    containing_service=None,
    input_type=_GRPCTASK,
    output_type=_GRPCTASKLIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='delete_by_id',
    full_name='task.CrudTaskService.delete_by_id',
    index=3,
    containing_service=None,
    input_type=_GRPCTASK,
    output_type=_GRPCTASK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CRUDTASKSERVICE)

DESCRIPTOR.services_by_name['CrudTaskService'] = _CRUDTASKSERVICE

# @@protoc_insertion_point(module_scope)
