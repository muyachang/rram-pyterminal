import CommandMap as CM
import PyTerminal as PT


def enable(target, verbal=True):
    """ Enable *target*

    Args:
        target (str): The target LED source (could be *TX* or *RX*)
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_LED + ' ' + CM.CM_LED_ENABLE + ' ' + target, verbal)


def disable(target, verbal=True):
    """ Disable *target*

    Args:
        target (str): The target LED source (could be *TX* or *RX*)
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_LED + ' ' + CM.CM_LED_DISABLE + ' ' + target, verbal)


def toggle(target, verbal=True):
    """ Toggle *target*

    Args:
        target (str): The target LED source (could be *TX* or *RX*)
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_LED + ' ' + CM.CM_LED_TOGGLE + ' ' + target, verbal)


def decode(parameters):
    """ Decode the command

    Args:
        parameters (list): Command in List form.

    """
    if   parameters[1] == 'enable' : enable (parameters[2])
    elif parameters[1] == 'disable': disable(parameters[2])
    elif parameters[1] == 'toggle' : toggle (parameters[2])
    else: PT.unknown(parameters)
