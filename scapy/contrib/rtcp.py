#
# Partial support of RTCP
#

"""
RTCP (Real-time Transport Protocol).
"""

# scapy.contrib.description = RTCP
# scapy.contrib.status = loads


from scapy.packet import Packet, bind_layers
from scapy.fields import BitEnumField, BitField, BitFieldLenField, \
    LongField, FieldListField, IntField, ShortField, ByteField



class RTCP(Packet):
    name = "RTCP"
    fields_desc = [BitField('version', 2, 2),
                   BitField('padding', 0, 1),
                   BitField('reception_count', 0, 5),
                   ByteField('packet_type', 200),
                   ShortField('lenght', 0),
                   IntField('SSRC', 0),
                   LongField('ntp_timestamp', 0),
                   IntField('rtp_timestamp', 0),
                   IntField('sender_packetcount', 0),
                   IntField('sender_octectcount', 0)]




