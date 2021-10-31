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


def conf_form(pyterminal, AVDD_WR, AVDD_WL, cycle, times, verbal):
    pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CONF_FORM + ' ' + AVDD_WR + ' ' + AVDD_WL + ' ' + cycle + ' ' + times, verbal)


def form(pyterminal, type, number, verbal):
    if type == 'cell':
        addr = int(number)
        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_FORM + ' ' + str(addr), verbal)
    elif type == 'row':
        for col in range(0, 256):
            addr = int(number)*256 + col
            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_FORM + ' ' + str(addr), verbal)
    elif type == 'col':
        for row in range(0, 256):
            addr = row*256 + int(number)
            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_FORM + ' ' + str(addr), verbal)
    elif type == 'module':
        for row in range(0, 256):
            print('row: ' + str(row))
            for col in range(0, 256):
                addr = row*256 + col
                pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_FORM + ' ' + str(addr), verbal)


def conf_set(pyterminal, AVDD_WR, AVDD_WL, cycle, times, verbal):
    pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CONF_SET + ' ' + AVDD_WR + ' ' + AVDD_WL + ' ' + cycle + ' ' + times, verbal)


def set(pyterminal, type, number, verbal):
    if type == 'cell':
        addr = int(number)
        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_SET + ' ' + str(addr), verbal)
    elif type == 'row':
        for col in range(0, 256):
            addr = int(number)*256 + col
            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_SET + ' ' + str(addr), verbal)
    elif type == 'col':
        for row in range(0, 256):
            addr = row*256 + int(number)
            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_SET + ' ' + str(addr), verbal)
    elif type == 'module':
        for row in range(0, 256):
            print('row: ' + str(row))
            for col in range(0, 256):
                addr = row*256 + col
                pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_SET + ' ' + str(addr), verbal)


def conf_reset(pyterminal, AVDD_WR, AVDD_WL, cycle, times, verbal):
    pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CONF_RESET + ' ' + AVDD_WR + ' ' + AVDD_WL + ' ' + cycle + ' ' + times, verbal)


def reset(pyterminal, type, number, verbal):
    if type == 'cell':
        addr = int(number)
        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_RESET + ' ' + str(addr), verbal)
    elif type == 'row':
        for col in range(0, 256):
            addr = int(number)*256 + col
            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_RESET + ' ' + str(addr), verbal)
    elif type == 'col':
        for row in range(0, 256):
            addr = row*256 + int(number)
            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_RESET + ' ' + str(addr), verbal)
    elif type == 'module':
        for row in range(0, 256):
            print('row: ' + str(row))
            for col in range(0, 256):
                addr = row*256 + col
                pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_RESET + ' ' + str(addr), verbal)


def conf_read(pyterminal, AVDD_WL, cycle, verbal):
    pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CONF_READ + ' ' + AVDD_WL + ' ' + cycle, verbal)


def read_raw(pyterminal, type, number, counter, data, verbal):
    if type == 'cell':
        addr = int(number)
        response = pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_READ + ' ' + str(addr) + ' ' + counter + ' ' + data, False)
        if verbal:
            print(f'{addr:>6} : {response:>10}')
        return response
    elif type == 'row':
        for col in range(0, 256):
            addr = int(number)*256 + col
            response = pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_READ + ' ' + str(addr) + ' ' + counter + ' ' + data, False)
            if verbal:
                print(f'{addr:>6} : {response:>10}')
    elif type == 'col':
        for row in range(0, 256):
            addr = row*256 + int(number)
            response = pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_READ + ' ' + str(addr) + ' ' + counter + ' ' + data, False)
            if verbal:
                print(f'{addr:>6} : {response:>10}')
    elif type == 'module':
        for row in range(0, 256):
            print('row: ' + str(row))
            for col in range(0, 256):
                addr = row*256 + col
                response = pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_READ + ' ' + str(addr) + ' ' + counter + ' ' + data, False)
                if verbal:
                    print(f'{addr:>6} : {response:>10}')

def conf_ADC(pyterminal, offset, step, comp, verbal):
    pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CONF_ADC + ' ' + offset + ' ' + step + ' ' + comp, verbal)


def conf_MAC(pyterminal, mode, resolution, verbal):
    pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CONF_MAC + ' ' + mode + ' ' + resolution, verbal)


def calibrate_voltage_references(pyterminal, index, low, high, tolerance, verbal):
    return pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CAL_VREF + ' ' + index + ' ' + low + ' ' + high + ' ' + tolerance, verbal)


def sweep_voltage_references(pyterminal, index, low, high, step, verbal):
    return pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_SWEEP_VREF + ' ' + index + ' ' + low + ' ' + high + ' ' + step, verbal)


def list_voltage_references(pyterminal, index, verbal):
    return pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_LIST_VREF + ' ' + index, verbal)


def check(pyterminal, type, number, verbal):
    if type == 'cell':
        addr = int(number)
        response = pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CHECK_CELL + ' ' + str(addr), False)
        print(f'{addr:>6} : {response:>10}')
    elif type == 'row':
        for col in range(0, 256):
            addr = int(number)*256 + col
            response = pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CHECK_CELL + ' ' + str(addr), False)
            print(f'{addr:>6} : {response:>10}')
    elif type == 'col':
        for row in range(0, 256):
            addr = row*256 + int(number)
            response = pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CHECK_CELL + ' ' + str(addr), False)
            print(f'{addr:>6} : {response:>10}')
    elif type == 'module':
        for row in range(0, 256):
            for col in range(0, 256):
                addr = row*256 + col
                response = pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CHECK_CELL + ' ' + str(addr), False)
                print(f'{addr:>6} : {response:>10}')

def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    # Driver functions
    if   parameters[1] == 'id'            : print_id                    (pyterminal, True)
    elif parameters[1] == 'status'        : status                      (pyterminal, True)
    elif parameters[1] == 'lane'          : lane                        (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'group'         : group                       (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'module'        : module                      (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'mask'          : mask                        (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'address'       : address                     (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'read'          : read                        (pyterminal, parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'mac'           : mac                         (pyterminal, parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'write'         : write                       (pyterminal, parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'adc'           : adc                         (pyterminal, parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'pg'            : pg                          (pyterminal, parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'ecc'           : ecc                         (pyterminal, parameters[2], parameters[3], parameters[4], True)
    # API functions
    elif parameters[1] == 'conf_form'     : conf_form                   (pyterminal, parameters[2], parameters[3], parameters[4], parameters[5], True)
    elif parameters[1] == 'form'          : form                        (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'conf_set'      : conf_set                    (pyterminal, parameters[2], parameters[3], parameters[4], parameters[5], True)
    elif parameters[1] == 'set'           : set                         (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'conf_reset'    : conf_reset                  (pyterminal, parameters[2], parameters[3], parameters[4], parameters[5], True)
    elif parameters[1] == 'reset'         : reset                       (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'conf_read'     : conf_read                   (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'read_raw'      : read_raw                    (pyterminal, parameters[2], parameters[3], parameters[4], parameters[5], True)
    elif parameters[1] == 'conf_ADC'      : conf_ADC                    (pyterminal, parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'conf_MAC'      : conf_MAC                    (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'calibrate_VRef': calibrate_voltage_references(pyterminal, parameters[2], parameters[3], parameters[4], parameters[5], True)
    elif parameters[1] == 'sweep_VRef'    : sweep_voltage_references    (pyterminal, parameters[2], parameters[3], parameters[4], parameters[5], True)
    elif parameters[1] == 'list_VRef'     : list_voltage_references     (pyterminal, parameters[2], True)
    elif parameters[1] == 'check'         : check                       (pyterminal, parameters[2], parameters[3], True)
    else: unknown(parameters)
