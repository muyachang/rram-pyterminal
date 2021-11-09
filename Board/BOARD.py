from Lib import CommandMap as CM


def version(pyterminal, verbal):
    """ Return the version of Atmel firmware

    Keyword arguments:
    pyterminal -- current connected COM port
    verbal -- whether to print the response or not
    """
    return pyterminal.send_command(CM.CM_BOARD + ' ' + CM.CM_BOARD_VERSION, verbal)


def unknown(parameters):
    """ Print out the unknown command

    Keyword arguments:
    parameters -- the split version of the command
    """
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    if   parameters[1] == 'version': version(pyterminal, True)
    else: unknown(parameters)
