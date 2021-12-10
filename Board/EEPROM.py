import CommandMap as CM
import PyTerminal as PT


def read(address, verbal):
    """ Read the value from *address*

    Args:
        address (str): Address to be written to
        verbal (bool): Whether to print the response or not.
    Returns:
        The status of dataflash
    """
    return PT.send_command(CM.CM_EEPROM + ' ' + CM.CM_EEPROM_READ + ' ' + address, verbal)


def write(address, value, verbal):
    """ Write *value* to *address*

    Args:
        address (str): Address to be written to
        value (str): Value to be written to
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_EEPROM + ' ' + CM.CM_EEPROM_WRITE + ' ' + address + ' ' + value, verbal)


def decode(parameters):
    """ Decode the command

    Args:
        parameters (list): Command in List form.
    """
    if   parameters[1] == 'read' : read (parameters[2],                True)
    elif parameters[1] == 'write': write(parameters[2], parameters[3], True)
    else: PT.unknown(parameters)
        