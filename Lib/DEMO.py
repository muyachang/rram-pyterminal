import CommandMap as CM


def list_demos(pyterminal, verbal):
    """ List the available DEMO applications

    Keyword arguments:
    pyterminal -- current connected COM port
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_DEMO + ' ' + CM.CM_DEMO_LIST, verbal)


def load(pyterminal, number, verbal):
    """ Load the 'target' DEMO application

    Keyword arguments:
    pyterminal -- current connected COM port
    number -- DEMO application number, from 0~23
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_DEMO + ' ' + CM.CM_DEMO_LOAD + ' ' + number, verbal)


def run(pyterminal, verbal):
    """ Run the application on the testchip. (i.e. reset the testchip)

    Keyword arguments:
    pyterminal -- current connected COM port
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_DEMO + ' ' + CM.CM_DEMO_RUN, verbal)


def analyze(pyterminal, verbal):
    """ Analyze the size of DEMO applications one by one, the purpose of this function was to speedup loading process

    Keyword arguments:
    pyterminal -- current connected COM port
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_DEMO + ' ' + CM.CM_DEMO_ANALYZE, verbal)


def unknown(parameters):
    """ Print out the unknown command

    Keyword arguments:
    pyterminal -- current connected COM port
    """
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    if   parameters[1] == 'list'   : list_demos(pyterminal,                True)
    elif parameters[1] == 'load'   : load      (pyterminal, parameters[2], True)
    elif parameters[1] == 'run'    : run       (pyterminal,                True)
    elif parameters[1] == 'analyze': analyze   (pyterminal,                True)
    else: unknown(parameters)
