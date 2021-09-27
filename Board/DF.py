from Lib import CommandMap as CM

LevelDict = {'chip'  : b'\x41'.decode('utf-8'), 
             'sector': b'\x42'.decode('utf-8'),
             'block' : b'\x43'.decode('utf-8'),
             'page'  : b'\x44'.decode('utf-8'),
             'byte'  : b'\x45'.decode('utf-8')}


def status(pyterminal):
    pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_STATUS, True)
    

def get_id(pyterminal):
    pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_ID, True)


def reset(pyterminal):
    pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_RESET, True)


def read(pyterminal, level, number):
    pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_READ + ' ' + LevelDict[level] + ' ' + number, True)


def write(pyterminal, address, value):
    pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_WRITE + ' ' + address + ' ' + value, True)


def erase(pyterminal, level, number):
    pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_ERASE + ' ' + LevelDict[level] + ' ' + number, True)


def protect(pyterminal, action, sector):
    if   action == 'enable':
        pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_ENABLE, True)
    elif action == 'disable':
        pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_DISABLE, True)
    elif action == 'status':
        pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_STATUS, True)
    elif action == 'all':
        for sector in range(0, 64):
            pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_ADD + ' ' + str(sector), True)
    elif action == 'none':
        for sector in range(0, 64):
            pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_REMOVE + ' ' + str(sector), True)
    elif action == 'add':
        pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_ADD + ' ' + sector, True)
    elif action == 'remove':
        pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_REMOVE + ' ' + sector, True)


def blank_check(pyterminal):
    pyterminal.send_command(CM.CM_DF + ' ' + CM.CM_DF_BLANKCHECK, True)


def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')
          

def decode(pyterminal, parameters):
    if   parameters[1] == 'status'    : status     (pyterminal)
    elif parameters[1] == 'id'        : get_id     (pyterminal)
    elif parameters[1] == 'reset'     : reset      (pyterminal)
    elif parameters[1] == 'read'      : read       (pyterminal, parameters[2], parameters[3])
    elif parameters[1] == 'write'     : write      (pyterminal, parameters[2], parameters[3])
    elif parameters[1] == 'erase'     : erase      (pyterminal, parameters[2], parameters[3])
    elif parameters[1] == 'protect'   : protect    (pyterminal, parameters[2], parameters[3])
    elif parameters[1] == 'blankcheck': blank_check(pyterminal)
    else: unknown(parameters)
