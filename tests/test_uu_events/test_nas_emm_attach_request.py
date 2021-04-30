from pyshark import FileCapture

from srsran_controller.uu_events.nas_emm_attach_request import create as create_attach_request

ATTACH_REQUEST_PCAP_DATA = (
    'd4c3b2a1020004000000000000000000ffff0000950000000ac78b60366504003702000037020000beefdead023700006d61632d6c746501'
    '000302004603000004048807010a000f00013d3a211f1f0935a0000020002a0e82e2101220202064a8ed3005e0e000080403a02200000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
)


def test_parsing_emm_attach_request(tmp_path):
    p = tmp_path / 'attach_request.pcap'
    p.write_bytes(bytes.fromhex(ATTACH_REQUEST_PCAP_DATA))
    pcap = FileCapture(str(p))
    rar = create_attach_request(list(pcap)[0])
    assert rar == {'imsi': '001010123456789', 'event': 'Attach request', 'rnti': 70}
