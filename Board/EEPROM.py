import CommandMap as CM
import PyTerminal as PT


def read(address, verbal=True):
    """ Read the value from *address* in EEPROM

    Args:
        address (str): Address to be written to
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    Returns:
        int: The value at *address* in EEPROM

    """
    return int(PT.send_command(CM.CM_EEPROM + ' ' + CM.CM_EEPROM_READ + ' ' + address, verbal))


def write(address, value, verbal=True):
    """ Write *value* to *address* in EEPROM

    Args:
        address (str): Address to be written to
        value (str): Value to be written to
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_EEPROM + ' ' + CM.CM_EEPROM_WRITE + ' ' + address + ' ' + value, verbal)


def decode(parameters):
    """ Decode the command

    Args:
        parameters (list): Command in List form.

    """
    if   parameters[1] == 'read' : read (parameters[2],              )
    elif parameters[1] == 'write': write(parameters[2], parameters[3])
    else: PT.unknown(parameters)
        