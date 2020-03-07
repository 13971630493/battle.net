# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bnet/rpc_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bnet/rpc_config.proto',
  package='bnet.protocol.config',
  serialized_pb=_b('\n\x15\x62net/rpc_config.proto\x12\x14\x62net.protocol.config\"\xa7\x02\n\x0fRPCMethodConfig\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x13\n\x0bmethod_name\x18\x02 \x01(\t\x12\x1a\n\x0f\x66ixed_call_cost\x18\x03 \x01(\r:\x01\x31\x12\x1c\n\x11\x66ixed_packet_size\x18\x04 \x01(\r:\x01\x30\x12\x1e\n\x13variable_multiplier\x18\x05 \x01(\x02:\x01\x30\x12\x15\n\nmultiplier\x18\x06 \x01(\x02:\x01\x31\x12\x18\n\x10rate_limit_count\x18\x07 \x01(\r\x12\x1a\n\x12rate_limit_seconds\x18\x08 \x01(\r\x12\x17\n\x0fmax_packet_size\x18\t \x01(\r\x12\x18\n\x10max_encoded_size\x18\n \x01(\r\x12\x0f\n\x07timeout\x18\x0b \x01(\x02\"\xae\x01\n\x0eRPCMeterConfig\x12\x35\n\x06method\x18\x01 \x03(\x0b\x32%.bnet.protocol.config.RPCMethodConfig\x12\x1c\n\x11income_per_second\x18\x02 \x01(\r:\x01\x31\x12\x17\n\x0finitial_balance\x18\x03 \x01(\r\x12\x13\n\x0b\x63\x61p_balance\x18\x04 \x01(\r\x12\x19\n\x0estartup_period\x18\x05 \x01(\x02:\x01\x30')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RPCMETHODCONFIG = _descriptor.Descriptor(
  name='RPCMethodConfig',
  full_name='bnet.protocol.config.RPCMethodConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_name', full_name='bnet.protocol.config.RPCMethodConfig.service_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='method_name', full_name='bnet.protocol.config.RPCMethodConfig.method_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fixed_call_cost', full_name='bnet.protocol.config.RPCMethodConfig.fixed_call_cost', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fixed_packet_size', full_name='bnet.protocol.config.RPCMethodConfig.fixed_packet_size', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variable_multiplier', full_name='bnet.protocol.config.RPCMethodConfig.variable_multiplier', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='multiplier', full_name='bnet.protocol.config.RPCMethodConfig.multiplier', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rate_limit_count', full_name='bnet.protocol.config.RPCMethodConfig.rate_limit_count', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rate_limit_seconds', full_name='bnet.protocol.config.RPCMethodConfig.rate_limit_seconds', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_packet_size', full_name='bnet.protocol.config.RPCMethodConfig.max_packet_size', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_encoded_size', full_name='bnet.protocol.config.RPCMethodConfig.max_encoded_size', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='bnet.protocol.config.RPCMethodConfig.timeout', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=343,
)


_RPCMETERCONFIG = _descriptor.Descriptor(
  name='RPCMeterConfig',
  full_name='bnet.protocol.config.RPCMeterConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='method', full_name='bnet.protocol.config.RPCMeterConfig.method', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='income_per_second', full_name='bnet.protocol.config.RPCMeterConfig.income_per_second', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='initial_balance', full_name='bnet.protocol.config.RPCMeterConfig.initial_balance', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cap_balance', full_name='bnet.protocol.config.RPCMeterConfig.cap_balance', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='startup_period', full_name='bnet.protocol.config.RPCMeterConfig.startup_period', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=346,
  serialized_end=520,
)

_RPCMETERCONFIG.fields_by_name['method'].message_type = _RPCMETHODCONFIG
DESCRIPTOR.message_types_by_name['RPCMethodConfig'] = _RPCMETHODCONFIG
DESCRIPTOR.message_types_by_name['RPCMeterConfig'] = _RPCMETERCONFIG

RPCMethodConfig = _reflection.GeneratedProtocolMessageType('RPCMethodConfig', (_message.Message,), dict(
  DESCRIPTOR = _RPCMETHODCONFIG,
  __module__ = 'bnet.rpc_config_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.config.RPCMethodConfig)
  ))
_sym_db.RegisterMessage(RPCMethodConfig)

RPCMeterConfig = _reflection.GeneratedProtocolMessageType('RPCMeterConfig', (_message.Message,), dict(
  DESCRIPTOR = _RPCMETERCONFIG,
  __module__ = 'bnet.rpc_config_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.config.RPCMeterConfig)
  ))
_sym_db.RegisterMessage(RPCMeterConfig)


# @@protoc_insertion_point(module_scope)
