from Lib import CommandMap as CM


def read(pyterminal, address):
    pyterminal.send_command(CM.CM_EEPROM + ' ' + CM.CM_EEPROM_READ + ' ' + address, True)


def write(pyterminal, address, value):
    pyterminal.send_command(CM.CM_EEPROM + ' ' + CM.CM_EEPROM_WRITE + ' ' + address + ' ' + value, True)


def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    if   parameters[1] == 'read' : read (pyterminal, parameters[2])
    elif parameters[1] == 'write': write(pyterminal, parameters[2], parameters[3])
    else: unknown(parameters)
        