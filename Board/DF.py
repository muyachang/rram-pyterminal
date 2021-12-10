import CommandMap as CM
import PyTerminal as PT

dict = {'chip'  : b'\x41'.decode('utf-8'),
        'sector': b'\x42'.decode('utf-8'),
        'block' : b'\x43'.decode('utf-8'),
        'page'  : b'\x44'.decode('utf-8'),
        'byte'  : b'\x45'.decode('utf-8')}
"""Dataflash memory hierarchy dictionary from *string* to *ASCII*"""


def status(verbal):
    """ Get the status of dataflash

    Args:
        verbal (bool): Whether to print the response or not.
    Returns:
        The status of dataflash
    """
    return PT.send_command(CM.CM_DF + ' ' + CM.CM_DF_STATUS, verbal)
    

def get_id(verbal):
    """ Get the ID of dataflash

    Args:
        verbal (bool): Whether to print the response or not.
    Returns:
        The ID of dataflash
    """
    return PT.send_command(CM.CM_DF + ' ' + CM.CM_DF_ID, verbal)


def reset(verbal):
    """ Software reset the dataflash

    Args:
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DF + ' ' + CM.CM_DF_RESET, verbal)


def read(level, number, verbal):
    """ Read the data from dataflash

    Args:
        level (str): Could be *byte*, *page*, *block*, *sector*
        number (str): Target number
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DF + ' ' + CM.CM_DF_READ + ' ' + dict[level] + ' ' + number, verbal)


def write(address, value, verbal):
    """ Read the data from the dataflash

    Args:
        address (str): Address to be written to
        value (str): Value to be written to
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DF + ' ' + CM.CM_DF_WRITE + ' ' + address + ' ' + value, verbal)


def erase(level, number, verbal):
    """ Erase the data in dataflash

    Args:
        level (str): Could be *byte*, *page*, *block*, *sector*
        number (str): Target number
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DF + ' ' + CM.CM_DF_ERASE + ' ' + dict[level] + ' ' + number, verbal)


def protect(action, sector, verbal):
    """ Configure the protect function in the dataflash

    Args:
        action (str): Could be *enable*, *disable*, *status*, *all*, *none*, *add*, and *remove*
        sector (str): Target sector number, could be *0a*, *0b*, or *1*~*63*
        verbal (bool): Whether to print the response or not.
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
    """ Get the first nonzero address in dataflash

    Args:
        verbal (bool): Whether to print the response or not.
    Returns:
        The first nonzero address in dataflash
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
