import CommandMap as CM


def clean_input(pyterminal, verbal):
    """

    Keyword arguments:
    pyterminal -- current connected COM port
    verbal -- whether to print the response or not
    """
    return pyterminal.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_CLEAN_INPUT, verbal)


def config_input(pyterminal, address, value, verbal):
    """

    Keyword arguments:
    pyterminal -- current connected COM port
    verbal -- whether to print the response or not
    """
    return pyterminal.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_CONF_INPUT + ' ' + address + ' ' + value, verbal)


def print_input(pyterminal, verbal):
    """

    Keyword arguments:
    pyterminal -- current connected COM port
    verbal -- whether to print the response or not
    """
    return pyterminal.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_PRINT_INPUT, verbal)


def forward(pyterminal, WL, verbal):
    """

    Keyword arguments:
    pyterminal -- current connected COM port
    verbal -- whether to print the response or not
    """
    return pyterminal.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_FORWARD + ' ' + WL, verbal)


def unknown(parameters):
    """ Print out the unknown command

    Keyword arguments:
    parameters -- the split version of the command
    """
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    """ Decode the split version of the command

    Keyword arguments:
    pyterminal -- current connected COM port
    parameters -- split version of the command
    """
    if   parameters[1] == 'clean_input' : clean_input (pyterminal, True)
    elif parameters[1] == 'config_input': config_input(pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'print_input' : print_input (pyterminal, True)
    elif parameters[1] == 'forward'     : forward     (pyterminal, parameters[2], True)
    else: unknown(parameters)
