from Lib import CommandMap as CM

LevelDict = {'chip'  : b'\x41'.decode('utf-8'), 
             'sector': b'\x42'.decode('utf-8'),
             'block' : b'\x43'.decode('utf-8'),
             'page'  : b'\x44'.decode('utf-8'),
             'byte'  : b'\x45'.decode('utf-8')}

def status(PT):
    PT.sendCommand(CM.CM_DF + ' ' + CM.CM_DF_STATUS, True)
    
def id(PT):
    PT.sendCommand(CM.CM_DF + ' ' + CM.CM_DF_ID, True)

def reset(PT):
    PT.sendCommand(CM.CM_DF + ' ' + CM.CM_DF_RESET, True)

def read(PT, level, number):
    PT.sendCommand(CM.CM_DF + ' ' + CM.CM_DF_READ + ' ' + LevelDict[level] + ' ' + number, True)

def write(PT, address, value):
    PT.sendCommand(CM.CM_DF + ' ' + CM.CM_DF_WRITE + ' ' + address + ' ' + value, True)

def erase(PT, level, number):
    PT.sendCommand(CM.CM_DF + ' ' + CM.CM_DF_ERASE + ' ' + LevelDict[level] + ' ' + number, True)

def protect(PT, action, sector):
    if   action == 'enable':
        PT.sendCommand(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_ENABLE, True)
    elif action == 'disable':
        PT.sendCommand(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_DISABLE, True)
    elif action == 'status':
        PT.sendCommand(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_STATUS, True)
    elif action == 'all':
        for sector in range(0,64):
            PT.sendCommand(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_ADD + ' ' + str(sector), True)
    elif action == 'none':
        for sector in range(0,64):
            PT.sendCommand(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_REMOVE + ' ' + str(sector), True)
    elif action == 'add':
        PT.sendCommand(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_ADD + ' ' + sector, True)
    elif action == 'remove':
        PT.sendCommand(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_REMOVE + ' ' + sector, True)

def blankcheck(PT):
    PT.sendCommand(CM.CM_DF + ' ' + CM.CM_DF_BLANKCHECK, True)

def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')
          
def decode(PT, parameters):
    if   parameters[1] == 'status'    : status    (PT)
    elif parameters[1] == 'id'        : id        (PT)
    elif parameters[1] == 'reset'     : reset     (PT)
    elif parameters[1] == 'read'      : read      (PT, parameters[2], parameters[3])
    elif parameters[1] == 'write'     : write     (PT, parameters[2], parameters[3])
    elif parameters[1] == 'erase'     : erase     (PT, parameters[2], parameters[3])
    elif parameters[1] == 'protect'   : protect   (PT, parameters[2], parameters[3])
    elif parameters[1] == 'blankcheck': blankcheck(PT)
    else                              : unknown   (parameters)