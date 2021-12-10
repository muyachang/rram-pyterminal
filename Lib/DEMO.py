import CommandMap as CM
import PyTerminal as PT


def list_demos(verbal):
    """ List the available DEMO applications

    Args:
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DEMO + ' ' + CM.CM_DEMO_LIST, verbal)


def load(number, verbal):
    """ Load DEMO application #*number*

    Args:
        number (str): DEMO application number, from *0*~*23*
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DEMO + ' ' + CM.CM_DEMO_LOAD + ' ' + number, verbal)


def run(verbal):
    """ Run the application on the testchip. (i.e. reset the testchip)

    Args:
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DEMO + ' ' + CM.CM_DEMO_RUN, verbal)


def analyze(verbal):
    """ Analyze the sizes of DEMO applications to speedup the loading process

    Args:
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DEMO + ' ' + CM.CM_DEMO_ANALYZE, verbal)


def decode(parameters):
    """ Decode the command

    Args:
        parameters (list): Command in List form.
    """
    if   parameters[1] == 'list'   : list_demos(               True)
    elif parameters[1] == 'load'   : load      (parameters[2], True)
    elif parameters[1] == 'run'    : run       (               True)
    elif parameters[1] == 'analyze': analyze   (               True)
    else: PT.unknown(parameters)
