from Lib import CommandMap as CM


def connect(pyterminal):
    response = pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_CONNECT, False)
    print('Testchip ID: ' + response.split()[0])


def read(pyterminal, address):
    pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_READ + ' ' + address, True)


def write(pyterminal, address, value):
    pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_WRITE + ' ' + address + ' ' + value, True)


def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    if   parameters[1] == 'connect': connect(pyterminal)
    elif parameters[1] == 'read'   : read   (pyterminal, parameters[2])
    elif parameters[1] == 'write'  : write  (pyterminal, parameters[2], parameters[3])
    else: unknown(parameters)
