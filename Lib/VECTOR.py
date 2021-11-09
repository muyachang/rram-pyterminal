import CommandMap as CM


def id(pyterminal, verbal):
    return pyterminal.send_command(CM.CM_VECTOR + ' ' + CM.CM_VECTOR_PID, verbal)


def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    if   parameters[1] == 'id'     : id(pyterminal, True)
    else: unknown(parameters)
