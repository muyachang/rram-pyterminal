import CommandMap as CM
import PyTerminal as PT

def version(verbal):
    """ Return the version of Atmel firmware

    Args:
        verbal (bool): Whether to print the response or not.
    Returns:
        The version of Atmel firmware Modules.
    """
    return PT.send_command(CM.CM_BOARD + ' ' + CM.CM_BOARD_VERSION, verbal)


def decode(parameters):
    """ Decode the command

    Args:
        parameters (list): Command in List form.
    """
    if   parameters[1] == 'version': version(True)
    else: PT.unknown(parameters)
