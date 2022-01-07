import CommandMap as CM
import PyTerminal as PT


def id(verbal=True):
    """ Get the ID of Vector module

    Args:
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    Returns:
        str: The ID of Vector module (should be `0x03020121`)

    """
    return PT.send_command(CM.CM_VECTOR + ' ' + CM.CM_VECTOR_PID, verbal)


def decode(parameters):
    """ Decode the command

    Args:
        parameters (list): Command in List form.

    """
    if   parameters[1] == 'id'     : id()
    else: PT.unknown(parameters)
