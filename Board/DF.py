from Lib import CommandMap as CM

LevelDict = {'chip'  : b'\x41'.decode('utf-8'), 
             'sector': b'\x42'.decode('utf-8'),
             'block' : b'\x43'.decode('utf-8'),
             'page'  : b'\x44'.decode('utf-8'),
             'byte'  : b'\x45'.decode('utf-8')}


def status(pyterminal, verbal):
    """ Get the status of the dataflash

    Keyword arguments:
    pyterminal -- current connected COM port
    verbal -- whether to print the response or not
    """
    return pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_STATUS, verbal)
    

def get_id(pyterminal, verbal):
    """ Get the id of the dataflash

    Keyword arguments:
    pyterminal -- current connected COM port
    verbal -- whether to print the response or not
    """
    return pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_ID, verbal)


def reset(pyterminal, verbal):
    """ Software reset the dataflash

    Keyword arguments:
    pyterminal -- current connected COM port
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_RESET, verbal)


def read(pyterminal, level, number, verbal):
    """ Read the data from the dataflash

    Keyword arguments:
    pyterminal -- current connected COM port
    level -- could be 'byte', 'page', 'block', 'sector'
    number -- target number
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_READ + ' ' + LevelDict[level] + ' ' + number, verbal)


def write(pyterminal, address, value, verbal):
    """ Read the data from the dataflash

    Keyword arguments:
    pyterminal -- current connected COM port
    address -- address to be written to
    value -- value to be written to
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_WRITE + ' ' + address + ' ' + value, verbal)


def erase(pyterminal, level, number, verbal):
    """ Erase the data in the dataflash

    Keyword arguments:
    pyterminal -- current connected COM port
    level -- could be 'byte', 'page', 'block', 'sector'
    number -- target number
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_ERASE + ' ' + LevelDict[level] + ' ' + number, verbal)


def protect(pyterminal, action, sector, verbal):
    """ Configure the protect function in the dataflash

    Keyword arguments:
    pyterminal -- current connected COM port
    action -- could be 'enable', 'disable', 'status', 'all', 'none', 'add', and 'remove'
    sector -- target sector number, could be '0a', '0b', or '1'~'63'
    verbal -- whether to print the response or not
    """
    if   action == 'enable':
        pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_ENABLE, verbal)
    elif action == 'disable':
        pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_DISABLE, verbal)
    elif action == 'status':
        pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_STATUS, verbal)
    elif action == 'all':
        for sector in range(0, 64):
            pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_ADD + ' ' + str(sector), verbal)
    elif action == 'none':
        for sector in range(0, 64):
            pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_REMOVE + ' ' + str(sector), verbal)
    elif action == 'add':
        pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_ADD + ' ' + sector, verbal)
    elif action == 'remove':
        pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_REMOVE + ' ' + sector, verbal)


def blank_check(pyterminal, verbal):
    """ Get the first nonzero address in the dataflash

    Keyword arguments:
    pyterminal -- current connected COM port
    verbal -- whether to print the response or not
    """
    return pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_BLANKCHECK, verbal)


def unknown(parameters):
    """ Print out the unknown command

    Keyword arguments:
    pyterminal -- current connected COM port
    """
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')
          

def decode(pyterminal, parameters):
    if   parameters[1] == 'status'     : status     (pyterminal,                               True)
    elif parameters[1] == 'id'         : get_id     (pyterminal,                               True)
    elif parameters[1] == 'reset'      : reset      (pyterminal,                               True)
    elif parameters[1] == 'read'       : read       (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'write'      : write      (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'erase'      : erase      (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'protect'    : protect    (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'blank_check': blank_check(pyterminal,                               True)
    else: unknown(parameters)
