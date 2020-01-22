# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bnet/friends_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import bnet.attribute_pb2
import bnet.entity_pb2
import bnet.friends_types_pb2
import bnet.invitation_types_pb2
import bnet.role_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bnet/friends_service.proto',
  package='bnet.protocol.friends',
  serialized_pb=_b('\n\x1a\x62net/friends_service.proto\x12\x15\x62net.protocol.friends\x1a\x14\x62net/attribute.proto\x1a\x11\x62net/entity.proto\x1a\x18\x62net/friends_types.proto\x1a\x1b\x62net/invitation_types.proto\x1a\x0f\x62net/role.proto\"Y\n\x19SubscribeToFriendsRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12\x11\n\tobject_id\x18\x02 \x02(\x04\"\x8d\x02\n\x1aSubscribeToFriendsResponse\x12\x13\n\x0bmax_friends\x18\x01 \x01(\r\x12 \n\x18max_received_invitations\x18\x02 \x01(\r\x12\x1c\n\x14max_sent_invitations\x18\x03 \x01(\r\x12!\n\x04role\x18\x04 \x03(\x0b\x32\x13.bnet.protocol.Role\x12.\n\x07\x66riends\x18\x05 \x03(\x0b\x32\x1d.bnet.protocol.friends.Friend\x12G\n\x14received_invitations\x18\x07 \x03(\x0b\x32).bnet.protocol.friends.ReceivedInvitation\"[\n\x1bUnsubscribeToFriendsRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12\x11\n\tobject_id\x18\x02 \x01(\x04\"m\n\x14GenericFriendRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12*\n\ttarget_id\x18\x02 \x02(\x0b\x32\x17.bnet.protocol.EntityId\"M\n\x15GenericFriendResponse\x12\x34\n\rtarget_friend\x18\x01 \x01(\x0b\x32\x1d.bnet.protocol.friends.Friend\"x\n\x11\x41ssignRoleRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12*\n\ttarget_id\x18\x02 \x02(\x0b\x32\x17.bnet.protocol.EntityId\x12\x0c\n\x04role\x18\x03 \x03(\x05\"}\n\x12ViewFriendsRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12*\n\ttarget_id\x18\x02 \x02(\x0b\x32\x17.bnet.protocol.EntityId\x12\x10\n\x04role\x18\x03 \x03(\rB\x02\x10\x01\"E\n\x13ViewFriendsResponse\x12.\n\x07\x66riends\x18\x01 \x03(\x0b\x32\x1d.bnet.protocol.friends.Friend\"\xc2\x01\n\x18UpdateFriendStateRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12*\n\ttarget_id\x18\x02 \x02(\x0b\x32\x17.bnet.protocol.EntityId\x12\x35\n\tattribute\x18\x03 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\x12\x18\n\x10\x61ttributes_epoch\x18\x04 \x01(\x04\"u\n\x12\x46riendNotification\x12-\n\x06target\x18\x01 \x02(\x0b\x32\x1d.bnet.protocol.friends.Friend\x12\x30\n\x0fgame_account_id\x18\x02 \x01(\x0b\x32\x17.bnet.protocol.EntityId\"\x88\x01\n\x1dUpdateFriendStateNotification\x12\x35\n\x0e\x63hanged_friend\x18\x01 \x02(\x0b\x32\x1d.bnet.protocol.friends.Friend\x12\x30\n\x0fgame_account_id\x18\x02 \x01(\x0b\x32\x17.bnet.protocol.EntityId\"\x97\x01\n\x16InvitationNotification\x12\x38\n\ninvitation\x18\x01 \x02(\x0b\x32$.bnet.protocol.invitation.Invitation\x12\x30\n\x0fgame_account_id\x18\x02 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12\x11\n\x06reason\x18\x03 \x01(\r:\x01\x30')
  ,
  dependencies=[bnet.attribute_pb2.DESCRIPTOR,bnet.entity_pb2.DESCRIPTOR,bnet.friends_types_pb2.DESCRIPTOR,bnet.invitation_types_pb2.DESCRIPTOR,bnet.role_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SUBSCRIBETOFRIENDSREQUEST = _descriptor.Descriptor(
  name='SubscribeToFriendsRequest',
  full_name='bnet.protocol.friends.SubscribeToFriendsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.friends.SubscribeToFriendsRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object_id', full_name='bnet.protocol.friends.SubscribeToFriendsRequest.object_id', index=1,
      number=2, type=4, cpp_type=4, label=2,
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
  serialized_start=166,
  serialized_end=255,
)


_SUBSCRIBETOFRIENDSRESPONSE = _descriptor.Descriptor(
  name='SubscribeToFriendsResponse',
  full_name='bnet.protocol.friends.SubscribeToFriendsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_friends', full_name='bnet.protocol.friends.SubscribeToFriendsResponse.max_friends', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_received_invitations', full_name='bnet.protocol.friends.SubscribeToFriendsResponse.max_received_invitations', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_sent_invitations', full_name='bnet.protocol.friends.SubscribeToFriendsResponse.max_sent_invitations', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role', full_name='bnet.protocol.friends.SubscribeToFriendsResponse.role', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friends', full_name='bnet.protocol.friends.SubscribeToFriendsResponse.friends', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='received_invitations', full_name='bnet.protocol.friends.SubscribeToFriendsResponse.received_invitations', index=5,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=258,
  serialized_end=527,
)


_UNSUBSCRIBETOFRIENDSREQUEST = _descriptor.Descriptor(
  name='UnsubscribeToFriendsRequest',
  full_name='bnet.protocol.friends.UnsubscribeToFriendsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.friends.UnsubscribeToFriendsRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object_id', full_name='bnet.protocol.friends.UnsubscribeToFriendsRequest.object_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=529,
  serialized_end=620,
)


_GENERICFRIENDREQUEST = _descriptor.Descriptor(
  name='GenericFriendRequest',
  full_name='bnet.protocol.friends.GenericFriendRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.friends.GenericFriendRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_id', full_name='bnet.protocol.friends.GenericFriendRequest.target_id', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=622,
  serialized_end=731,
)


_GENERICFRIENDRESPONSE = _descriptor.Descriptor(
  name='GenericFriendResponse',
  full_name='bnet.protocol.friends.GenericFriendResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_friend', full_name='bnet.protocol.friends.GenericFriendResponse.target_friend', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=733,
  serialized_end=810,
)


_ASSIGNROLEREQUEST = _descriptor.Descriptor(
  name='AssignRoleRequest',
  full_name='bnet.protocol.friends.AssignRoleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.friends.AssignRoleRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_id', full_name='bnet.protocol.friends.AssignRoleRequest.target_id', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role', full_name='bnet.protocol.friends.AssignRoleRequest.role', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=812,
  serialized_end=932,
)


_VIEWFRIENDSREQUEST = _descriptor.Descriptor(
  name='ViewFriendsRequest',
  full_name='bnet.protocol.friends.ViewFriendsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.friends.ViewFriendsRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_id', full_name='bnet.protocol.friends.ViewFriendsRequest.target_id', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role', full_name='bnet.protocol.friends.ViewFriendsRequest.role', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
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
  serialized_start=934,
  serialized_end=1059,
)


_VIEWFRIENDSRESPONSE = _descriptor.Descriptor(
  name='ViewFriendsResponse',
  full_name='bnet.protocol.friends.ViewFriendsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='friends', full_name='bnet.protocol.friends.ViewFriendsResponse.friends', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1061,
  serialized_end=1130,
)


_UPDATEFRIENDSTATEREQUEST = _descriptor.Descriptor(
  name='UpdateFriendStateRequest',
  full_name='bnet.protocol.friends.UpdateFriendStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.friends.UpdateFriendStateRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_id', full_name='bnet.protocol.friends.UpdateFriendStateRequest.target_id', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attribute', full_name='bnet.protocol.friends.UpdateFriendStateRequest.attribute', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes_epoch', full_name='bnet.protocol.friends.UpdateFriendStateRequest.attributes_epoch', index=3,
      number=4, type=4, cpp_type=4, label=1,
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
  serialized_start=1133,
  serialized_end=1327,
)


_FRIENDNOTIFICATION = _descriptor.Descriptor(
  name='FriendNotification',
  full_name='bnet.protocol.friends.FriendNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='bnet.protocol.friends.FriendNotification.target', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_account_id', full_name='bnet.protocol.friends.FriendNotification.game_account_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1329,
  serialized_end=1446,
)


_UPDATEFRIENDSTATENOTIFICATION = _descriptor.Descriptor(
  name='UpdateFriendStateNotification',
  full_name='bnet.protocol.friends.UpdateFriendStateNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='changed_friend', full_name='bnet.protocol.friends.UpdateFriendStateNotification.changed_friend', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_account_id', full_name='bnet.protocol.friends.UpdateFriendStateNotification.game_account_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1449,
  serialized_end=1585,
)


_INVITATIONNOTIFICATION = _descriptor.Descriptor(
  name='InvitationNotification',
  full_name='bnet.protocol.friends.InvitationNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='invitation', full_name='bnet.protocol.friends.InvitationNotification.invitation', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_account_id', full_name='bnet.protocol.friends.InvitationNotification.game_account_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='bnet.protocol.friends.InvitationNotification.reason', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=1588,
  serialized_end=1739,
)

_SUBSCRIBETOFRIENDSREQUEST.fields_by_name['agent_id'].message_type = bnet.entity_pb2._ENTITYID
_SUBSCRIBETOFRIENDSRESPONSE.fields_by_name['role'].message_type = bnet.role_pb2._ROLE
_SUBSCRIBETOFRIENDSRESPONSE.fields_by_name['friends'].message_type = bnet.friends_types_pb2._FRIEND
_SUBSCRIBETOFRIENDSRESPONSE.fields_by_name['received_invitations'].message_type = bnet.friends_types_pb2._RECEIVEDINVITATION
_UNSUBSCRIBETOFRIENDSREQUEST.fields_by_name['agent_id'].message_type = bnet.entity_pb2._ENTITYID
_GENERICFRIENDREQUEST.fields_by_name['agent_id'].message_type = bnet.entity_pb2._ENTITYID
_GENERICFRIENDREQUEST.fields_by_name['target_id'].message_type = bnet.entity_pb2._ENTITYID
_GENERICFRIENDRESPONSE.fields_by_name['target_friend'].message_type = bnet.friends_types_pb2._FRIEND
_ASSIGNROLEREQUEST.fields_by_name['agent_id'].message_type = bnet.entity_pb2._ENTITYID
_ASSIGNROLEREQUEST.fields_by_name['target_id'].message_type = bnet.entity_pb2._ENTITYID
_VIEWFRIENDSREQUEST.fields_by_name['agent_id'].message_type = bnet.entity_pb2._ENTITYID
_VIEWFRIENDSREQUEST.fields_by_name['target_id'].message_type = bnet.entity_pb2._ENTITYID
_VIEWFRIENDSRESPONSE.fields_by_name['friends'].message_type = bnet.friends_types_pb2._FRIEND
_UPDATEFRIENDSTATEREQUEST.fields_by_name['agent_id'].message_type = bnet.entity_pb2._ENTITYID
_UPDATEFRIENDSTATEREQUEST.fields_by_name['target_id'].message_type = bnet.entity_pb2._ENTITYID
_UPDATEFRIENDSTATEREQUEST.fields_by_name['attribute'].message_type = bnet.attribute_pb2._ATTRIBUTE
_FRIENDNOTIFICATION.fields_by_name['target'].message_type = bnet.friends_types_pb2._FRIEND
_FRIENDNOTIFICATION.fields_by_name['game_account_id'].message_type = bnet.entity_pb2._ENTITYID
_UPDATEFRIENDSTATENOTIFICATION.fields_by_name['changed_friend'].message_type = bnet.friends_types_pb2._FRIEND
_UPDATEFRIENDSTATENOTIFICATION.fields_by_name['game_account_id'].message_type = bnet.entity_pb2._ENTITYID
_INVITATIONNOTIFICATION.fields_by_name['invitation'].message_type = bnet.invitation_types_pb2._INVITATION
_INVITATIONNOTIFICATION.fields_by_name['game_account_id'].message_type = bnet.entity_pb2._ENTITYID
DESCRIPTOR.message_types_by_name['SubscribeToFriendsRequest'] = _SUBSCRIBETOFRIENDSREQUEST
DESCRIPTOR.message_types_by_name['SubscribeToFriendsResponse'] = _SUBSCRIBETOFRIENDSRESPONSE
DESCRIPTOR.message_types_by_name['UnsubscribeToFriendsRequest'] = _UNSUBSCRIBETOFRIENDSREQUEST
DESCRIPTOR.message_types_by_name['GenericFriendRequest'] = _GENERICFRIENDREQUEST
DESCRIPTOR.message_types_by_name['GenericFriendResponse'] = _GENERICFRIENDRESPONSE
DESCRIPTOR.message_types_by_name['AssignRoleRequest'] = _ASSIGNROLEREQUEST
DESCRIPTOR.message_types_by_name['ViewFriendsRequest'] = _VIEWFRIENDSREQUEST
DESCRIPTOR.message_types_by_name['ViewFriendsResponse'] = _VIEWFRIENDSRESPONSE
DESCRIPTOR.message_types_by_name['UpdateFriendStateRequest'] = _UPDATEFRIENDSTATEREQUEST
DESCRIPTOR.message_types_by_name['FriendNotification'] = _FRIENDNOTIFICATION
DESCRIPTOR.message_types_by_name['UpdateFriendStateNotification'] = _UPDATEFRIENDSTATENOTIFICATION
DESCRIPTOR.message_types_by_name['InvitationNotification'] = _INVITATIONNOTIFICATION

SubscribeToFriendsRequest = _reflection.GeneratedProtocolMessageType('SubscribeToFriendsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIBETOFRIENDSREQUEST,
  __module__ = 'bnet.friends_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.SubscribeToFriendsRequest)
  ))
_sym_db.RegisterMessage(SubscribeToFriendsRequest)

SubscribeToFriendsResponse = _reflection.GeneratedProtocolMessageType('SubscribeToFriendsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIBETOFRIENDSRESPONSE,
  __module__ = 'bnet.friends_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.SubscribeToFriendsResponse)
  ))
_sym_db.RegisterMessage(SubscribeToFriendsResponse)

UnsubscribeToFriendsRequest = _reflection.GeneratedProtocolMessageType('UnsubscribeToFriendsRequest', (_message.Message,), dict(
  DESCRIPTOR = _UNSUBSCRIBETOFRIENDSREQUEST,
  __module__ = 'bnet.friends_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.UnsubscribeToFriendsRequest)
  ))
_sym_db.RegisterMessage(UnsubscribeToFriendsRequest)

GenericFriendRequest = _reflection.GeneratedProtocolMessageType('GenericFriendRequest', (_message.Message,), dict(
  DESCRIPTOR = _GENERICFRIENDREQUEST,
  __module__ = 'bnet.friends_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.GenericFriendRequest)
  ))
_sym_db.RegisterMessage(GenericFriendRequest)

GenericFriendResponse = _reflection.GeneratedProtocolMessageType('GenericFriendResponse', (_message.Message,), dict(
  DESCRIPTOR = _GENERICFRIENDRESPONSE,
  __module__ = 'bnet.friends_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.GenericFriendResponse)
  ))
_sym_db.RegisterMessage(GenericFriendResponse)

AssignRoleRequest = _reflection.GeneratedProtocolMessageType('AssignRoleRequest', (_message.Message,), dict(
  DESCRIPTOR = _ASSIGNROLEREQUEST,
  __module__ = 'bnet.friends_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.AssignRoleRequest)
  ))
_sym_db.RegisterMessage(AssignRoleRequest)

ViewFriendsRequest = _reflection.GeneratedProtocolMessageType('ViewFriendsRequest', (_message.Message,), dict(
  DESCRIPTOR = _VIEWFRIENDSREQUEST,
  __module__ = 'bnet.friends_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.ViewFriendsRequest)
  ))
_sym_db.RegisterMessage(ViewFriendsRequest)

ViewFriendsResponse = _reflection.GeneratedProtocolMessageType('ViewFriendsResponse', (_message.Message,), dict(
  DESCRIPTOR = _VIEWFRIENDSRESPONSE,
  __module__ = 'bnet.friends_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.ViewFriendsResponse)
  ))
_sym_db.RegisterMessage(ViewFriendsResponse)

UpdateFriendStateRequest = _reflection.GeneratedProtocolMessageType('UpdateFriendStateRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEFRIENDSTATEREQUEST,
  __module__ = 'bnet.friends_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.UpdateFriendStateRequest)
  ))
_sym_db.RegisterMessage(UpdateFriendStateRequest)

FriendNotification = _reflection.GeneratedProtocolMessageType('FriendNotification', (_message.Message,), dict(
  DESCRIPTOR = _FRIENDNOTIFICATION,
  __module__ = 'bnet.friends_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.FriendNotification)
  ))
_sym_db.RegisterMessage(FriendNotification)

UpdateFriendStateNotification = _reflection.GeneratedProtocolMessageType('UpdateFriendStateNotification', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEFRIENDSTATENOTIFICATION,
  __module__ = 'bnet.friends_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.UpdateFriendStateNotification)
  ))
_sym_db.RegisterMessage(UpdateFriendStateNotification)

InvitationNotification = _reflection.GeneratedProtocolMessageType('InvitationNotification', (_message.Message,), dict(
  DESCRIPTOR = _INVITATIONNOTIFICATION,
  __module__ = 'bnet.friends_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.InvitationNotification)
  ))
_sym_db.RegisterMessage(InvitationNotification)


_VIEWFRIENDSREQUEST.fields_by_name['role'].has_options = True
_VIEWFRIENDSREQUEST.fields_by_name['role']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)