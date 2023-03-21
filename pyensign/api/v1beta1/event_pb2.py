# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1beta1/event.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mimetype.v1beta1 import mimetype_pb2 as mimetype_dot_v1beta1_dot_mimetype__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x61pi/v1beta1/event.proto\x12\x0e\x65nsign.v1beta1\x1a\x1fmimetype/v1beta1/mimetype.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xbe\x03\n\x05\x45vent\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08topic_id\x18\x02 \x01(\t\x12(\n\x08mimetype\x18\x03 \x01(\x0e\x32\x16.mimetype.v1beta1.MIME\x12\"\n\x04type\x18\x04 \x01(\x0b\x32\x14.ensign.v1beta1.Type\x12\x0b\n\x03key\x18\x05 \x01(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x06 \x01(\x0c\x12.\n\nencryption\x18\x07 \x01(\x0b\x32\x1a.ensign.v1beta1.Encryption\x12\x30\n\x0b\x63ompression\x18\x08 \x01(\x0b\x32\x1b.ensign.v1beta1.Compression\x12)\n\tgeography\x18\t \x01(\x0b\x32\x16.ensign.v1beta1.Region\x12,\n\tpublisher\x18\n \x01(\x0b\x32\x19.ensign.v1beta1.Publisher\x12\x17\n\x0fuser_defined_id\x18\x0b \x01(\t\x12+\n\x07\x63reated\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tcommitted\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"%\n\x04Type\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\r\"/\n\nEncryption\x12\x11\n\talgorithm\x18\x01 \x01(\t\x12\x0e\n\x06key_id\x18\x02 \x01(\t\" \n\x0b\x43ompression\x12\x11\n\talgorithm\x18\x02 \x01(\t\"\x16\n\x06Region\x12\x0c\n\x04name\x18\x01 \x01(\t\".\n\tPublisher\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x0e\n\x06ipaddr\x18\x02 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1beta1.event_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EVENT._serialized_start=110
  _EVENT._serialized_end=556
  _TYPE._serialized_start=558
  _TYPE._serialized_end=595
  _ENCRYPTION._serialized_start=597
  _ENCRYPTION._serialized_end=644
  _COMPRESSION._serialized_start=646
  _COMPRESSION._serialized_end=678
  _REGION._serialized_start=680
  _REGION._serialized_end=702
  _PUBLISHER._serialized_start=704
  _PUBLISHER._serialized_end=750
# @@protoc_insertion_point(module_scope)