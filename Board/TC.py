from Lib import CommandMap as CM


def connect(pyterminal, verbal):
    pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_CONNECT, verbal)


def read(pyterminal, address, verbal):
    pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_READ + ' ' + address, verbal)


def write(pyterminal, address, value, verbal):
    pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_WRITE + ' ' + address + ' ' + value, verbal)


def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    if   parameters[1] == 'connect': connect(pyterminal, True)
    elif parameters[1] == 'read'   : read   (pyterminal, parameters[2], True)
    elif parameters[1] == 'write'  : write  (pyterminal, parameters[2], parameters[3], True)
    else: unknown(parameters)
