import CommandMap as CM
import PyTerminal as PT


def id(verbal):
    """ Get the ID of Vector module

    Args:
        verbal (bool): Whether to print the response or not.
    Returns:
        The ID of Vector module
    """
    return PT.send_command(CM.CM_VECTOR + ' ' + CM.CM_VECTOR_PID, verbal)


def decode(parameters):
    """ Decode the command

    Args:
        parameters (list): Command in List form.
    """
    if   parameters[1] == 'id'     : id(True)
    else: PT.unknown(parameters)
