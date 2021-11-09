import CommandMap as CM


def id(pyterminal, verbal):
    """ Get the id of the Vector module

    Keyword arguments:
    pyterminal -- current connected COM port
    verbal -- whether to print the response or not
    """
    return pyterminal.send_command(CM.CM_VECTOR + ' ' + CM.CM_VECTOR_PID, verbal)


def unknown(parameters):
    """ Print out the unknown command

    Keyword arguments:
    parameters -- the split version of the command
    """
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    if   parameters[1] == 'id'     : id(pyterminal, True)
    else: unknown(parameters)
