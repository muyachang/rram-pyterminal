import CommandMap as CM
import PyTerminal as PT

LevelDict = {'chip'  : b'\x41'.decode('utf-8'), 
             'sector': b'\x42'.decode('utf-8'),
             'block' : b'\x43'.decode('utf-8'),
             'page'  : b'\x44'.decode('utf-8'),
             'byte'  : b'\x45'.decode('utf-8')}


def status(verbal):
    """ Get the status of the dataflash

    Keyword arguments:
    verbal -- whether to print the response or not
    """
    return PT.send_command(CM.CM_DF + ' ' + CM.CM_DF_STATUS, verbal)
    

def get_id(verbal):
    """ Get the id of the dataflash

    Keyword arguments:
    verbal -- whether to print the response or not
    """
    return PT.send_command(CM.CM_DF + ' ' + CM.CM_DF_ID, verbal)


def reset(verbal):
    """ Software reset the dataflash

    Keyword arguments:
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_DF + ' ' + CM.CM_DF_RESET, verbal)


def read(level, number, verbal):
    """ Read the data from the dataflash

    Keyword arguments:
    level -- could be 'byte', 'page', 'block', 'sector'
    number -- target number
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_DF + ' ' + CM.CM_DF_READ + ' ' + LevelDict[level] + ' ' + number, verbal)


def write(address, value, verbal):
    """ Read the data from the dataflash

    Keyword arguments:
    address -- address to be written to
    value -- value to be written to
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_DF + ' ' + CM.CM_DF_WRITE + ' ' + address + ' ' + value, verbal)


def erase(level, number, verbal):
    """ Erase the data in the dataflash

    Keyword arguments:
    level -- could be 'byte', 'page', 'block', 'sector'
    number -- target number
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_DF + ' ' + CM.CM_DF_ERASE + ' ' + LevelDict[level] + ' ' + number, verbal)


def protect(action, sector, verbal):
    """ Configure the protect function in the dataflash

    Keyword arguments:
    action -- could be 'enable', 'disable', 'status', 'all', 'none', 'add', and 'remove'
    sector -- target sector number, could be '0a', '0b', or '1'~'63'
    verbal -- whether to print the response or not
    """
    if   action == 'enable':
        PT.send_command(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_ENABLE, verbal)
    elif action == 'disable':
        PT.send_command(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_DISABLE, verbal)
    elif action == 'status':
        PT.send_command(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_STATUS, verbal)
    elif action == 'all':
        for sector in range(0, 64):
            PT.send_command(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_ADD + ' ' + str(sector), verbal)
    elif action == 'none':
        for sector in range(0, 64):
            PT.send_command(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_REMOVE + ' ' + str(sector), verbal)
    elif action == 'add':
        PT.send_command(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_ADD + ' ' + sector, verbal)
    elif action == 'remove':
        PT.send_command(CM.CM_DF + ' ' + CM.CM_DF_PROTECT + ' ' + CM.CM_DF_PROTECT_REMOVE + ' ' + sector, verbal)


def blank_check(verbal):
    """ Get the first nonzero address in the dataflash

    Keyword arguments:
    verbal -- whether to print the response or not
    """
    return PT.send_command(CM.CM_DF + ' ' + CM.CM_DF_BLANKCHECK, verbal)
          

def decode(parameters):
    """ Decode the command

    Args:
        parameters (list): Command in List form.
    """
    if   parameters[1] == 'status'     : status     (                              True)
    elif parameters[1] == 'id'         : get_id     (                              True)
    elif parameters[1] == 'reset'      : reset      (                              True)
    elif parameters[1] == 'read'       : read       (parameters[2], parameters[3], True)
    elif parameters[1] == 'write'      : write      (parameters[2], parameters[3], True)
    elif parameters[1] == 'erase'      : erase      (parameters[2], parameters[3], True)
    elif parameters[1] == 'protect'    : protect    (parameters[2], parameters[3], True)
    elif parameters[1] == 'blank_check': blank_check(                              True)
    else: PT.unknown(parameters)
