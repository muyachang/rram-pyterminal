from Lib import CommandMap as CM


def read(pyterminal, address, verbal):
    """ Read the value from 'address'

    Keyword arguments:
    pyterminal -- current connected COM port
    address -- address to be read from
    verbal -- whether to print the response or not
    """
    return pyterminal.send_command(CM.CM_EEPROM + ' ' + CM.CM_EEPROM_READ + ' ' + address, verbal)


def write(pyterminal, address, value, verbal):
    """ Write 'value' to 'address'

    Keyword arguments:
    pyterminal -- current connected COM port
    address -- address to be written to
    value -- value to be written to
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_EEPROM + ' ' + CM.CM_EEPROM_WRITE + ' ' + address + ' ' + value, verbal)


def unknown(parameters):
    """ Print out the unknown command

    Keyword arguments:
    pyterminal -- current connected COM port
    """
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    if   parameters[1] == 'read' : read (pyterminal, parameters[2],                True)
    elif parameters[1] == 'write': write(pyterminal, parameters[2], parameters[3], True)
    else: unknown(parameters)
        