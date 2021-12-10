import CommandMap as CM
import PyTerminal as PT


def id(verbal):
    """ Get the id of the Vector module

    Keyword arguments:
    verbal -- whether to print the response or not
    """
    return PT.send_command(CM.CM_VECTOR + ' ' + CM.CM_VECTOR_PID, verbal)


def decode(parameters):
    """ Decode the split version of the command

    Keyword arguments:
    parameters -- split version of the command
    """
    if   parameters[1] == 'id'     : id(True)
    else: PT.unknown(parameters)
