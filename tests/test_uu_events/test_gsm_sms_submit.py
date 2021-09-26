import datetime

from pyshark import FileCapture

from srsran_controller.uu_events.factory import EventsFactory
from srsran_controller.uu_events.gsm_sms_submit import GSM_SMS_SUBMIT_NAME

GSM_SMS_SUBMIT_PCAP_DATA = (
    '0a0d0d0ab80000004d3c2b1a01000000ffffffffffffffff02003500496e74656c28522920436f726528544d292069372d37373030204350'
    '55204020332e363047487a20287769746820535345342e3229000000030017004c696e757820352e31312e302d32352d67656e6572696300'
    '04003a0044756d70636170202857697265736861726b2920332e322e3320284769742076332e322e33207061636b6167656420617320332e'
    '322e332d3129000000000000b80000000100000060000000010000000000040002000b006c74652d6e6574776f726b000900010009000000'
    '0b000e000075647020706f7274203538343700000c0017004c696e757820352e31312e302d32352d67656e65726963000000000060000000'
    '060000007c0200000000000042c0a016b6cea54859020000590200000242c3b919f70242c0a8340208004500024bb4b7400040119999c0a8'
    '3402c0a834fe163716d70237ec996d61632d6c746501000302004a0300000433d007010a000f00013d3a223523461f8000a00000480564e0'
    'e28e80e040ec644d2023e0038000d02a7081200ce28021e1922f2a468902acc00000f886f91f8fd26020552504870043806b45000042cb32'
    '00004011f356ac10000208080808ef7f0035002e7efdd987010000010000000000000a696e69742d7030316d64056170706c6503636f6d00'
    '0041000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '000000000000000000000000000000007c020000050000006c00000000000000f1ca05008b4328be01001c00436f756e746572732070726f'
    '76696465642062792064756d7063617002000800f1ca0500f83dc6b103000800f1ca0500ef4228be04000800b30000000000000005000800'
    '0000000000000000000000006c000000'
)


def test_parsing_gsm_sms_submit(tmp_path):
    p = tmp_path / 'gsm_sms_submit.pcap'
    p.write_bytes(bytes.fromhex(GSM_SMS_SUBMIT_PCAP_DATA))
    with FileCapture(str(p)) as pcap:
        submit = EventsFactory().from_packet(list(pcap)[0])
    assert submit == {
        'event': GSM_SMS_SUBMIT_NAME,
        'rp_da': '3548900076',
        'content': 'Do food',
        'tp_da': '972543845166',
        'data': 'From: 972543845166\n Content: Do food',
        'rnti': 74,
        'time': datetime.datetime(2021, 9, 1, 19, 40, 56, 27320),
    }
