# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: federated.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x66\x65\x64\x65rated.proto\"\x1e\n\x0bLocalUpdate\x12\x0f\n\x07weights\x18\x01 \x01(\x0c\"!\n\x0eServerResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x07\n\x05\x45mpty\"\x1e\n\x0bGlobalModel\x12\x0f\n\x07weights\x18\x01 \x01(\x0c\x32m\n\x11\x46\x65\x64\x65ratedLearning\x12\x30\n\x0fSendLocalUpdate\x12\x0c.LocalUpdate\x1a\x0f.ServerResponse\x12&\n\x0eGetGlobalModel\x12\x06.Empty\x1a\x0c.GlobalModelb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'federated_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_LOCALUPDATE']._serialized_start=19
  _globals['_LOCALUPDATE']._serialized_end=49
  _globals['_SERVERRESPONSE']._serialized_start=51
  _globals['_SERVERRESPONSE']._serialized_end=84
  _globals['_EMPTY']._serialized_start=86
  _globals['_EMPTY']._serialized_end=93
  _globals['_GLOBALMODEL']._serialized_start=95
  _globals['_GLOBALMODEL']._serialized_end=125
  _globals['_FEDERATEDLEARNING']._serialized_start=127
  _globals['_FEDERATEDLEARNING']._serialized_end=236
# @@protoc_insertion_point(module_scope)
