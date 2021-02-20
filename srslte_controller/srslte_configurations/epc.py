import configparser
from dataclasses import dataclass, field, asdict

from typing import TextIO


@dataclass
class SrsEpcMmeConfiguration:
    mme_code: str
    mme_group: str
    tac: str
    mcc: str
    mnc: str
    mme_bind_addr: str
    apn: str
    dns_addr: str = '8.8.8.8'
    encryption_algo: str = 'EEA0'
    integrity_algo: str = 'EIA1'
    paging_timer: int = 2


@dataclass
class SrsEpcHssConfiguration:
    db_file: str


@dataclass
class SrsEpcSpgwConfiguration:
    gtpu_bind_addr: str
    sgi_if_addr: str
    sgi_if_name: str = 'srs_spgw_sgi'
    max_paging_queue: int = 100


@dataclass
class SrsEpcPcapConfiguration:
    filename: str
    enable: bool = True


@dataclass
class SrsEpcLogConfiguration:
    nas_level: str = 'info'
    s1ap_level: str = 'info'
    mme_gtpc_level: str = 'info'
    spgw_gtpc_level: str = 'info'
    gtpu_level: str = 'info'
    spgw_level: str = 'info'
    hss_level: str = 'info'
    filename: str = '/tmp/epc.log'
    all_hex_limit: int = 64
    all_level: str = ''

    def to_dict(self):
        log = asdict(self)
        if not self.all_level:
            del log['all_level']
        else:
            del log['nas_level']
            del log['s1ap_level']
            del log['mme_gtpc_level']
            del log['spgw_gtpc_level']
            del log['gtpu_level']
            del log['spgw_level']
            del log['hss_level']
        return log


@dataclass
class SrsEpcConfiguration:
    mme: SrsEpcMmeConfiguration
    hss: SrsEpcHssConfiguration
    spgw: SrsEpcSpgwConfiguration
    pcap: SrsEpcPcapConfiguration = field(
        default_factory=lambda: SrsEpcPcapConfiguration(enable=False, filename='/tmp/epc.pcap')
    )
    log: SrsEpcLogConfiguration = field(default_factory=lambda: SrsEpcLogConfiguration())

    def write(self, fd: TextIO):
        config = configparser.ConfigParser()
        config['mme'] = asdict(self.mme)
        config['hss'] = asdict(self.hss)
        config['spgw'] = asdict(self.spgw)
        config['pcap'] = asdict(self.pcap)
        config['log'] = self.log.to_dict()
        config.write(fd)
