from Lib import CommandMap as CM


def version(pyterminal):
    pyterminal.send_command(CM.CM_BOARD + ' ' + CM.CM_BOARD_VERSION, True)

def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    if   parameters[1] == 'version': version(pyterminal)
    else: unknown(parameters)
        