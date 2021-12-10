import CommandMap as CM
import PyTerminal as PT


def list_demos(verbal):
    """ List the available DEMO applications

    Keyword arguments:
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_DEMO + ' ' + CM.CM_DEMO_LIST, verbal)


def load(number, verbal):
    """ Load the 'target' DEMO application

    Keyword arguments:
    number -- DEMO application number, from 0~23
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_DEMO + ' ' + CM.CM_DEMO_LOAD + ' ' + number, verbal)


def run(verbal):
    """ Run the application on the testchip. (i.e. reset the testchip)

    Keyword arguments:
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_DEMO + ' ' + CM.CM_DEMO_RUN, verbal)


def analyze(verbal):
    """ Analyze the size of DEMO applications one by one, the purpose of this function was to speedup loading process

    Keyword arguments:
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_DEMO + ' ' + CM.CM_DEMO_ANALYZE, verbal)


def decode(parameters):
    """ Decode the split version of the command

    Keyword arguments:
    parameters -- split version of the command
    """
    if   parameters[1] == 'list'   : list_demos(               True)
    elif parameters[1] == 'load'   : load      (parameters[2], True)
    elif parameters[1] == 'run'    : run       (               True)
    elif parameters[1] == 'analyze': analyze   (               True)
    else: PT.unknown(parameters)
