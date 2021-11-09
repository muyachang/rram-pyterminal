from Lib import CommandMap as CM

LevelDict = {'chip'  : b'\x41'.decode('utf-8'), 
             'sector': b'\x42'.decode('utf-8'),
             'block' : b'\x43'.decode('utf-8'),
             'page'  : b'\x44'.decode('utf-8'),
             'byte'  : b'\x45'.decode('utf-8')}


def status(pyterminal, verbal):
    return pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_STATUS, verbal)
    

def get_id(pyterminal, verbal):
    return pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_ID, verbal)


def reset(pyterminal, verbal):
    pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_RESET, verbal)


def read(pyterminal, level, number, verbal):
    print(CM.CM_DF + ' ' + CM.CM_DF_READ + ' ' + LevelDict[level] + ' ' + number)
    pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_READ + ' ' + LevelDict[level] + ' ' + number, verbal)


def write(pyterminal, address, value, verbal):
    print(CM.CM_DF + ' ' + CM.CM_DF_WRITE + ' ' + address + ' ' + value)
    pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_WRITE + ' ' + address + ' ' + value, verbal)


def erase(pyterminal, level, number, verbal):
    print(CM.CM_DF + ' ' + CM.CM_DF_ERASE + ' ' + LevelDict[level] + ' ' + number)
    pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_ERASE + ' ' + LevelDict[level] + ' ' + number, verbal)


def protect(pyterminal, action, sector, verbal):
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
    return pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_BLANKCHECK, verbal)


def unknown(parameters):
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
