from pyshark import FileCapture

from srsran_controller.uu_events.nas_emm_security_mode_complete import create as create_security_mode_complete

SECURITY_MODE_COMPLETE_IMEI = (
    '0a0d0d0ab80000004d3c2b1a01000000ffffffffffffffff02003500496e74656c28522920436f726528544d292069372d37373030204350'
    '55204020332e363047487a20287769746820535345342e3229000000030016004c696e757820352e382e302d36332d67656e657269630000'
    '04003a0044756d70636170202857697265736861726b2920332e322e3320284769742076332e322e33207061636b6167656420617320332e'
    '322e332d3129000000000000b80000000100000060000000010000000000040002000b006c74652d6e6574776f726b000900010009000000'
    '0b000e000075647020706f7274203538343700000c0016004c696e757820352e382e302d36332d67656e6572696300000000000060000000'
    '060000007c02000000000000341b94165414c31559020000590200000242eee8b2910242c0a8340208004500024b9ae840004011b368c0a8'
    '3402c0a834fe163716d70237ec996d61632d6c746501000302004603000004032807010a000f00013e2102211d1f000000000ca003034802'
    '68fe3053dca000ebc4612666b28012cf066a3e60000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '000000000000000000000000000000007c020000050000006c00000000000000b5c70500ba35193801001c00436f756e746572732070726f'
    '76696465642062792064756d7063617002000800b5c7050096dddd0a03000800b5c705003e351938040008001b0000000000000005000800'
    '0000000000000000000000006c000000'
)


def test_parsing_emm_security_mode_complete_imei(tmp_path):
    p = tmp_path / 'security_mode_complete_imei.pcap'
    p.write_bytes(bytes.fromhex(SECURITY_MODE_COMPLETE_IMEI))
    with FileCapture(str(p)) as pcap:
        res = create_security_mode_complete(list(pcap)[0])
    assert res == {'imeisv': '3534900698733153', 'event': 'Security mode complete', 'rnti': 70}
