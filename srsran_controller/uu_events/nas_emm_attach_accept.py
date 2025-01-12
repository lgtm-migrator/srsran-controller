NAS_EMM_TYPE_ATTACH_ACCEPT = 0x42
ATTACH_ACCEPT_NAME = 'Attach accept'


def create(pkt):
    try:
        mac_layer = pkt['mac-lte']
        if int(mac_layer.nas_eps_nas_msg_emm_type, 0) == NAS_EMM_TYPE_ATTACH_ACCEPT:
            return {
                'ip': getattr(mac_layer, 'nas_eps.esm.pdn_ipv4'),
                'tmsi': int(mac_layer.nas_eps_emm_m_tmsi, 0),
                'event': ATTACH_ACCEPT_NAME,
                'rnti': int(mac_layer.rnti)
            }
    except (KeyError, AttributeError):
        pass
