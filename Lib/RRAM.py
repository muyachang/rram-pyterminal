import CommandMap as CM


def id(pyterminal, verbal):
    """ Get the id of the RRAM module

    Keyword arguments:
    pyterminal -- current connected COM port
    verbal -- whether to print the response or not
    """
    return pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_PID, verbal)


def status(pyterminal, verbal):
    """ Get the status of the RRAM modules

    Keyword arguments:
    pyterminal -- current connected COM port
    verbal -- whether to print the response or not
    """
    return pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_STATUS, verbal)


def lane(pyterminal, action, target, verbal):
    """ Set/Get the selected ADC lane

    Keyword arguments:
    pyterminal -- current connected COM port
    action -- could be 'set' or 'get'
    target -- target lane number, from '0'~'7'
    verbal -- whether to print the response or not
    """
    if   action == 'set':            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_LANE + ' ' + CM.CM_RRAM_SET + ' ' + target, verbal)
    elif action == 'get': return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_LANE + ' ' + CM.CM_RRAM_GET, verbal))
    else: unknown(['RRAM', 'lane', action, target])


def group(pyterminal, action, target, verbal):
    """ Set/Get the selected group for the Vector module

    Keyword arguments:
    pyterminal -- current connected COM port
    action -- could be 'set' or 'get'
    target -- target group number, from '0'~'35'
    verbal -- whether to print the response or not
    """
    if   action == 'set':            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_GROUP + ' ' + CM.CM_RRAM_SET + ' ' + target, verbal)
    elif action == 'get': return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_GROUP + ' ' + CM.CM_RRAM_GET, verbal))
    else: unknown(['RRAM', 'group', action, target])


def module(pyterminal, action, target, verbal):
    """ Set/Get the selected RRAM module

    Keyword arguments:
    pyterminal -- current connected COM port
    action -- could be 'set' or 'get'
    target -- target RRAM module number, from '0'~'287'
    verbal -- whether to print the response or not
    """
    if   action == 'set':            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MODULE + ' ' + CM.CM_RRAM_SET + ' ' + target, verbal)
    elif action == 'get': return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MODULE + ' ' + CM.CM_RRAM_GET, verbal))
    else: unknown(['RRAM', 'module', action, target])


def mask(pyterminal, action, target, verbal):
    """ Set/Get the RRAM module selection mask register

    Keyword arguments:
    pyterminal -- current connected COM port
    action -- could be 'set' or 'get'
    target -- target RRAM module selection mask, from '0x00000001'~'0xFFFFFFFF'
    verbal -- whether to print the response or not
    """
    if   action == 'set':        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MASK + ' ' + CM.CM_RRAM_SET + ' ' + target, verbal)
    elif action == 'get': return pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MASK + ' ' + CM.CM_RRAM_GET, verbal)
    else: unknown(['RRAM', 'mask', action, target])


def address(pyterminal, action, target, verbal):
    """ Set/Get the RRAM module address register

    Keyword arguments:
    pyterminal -- current connected COM port
    action -- could be 'set' or 'get'
    target -- target address, from '0'~'65535'
    verbal -- whether to print the response or not
    """
    if   action == 'set':            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADDRESS + ' ' + CM.CM_RRAM_SET + ' ' + target, verbal)
    elif action == 'get': return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADDRESS + ' ' + CM.CM_RRAM_GET, verbal))
    else: unknown(['RRAM', 'address', action, target])


def read(pyterminal, action, action_type, target, verbal):
    """ Configure read related settings

    Keyword arguments:
    pyterminal -- current connected COM port
    action -- could be 'set' or 'get'
    action_type -- could be 'status', 'enable', 'cycle', 'source', 'counter', 'data'
    target -- target number, '0'~'1' for 'enable' 'source', '0'~'255' for 'cycle', and '0x1'~'0x1FF' for 'data'
    verbal -- whether to print the response or not
    """
    if action == 'set':
        if   action_type == 'enable' :        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_READ_ENABLE  + ' ' + target, verbal)
        elif action_type == 'cycle'  :        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_READ_CYCLE   + ' ' + target, verbal)
        elif action_type == 'source' :        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_READ_SOURCE  + ' ' + target, verbal)
        elif action_type == 'counter':        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_READ_COUNTER + ' ' + target, verbal)
        elif action_type == 'data'   :        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_READ_DATA    + ' ' + target, verbal)
        else: unknown(['RRAM', 'read', action, action_type, target])
    elif action == 'get':
        if   action_type == 'enable' : return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_READ_ENABLE , verbal))
        elif action_type == 'status' : return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_READ_STATUS , verbal))
        elif action_type == 'cycle'  : return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_READ_CYCLE  , verbal))
        elif action_type == 'source' : return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_READ_SOURCE , verbal))
        elif action_type == 'counter': return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_READ_COUNTER, verbal))
        elif action_type == 'data'   : return     pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_READ_DATA   , verbal)
        else: unknown(['RRAM', 'read', action, action_type, target])
    elif action == 'toggle':
        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_TOGGLE, verbal)
    else: unknown(['RRAM', 'read', action, action_type, target])


def mac(pyterminal, action, action_type, target, verbal):
    """ Configure mac related settings

    Keyword arguments:
    pyterminal -- current connected COM port
    action -- could be 'set' or 'get'
    action_type -- could be 'status', 'result', 'mode', 'resolution'
    target -- target number, '0'~'1' for 'mode', '0'~'3' for 'resolution'
    verbal -- whether to print the response or not
    """
    if action == 'set':
        if   action_type == 'mode'      :            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MAC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_MAC_MODE       + ' ' + target, verbal)
        elif action_type == 'resolution':            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MAC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_MAC_RESOLUTION + ' ' + target, verbal)
        else: unknown(['RRAM', 'mac', action, action_type, target])
    elif action == 'get':
        if   action_type == 'status'    : return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MAC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_MAC_STATUS    , verbal))
        elif action_type == 'mode'      : return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MAC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_MAC_MODE      , verbal))
        elif action_type == 'resolution': return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MAC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_MAC_RESOLUTION, verbal))
        elif action_type == 'result'    : return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MAC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_MAC_RESULT    , verbal))
        else: unknown(['RRAM', 'mac', action, action_type, target])
    else: unknown(['RRAM', 'mac', action, action_type, target])


def write(pyterminal, action, action_type, target, verbal):
    """ Configure read related settings

    Keyword arguments:
    pyterminal -- current connected COM port
    action -- could be 'set' or 'get'
    action_type -- could be 'status', 'enable', 'cycle', 'mode'
    target -- target number, '0'~'1' for 'enable' 'mode', '0'~'65535' for 'cycle'
    verbal -- whether to print the response or not
    """
    if action == 'set':
        if   action_type == 'enable':            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_WRITE_ENABLE + ' ' + target, verbal)
        elif action_type == 'cycle' :            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_WRITE_CYCLE  + ' ' + target, verbal)
        elif action_type == 'mode'  :            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_WRITE_MODE   + ' ' + target, verbal)
        else: unknown(['RRAM', 'write', action, action_type, target])
    elif action == 'get':
        if   action_type == 'enable': return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_WRITE_ENABLE, verbal))
        elif action_type == 'status': return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_WRITE_STATUS, verbal))
        elif action_type == 'cycle' : return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_WRITE_CYCLE , verbal))
        elif action_type == 'mode'  : return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_WRITE_MODE  , verbal))
        else: unknown(['RRAM', 'write', action, action_type, target])
    elif action == 'trigger':
        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_TRIGGER, verbal)
    else: unknown(['RRAM', 'write', action, action_type, target])


def adc(pyterminal, action, action_type, target, verbal):
    """ Configure adc related settings

    Keyword arguments:
    pyterminal -- current connected COM port
    action -- could be 'set' or 'get'
    action_type -- could be 'raw', 'step', 'offset', 'comp', 'hbias', 'cal'
    target -- target number, '0'~'1' for 'hbias' 'cal', '0'~'63' for 'step' 'offset', '0x0000'~'0x7FFF' for 'comp'
    verbal -- whether to print the response or not
    """
    if action == 'set':
        if   action_type == 'step'  :            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_ADC_STEP   + ' ' + target, verbal)
        elif action_type == 'offset':            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_ADC_OFFSET + ' ' + target, verbal)
        elif action_type == 'comp'  :            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_ADC_COMP   + ' ' + target, verbal)
        elif action_type == 'hbias' :            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_ADC_HBIAS  + ' ' + target, verbal)
        elif action_type == 'cal'   :            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_ADC_CAL    + ' ' + target, verbal)
        else: unknown(['RRAM', 'adc', action, action_type, target])
    elif action == 'get':
        if   action_type == 'raw'   : return     pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ADC_RAW   , verbal)
        elif action_type == 'step'  : return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ADC_STEP  , verbal))
        elif action_type == 'offset': return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ADC_OFFSET, verbal))
        elif action_type == 'comp'  : return     pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ADC_COMP  , verbal)
        elif action_type == 'hbias' : return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ADC_HBIAS , verbal))
        elif action_type == 'cal'   : return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ADC_CAL   , verbal))
        else:
            unknown(['RRAM', 'adc', action, action_type, target])
    else: unknown(['RRAM', 'adc', action, action_type, target])


def pg(pyterminal, action, action_type, target, verbal):
    """ Configure power gating related settings

    Keyword arguments:
    pyterminal -- current connected COM port
    action -- could be 'set' or 'get'
    action_type -- could be 'disable'
    target -- target number, '0'~'1' for 'disable'
    verbal -- whether to print the response or not
    """
    if action == 'set':
        if   action_type == 'disable':            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_PG + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_PG_DISABLE + ' ' + target, verbal)
        else:
            unknown(['RRAM', 'pg', action, action_type, target])
    elif action == 'get':
        if   action_type == 'disable': return int(pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_PG + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_PG_DISABLE, verbal))
        else:
            unknown(['RRAM', 'pg', action, action_type, target])
    else: unknown(['RRAM', 'pg', action, action_type, target])


def ecc(pyterminal, action, action_type, target, verbal):
    """ Configure power gating related settings

    Keyword arguments:
    pyterminal -- current connected COM port
    action -- could be 'set', 'get', 'clear', or 'check'
    action_type -- could be 'enable'
    target -- target number, '0'~'1' for 'enable'
    verbal -- whether to print the response or not
    """
    if action == 'set':
        if   action_type == 'enable':            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ECC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_ECC_ENABLE + ' ' + target, verbal)
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
    """ Configure FORM operation

    Keyword arguments:
    pyterminal -- current connected COM port
    AVDD_WR -- AVDD_WR voltage
    AVDD_WL -- AVDD_WL voltage
    cycle -- number of clock cycles per pulse
    times -- number of pulses
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CONF_FORM + ' ' + AVDD_WR + ' ' + AVDD_WL + ' ' + cycle + ' ' + times, verbal)


def form(pyterminal, level, number, verbal):
    """ FORM the cells

    Keyword arguments:
    pyterminal -- current connected COM port
    level -- could be 'cell', 'row', 'col', 'module'
    number -- target number
    verbal -- whether to print the response or not
    """
    if level == 'cell':
        addr = int(number)
        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_FORM + ' ' + str(addr), verbal)
    elif level == 'row':
        for col in range(0, 256):
            addr = int(number)*256 + col
            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_FORM + ' ' + str(addr), verbal)
    elif level == 'col':
        for row in range(0, 256):
            addr = row*256 + int(number)
            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_FORM + ' ' + str(addr), verbal)
    elif level == 'module':
        for row in range(0, 256):
            print('row: ' + str(row))
            for col in range(0, 256):
                addr = row*256 + col
                pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_FORM + ' ' + str(addr), verbal)


def conf_set(pyterminal, AVDD_WR, AVDD_WL, cycle, times, verbal):
    """ Configure SET operation

    Keyword arguments:
    pyterminal -- current connected COM port
    AVDD_WR -- AVDD_WR voltage
    AVDD_WL -- AVDD_WL voltage
    cycle -- number of clock cycles per pulse
    times -- number of pulses
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CONF_SET + ' ' + AVDD_WR + ' ' + AVDD_WL + ' ' + cycle + ' ' + times, verbal)


def set(pyterminal, level, number, verbal):
    """ SET the cells

    Keyword arguments:
    pyterminal -- current connected COM port
    level -- could be 'cell', 'row', 'col', 'module'
    number -- target number
    verbal -- whether to print the response or not
    """
    if level == 'cell':
        address = int(number)
        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_SET + ' ' + str(address), verbal)
    elif level == 'row':
        for col in range(0, 256):
            address = int(number)*256 + col
            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_SET + ' ' + str(address), verbal)
    elif level == 'col':
        for row in range(0, 256):
            address = row*256 + int(number)
            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_SET + ' ' + str(address), verbal)
    elif level == 'module':
        for row in range(0, 256):
            print('row: ' + str(row))
            for col in range(0, 256):
                address = row*256 + col
                pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_SET + ' ' + str(address), verbal)


def conf_reset(pyterminal, AVDD_WR, AVDD_WL, cycle, times, verbal):
    """ Configure RESET operation

    Keyword arguments:
    pyterminal -- current connected COM port
    AVDD_WR -- AVDD_WR voltage
    AVDD_WL -- AVDD_WL voltage
    cycle -- number of clock cycles per pulse
    times -- number of pulses
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CONF_RESET + ' ' + AVDD_WR + ' ' + AVDD_WL + ' ' + cycle + ' ' + times, verbal)


def reset(pyterminal, level, number, verbal):
    """ RESET the cells

    Keyword arguments:
    pyterminal -- current connected COM port
    level -- could be 'cell', 'row', 'col', 'module'
    number -- target number
    verbal -- whether to print the response or not
    """
    if level == 'cell':
        address = int(number)
        pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_RESET + ' ' + str(address), verbal)
    elif level == 'row':
        for col in range(0, 256):
            address = int(number)*256 + col
            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_RESET + ' ' + str(address), verbal)
    elif level == 'col':
        for row in range(0, 256):
            address = row*256 + int(number)
            pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_RESET + ' ' + str(address), verbal)
    elif level == 'module':
        for row in range(0, 256):
            print('row: ' + str(row))
            for col in range(0, 256):
                address = row*256 + col
                pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_RESET + ' ' + str(address), verbal)


def write_byte(pyterminal, address, value, verbal):
    """ Write 'value' to 'address'

    Keyword arguments:
    pyterminal -- current connected COM port
    address -- address to be written to
    value -- value to be written to
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_WRITE_BYTE + ' ' + address + ' ' + value, verbal)


def write_byte_iter(pyterminal, address, value, verbal):
    """ Write 'value' to 'address' iteratively, this function is more robust than 'write_byte' but takes longer

    Keyword arguments:
    pyterminal -- current connected COM port
    address -- address to be written to
    value -- value to be written to
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_WRITE_BYTE_ITER + ' ' + address + ' ' + value, verbal)


def conf_read(pyterminal, AVDD_WL, cycle, verbal):
    """ Configure READ operation

    Keyword arguments:
    pyterminal -- current connected COM port
    AVDD_WL -- AVDD_WL voltage
    cycle -- number of clock cycles per pulse
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CONF_READ + ' ' + AVDD_WL + ' ' + cycle, verbal)


def read_lane(pyterminal, address, data, verbal):
    """ Read the 'address' cell with 'data' fed to the WLs

    Keyword arguments:
    pyterminal -- current connected COM port
    address -- address to be read from
    value -- value to be fed to the WLs
    verbal -- whether to print the response or not
    """
    return pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_READ_LANE + ' ' + address + ' ' + data, verbal)


def read_byte(pyterminal, address, counter, data, verbal):
    """ Read the whole byte from 'address' with 'data' fed to the WLs and 'counter' for the MAC unit

    Keyword arguments:
    pyterminal -- current connected COM port
    address -- address to be read from
    counter -- so the MAC unit knows which bit the 'data' is currently at
    value -- value to be fed to the WLs
    verbal -- whether to print the response or not
    """
    return pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_READ_BYTE + ' ' + address + ' ' + counter + ' ' + data, verbal)


def conf_ADC(pyterminal, offset, step, comp, verbal):
    """ Configure ADC settings

    Keyword arguments:
    pyterminal -- current connected COM port
    offset -- from '0'~'63', '0' for minimum offset and '63' for maximum offset
    step -- from '0'~'63', '0' for minimum step and '63' for maximum step
    comp -- comparator enables, from '0x0001'~'0x7FFF', each bit controls a comparator
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CONF_ADC + ' ' + offset + ' ' + step + ' ' + comp, verbal)


def conf_MAC(pyterminal, mode, resolution, verbal):
    """ Configure MAC settings

    Keyword arguments:
    pyterminal -- current connected COM port
    mode -- from '0'~'1', '0' for unsigned and '1' for 'signed'
    resolution -- from '0'~'3', '0' for 1 bit, '1' for 2 bits, '2' for 4 bits, and '3' for 8 bits
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CONF_MAC + ' ' + mode + ' ' + resolution, verbal)


def calibrate_voltage_references(pyterminal, index, low, high, tolerance, verbal):
    """ Calibrate the internally generated reference voltages so the range would be approx. ('low', 'high') for 'index' module

    Keyword arguments:
    pyterminal -- current connected COM port
    index -- from '0' ~ '287', the target RRAM module
    low -- lower bound of the reference voltages
    high -- upper bound of the reference voltages
    tolerance -- means ideally the first extreme reference voltage should be within 'tolerance' from either 'low' or 'high'
    verbal -- whether to print the response or not
    """
    return pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CAL_VREF + ' ' + index + ' ' + low + ' ' + high + ' ' + tolerance, verbal)


def sweep_voltage_references(pyterminal, index, low, high, step, verbal):
    """ Sweep the ADC_CAL and look for all 15 internally generated reference voltages for 'index' module

    Keyword arguments:
    pyterminal -- current connected COM port
    index -- from '0' ~ '287', the target RRAM module
    low -- starting voltage for ADC_CAL
    high -- ending voltage for ADC_CAL
    step -- step for ADC_CAL
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_SWEEP_VREF + ' ' + index + ' ' + low + ' ' + high + ' ' + step, verbal)


def list_voltage_references(pyterminal, index, verbal):
    """ List 15 internally generated reference voltages of 'index' module, sweep_voltage_references needs to be done in advance

    Keyword arguments:
    pyterminal -- current connected COM port
    index -- from '0' ~ '287', the target RRAM module
    verbal -- whether to print the response or not
    """
    return pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_LIST_VREF + ' ' + index, verbal)


def sweep_decoder_references(pyterminal, index, ones, verbal):
    """ Calibrate decoder reference levels

    Keyword arguments:
    pyterminal -- current connected COM port
    index -- from '0' ~ '287', the target RRAM module
    ones -- could be omit or '0'~'9', omit means do the calibration for all '1'~'9'
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_SWEEP_DREF + ' ' + index + ' ' + ones, verbal)


def list_decoder_references(pyterminal, index, verbal):
    """ List decoder reference levels of 'index' module

    Keyword arguments:
    pyterminal -- current connected COM port
    index -- from '0' ~ '287', the target RRAM module
    verbal -- whether to print the response or not
    """
    return pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_LIST_DREF + ' ' + index, verbal)


def check(pyterminal, level, number, verbal):
    """ Check the health of RRAM cells, this function essentially SET the cell and read the value, then RESET the cell
        and read the value.
        If the cell is healthy, the ADC raw value after SET should be smaller than the value after RESET

    Keyword arguments:
    pyterminal -- current connected COM port
    level -- could be 'cell', 'row', 'col', 'module'
    number -- target number
    verbal -- whether to print the response or not
    """
    if level == 'cell':
        address = int(number)
        response = pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CHECK_CELL + ' ' + str(address), False)
        print(f'{address:>6} : {response:>10}')
    elif level == 'row':
        for col in range(0, 256):
            address = int(number)*256 + col
            response = pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CHECK_CELL + ' ' + str(address), False)
            print(f'{address:>6} : {response:>10}')
    elif level == 'col':
        for row in range(0, 256):
            address = row*256 + int(number)
            response = pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CHECK_CELL + ' ' + str(address), False)
            print(f'{address:>6} : {response:>10}')
    elif level == 'module':
        for row in range(0, 256):
            for col in range(0, 256):
                address = row*256 + col
                response = pyterminal.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CHECK_CELL + ' ' + str(address), False)
                print(f'{address:>6} : {response:>10}')


def unknown(parameters):
    """ Print out the unknown command

    Keyword arguments:
    parameters -- the split version of the command
    """
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    """ Decode the split version of the command

    Keyword arguments:
    pyterminal -- current connected COM port
    parameters -- split version of the command
    """
    # Driver functions
    if   parameters[1] == 'id'             : id                          (pyterminal,                                                             True)
    elif parameters[1] == 'status'         : status                      (pyterminal,                                                             True)
    elif parameters[1] == 'lane'           : lane                        (pyterminal, parameters[2], parameters[3],                               True)
    elif parameters[1] == 'group'          : group                       (pyterminal, parameters[2], parameters[3],                               True)
    elif parameters[1] == 'module'         : module                      (pyterminal, parameters[2], parameters[3],                               True)
    elif parameters[1] == 'mask'           : mask                        (pyterminal, parameters[2], parameters[3],                               True)
    elif parameters[1] == 'address'        : address                     (pyterminal, parameters[2], parameters[3],                               True)
    elif parameters[1] == 'read'           : read                        (pyterminal, parameters[2], parameters[3], parameters[4],                True)
    elif parameters[1] == 'mac'            : mac                         (pyterminal, parameters[2], parameters[3], parameters[4],                True)
    elif parameters[1] == 'write'          : write                       (pyterminal, parameters[2], parameters[3], parameters[4],                True)
    elif parameters[1] == 'adc'            : adc                         (pyterminal, parameters[2], parameters[3], parameters[4],                True)
    elif parameters[1] == 'pg'             : pg                          (pyterminal, parameters[2], parameters[3], parameters[4],                True)
    elif parameters[1] == 'ecc'            : ecc                         (pyterminal, parameters[2], parameters[3], parameters[4],                True)
    # API functions
    elif parameters[1] == 'conf_form'      : conf_form                   (pyterminal, parameters[2], parameters[3], parameters[4], parameters[5], True)
    elif parameters[1] == 'form'           : form                        (pyterminal, parameters[2], parameters[3],                               True)
    elif parameters[1] == 'conf_set'       : conf_set                    (pyterminal, parameters[2], parameters[3], parameters[4], parameters[5], True)
    elif parameters[1] == 'set'            : set                         (pyterminal, parameters[2], parameters[3],                               True)
    elif parameters[1] == 'conf_reset'     : conf_reset                  (pyterminal, parameters[2], parameters[3], parameters[4], parameters[5], True)
    elif parameters[1] == 'reset'          : reset                       (pyterminal, parameters[2], parameters[3],                               True)
    elif parameters[1] == 'write_byte'     : write_byte                  (pyterminal, parameters[2], parameters[3],                               True)
    elif parameters[1] == 'write_byte_iter': write_byte_iter             (pyterminal, parameters[2], parameters[3],                               True)
    elif parameters[1] == 'conf_read'      : conf_read                   (pyterminal, parameters[2], parameters[3],                               True)
    elif parameters[1] == 'read_lane'      : read_lane                   (pyterminal, parameters[2], parameters[3],                               True)
    elif parameters[1] == 'read_byte'      : read_byte                   (pyterminal, parameters[2], parameters[3], parameters[4],                True)
    elif parameters[1] == 'conf_ADC'       : conf_ADC                    (pyterminal, parameters[2], parameters[3], parameters[4],                True)
    elif parameters[1] == 'conf_MAC'       : conf_MAC                    (pyterminal, parameters[2], parameters[3],                               True)
    elif parameters[1] == 'calibrate_VRef' : calibrate_voltage_references(pyterminal, parameters[2], parameters[3], parameters[4], parameters[5], True)
    elif parameters[1] == 'sweep_VRef'     : sweep_voltage_references    (pyterminal, parameters[2], parameters[3], parameters[4], parameters[5], True)
    elif parameters[1] == 'list_VRef'      : list_voltage_references     (pyterminal, parameters[2],                                              True)
    elif parameters[1] == 'sweep_DRef'     : sweep_decoder_references    (pyterminal, parameters[2], parameters[3],                               True)
    elif parameters[1] == 'list_DRef'      : list_decoder_references     (pyterminal, parameters[2],                                              True)
    elif parameters[1] == 'check'          : check                       (pyterminal, parameters[2], parameters[3],                               True)
    else: unknown(parameters)
