import CommandMap as CM
import PyTerminal as PT


def enable(target, verbal):
    """ Enable 'target' LED source

    Keyword arguments:
    target -- the target LED source (could be 'TX' or 'RX')
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_LED + ' ' + CM.CM_LED_ENABLE + ' ' + target, verbal)


def disable(target, verbal):
    """ Disable 'target' LED source

    Keyword arguments:
    target -- the target LED source (could be 'TX' or 'RX')
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_LED + ' ' + CM.CM_LED_DISABLE + ' ' + target, verbal)


def toggle(target, verbal):
    """ Toggle 'target' LED source

    Keyword arguments:
    target -- the target LED source (could be 'TX' or 'RX')
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_LED + ' ' + CM.CM_LED_TOGGLE + ' ' + target, verbal)


def decode(parameters):
    """ Decode the command

    Args:
        parameters (list): Command in List form.
    """
    if   parameters[1] == 'enable' : enable (parameters[2], True)
    elif parameters[1] == 'disable': disable(parameters[2], True)
    elif parameters[1] == 'toggle' : toggle (parameters[2], True)
    else: PT.unknown(parameters)
