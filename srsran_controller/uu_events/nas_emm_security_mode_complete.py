NAS_EMM_TYPE_SECURITY_MODE_COMPLETE = 0x5e
SECURITY_MODE_COMPLETE_NAME = 'Security mode complete'


def create(pkt):
    try:
        mac_layer = pkt['mac-lte']
        if int(mac_layer.nas_eps_nas_msg_emm_type, 0) == NAS_EMM_TYPE_SECURITY_MODE_COMPLETE:
            event = {
                'event': SECURITY_MODE_COMPLETE_NAME,
                'rnti': int(mac_layer.rnti),
            }
            if hasattr(mac_layer, 'gsm_a.imeisv'):
                event['imeisv'] = getattr(mac_layer, 'gsm_a.imeisv')
            return event
    except (KeyError, AttributeError):
        pass
