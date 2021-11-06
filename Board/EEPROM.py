from Lib import CommandMap as CM


def read(pyterminal, address, verbal):
    return pyterminal.send_command(CM.CM_EEPROM + ' ' + CM.CM_EEPROM_READ + ' ' + str(address), verbal)


def write(pyterminal, address, value, verbal):
    pyterminal.send_command(CM.CM_EEPROM + ' ' + CM.CM_EEPROM_WRITE + ' ' + str(address) + ' ' + str(value), verbal)


def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    if   parameters[1] == 'read' : read (pyterminal, int(parameters[2], 0),                        True)
    elif parameters[1] == 'write': write(pyterminal, int(parameters[2], 0), int(parameters[3], 0), True)
    else: unknown(parameters)
        