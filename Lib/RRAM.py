import CommandMap as CM


def print_id(pyterminal, verbal):
    pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_PID, verbal)


def status(pyterminal, verbal):
    return pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_STATUS, verbal)


def lane(pyterminal, action, target, verbal):
    if   action == 'set':        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_LANE + ' ' + CM.CM_RRAM_SET + ' ' + target, verbal)
    elif action == 'get': return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_LANE + ' ' + CM.CM_RRAM_GET, verbal))
    else: unknown(['RRAM', 'lane', action, target])


def group(pyterminal, action, target, verbal):
    if   action == 'set':        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_GROUP + ' ' + CM.CM_RRAM_SET + ' ' + target, verbal)
    elif action == 'get': return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_GROUP + ' ' + CM.CM_RRAM_GET, verbal))
    else: unknown(['RRAM', 'group', action, target])


def module(pyterminal, action, target, verbal):
    if   action == 'set':        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MODULE + ' ' + CM.CM_RRAM_SET + ' ' + target, verbal)
    elif action == 'get': return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MODULE + ' ' + CM.CM_RRAM_GET, verbal))
    else: unknown(['RRAM', 'module', action, target])


def mask(pyterminal, action, target, verbal):
    if   action == 'set':        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MASK + ' ' + CM.CM_RRAM_SET + ' ' + target, verbal)
    elif action == 'get': return pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MASK + ' ' + CM.CM_RRAM_GET, verbal)
    else: unknown(['RRAM', 'mask', action, target])


def address(pyterminal, action, target, verbal):
    if   action == 'set':        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADDRESS + ' ' + CM.CM_RRAM_SET + ' ' + target, verbal)
    elif action == 'get': return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADDRESS + ' ' + CM.CM_RRAM_GET, verbal))
    else: unknown(['RRAM', 'address', action, target])


def read(pyterminal, action, action_type, target, verbal):
    if action == 'set':
        if   action_type == 'enable' :        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_READ_ENABLE + ' ' + target, verbal)
        elif action_type == 'cycle'  :        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_READ_CYCLE + ' ' + target, verbal)
        elif action_type == 'source' :        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_READ_SOURCE + ' ' + target, verbal)
        elif action_type == 'counter':        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_READ_COUNTER + ' ' + target, verbal)
        elif action_type == 'data'   :        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_READ_DATA + ' ' + target, verbal)
        else: unknown(['RRAM', 'read', action, action_type, target])
    elif action == 'get':
        if   action_type == 'enable' : return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_READ_ENABLE, verbal))
        elif action_type == 'status' : return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_READ_STATUS, verbal))
        elif action_type == 'cycle'  : return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_READ_CYCLE, verbal))
        elif action_type == 'source' : return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_READ_SOURCE, verbal))
        elif action_type == 'counter': return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_READ_COUNTER, verbal))
        elif action_type == 'data'   : return pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_READ_DATA, verbal)
        else: unknown(['RRAM', 'read', action, action_type, target])
    elif action == 'toggle':
        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_TOGGLE, verbal)
    else: unknown(['RRAM', 'read', action, action_type, target])


def mac(pyterminal, action, action_type, target, verbal):
    if action == 'set':
        if   action_type == 'mode'      :        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MAC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_MAC_MODE + ' ' + target, verbal)
        elif action_type == 'resolution':        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MAC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_MAC_RESOLUTION + ' ' + target, verbal)
        else: unknown(['RRAM', 'mac', action, action_type, target])
    elif action == 'get':
        if   action_type == 'status'    : return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MAC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_MAC_STATUS, verbal))
        elif action_type == 'mode'      : return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MAC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_MAC_MODE, verbal))
        elif action_type == 'resolution': return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MAC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_MAC_RESOLUTION, verbal))
        elif action_type == 'result'    : return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MAC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_MAC_RESULT, verbal))
        else: unknown(['RRAM', 'mac', action, action_type, target])
    else: unknown(['RRAM', 'mac', action, action_type, target])


def write(pyterminal, action, action_type, target, verbal):
    if action == 'set':
        if   action_type == 'enable':        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_WRITE_ENABLE + ' ' + target, verbal)
        elif action_type == 'cycle' :        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_WRITE_CYCLE + ' ' + target, verbal)
        elif action_type == 'mode'  :        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_WRITE_MODE + ' ' + target, verbal)
        else: unknown(['RRAM', 'write', action, action_type, target])
    elif action == 'get':
        if   action_type == 'enable': return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_WRITE_ENABLE, verbal))
        elif action_type == 'status': return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_WRITE_STATUS, verbal))
        elif action_type == 'cycle' : return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_WRITE_CYCLE, verbal))
        elif action_type == 'mode'  : return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_WRITE_MODE, verbal))
        else: unknown(['RRAM', 'write', action, action_type, target])
    elif action == 'trigger':
        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_TRIGGER, verbal)
    else: unknown(['RRAM', 'write', action, action_type, target])


def adc(pyterminal, action, action_type, target, verbal):
    if action == 'set':
        if   action_type == 'step'  :        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_ADC_STEP + ' ' + target, verbal)
        elif action_type == 'offset':        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_ADC_OFFSET + ' ' + target, verbal)
        elif action_type == 'comp'  :        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_ADC_COMP + ' ' + target, verbal)
        elif action_type == 'hbias' :        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_ADC_HBIAS + ' ' + target, verbal)
        elif action_type == 'cal'   :        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_ADC_CAL + ' ' + target, verbal)
        else: unknown(['RRAM', 'adc', action, action_type, target])
    elif action == 'get':
        if   action_type == 'raw'   : return pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ADC_RAW, verbal)
        elif action_type == 'step'  : return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ADC_STEP, verbal))
        elif action_type == 'offset': return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ADC_OFFSET, verbal))
        elif action_type == 'comp'  : return pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ADC_COMP, verbal)
        elif action_type == 'hbias' : return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ADC_HBIAS, verbal))
        elif action_type == 'cal'   : return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ADC_CAL, verbal))
        else:
            unknown(['RRAM', 'adc', action, action_type, target])
    else: unknown(['RRAM', 'adc', action, action_type, target])


def pg(pyterminal, action, action_type, target, verbal):
    if action == 'set':
        if   action_type == 'disable':        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_PG + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_PG_DISABLE + ' ' + target, verbal)
        else:
            unknown(['RRAM', 'pg', action, action_type, target])
    elif action == 'get':
        if   action_type == 'disable': return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_PG + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_PG_DISABLE, verbal))
        else:
            unknown(['RRAM', 'pg', action, action_type, target])
    else: unknown(['RRAM', 'pg', action, action_type, target])


def ecc(pyterminal, action, action_type, target, verbal):
    if action == 'set':
        if   action_type == 'enable':        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ECC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_ECC_ENABLE + ' ' + target, verbal)
        else:
            unknown(['RRAM', 'ecc', action, action_type, target])
    elif action == 'get':
        if   action_type == 'enable': return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ECC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ECC_ENABLE, verbal))
        else:
            unknown(['RRAM', 'ecc', action, action_type, target])
    elif action == 'clear':
        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ECC + ' ' + CM.CM_RRAM_CLEAR, verbal)
    elif action == 'check':
        return pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ECC + ' ' + CM.CM_RRAM_CHECK, verbal)
    else: unknown(['RRAM', 'ecc', action, action_type, target])


def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    if   parameters[1] == 'id'     : print_id(pyterminal, True)
    elif parameters[1] == 'status' : status  (pyterminal, True)
    elif parameters[1] == 'lane'   : lane    (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'group'  : group   (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'module' : module  (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'mask'   : mask    (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'address': address (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'read'   : read    (pyterminal, parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'mac'    : mac     (pyterminal, parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'write'  : write   (pyterminal, parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'adc'    : adc     (pyterminal, parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'pg'     : pg      (pyterminal, parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'ecc'    : ecc     (pyterminal, parameters[2], parameters[3], parameters[4], True)
    else: unknown(parameters)
