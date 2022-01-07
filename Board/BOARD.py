import CommandMap as CM
import PyTerminal as PT


def version(verbal=True):
    """ Return the version of Atmel firmware

    Args:
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    Returns:
        str: The version of Atmel firmware.

    """
    return PT.send_command(CM.CM_BOARD + ' ' + CM.CM_BOARD_VERSION, verbal)


def decode(parameters):
    """ Decode the command

    Args:
        parameters (list): Command in *List* form.

    """
    if   parameters[1] == 'version': version()
    else: PT.unknown(parameters)
