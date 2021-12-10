from datetime import datetime
import CommandMap as CM
import PyTerminal as PT


def connect(verbal):
    """ Connect to the testchip (and halt it), and get its id (should be '0x2BA01477')

    Keyword arguments:
    verbal -- whether to print the response or not
    """
    return PT.send_command(CM.CM_TC + ' ' + CM.CM_TC_CONNECT, verbal)


def disconnect(verbal):
    """ Unhalt from the testchip and disconnect from it

    Keyword arguments:
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_TC + ' ' + CM.CM_TC_DISCONNECT, verbal)


def read(address, verbal):
    """ Read the value from 'address'

    Keyword arguments:
    address -- address to be read from
    verbal -- whether to print the response or not
    """
    return PT.send_command(CM.CM_TC + ' ' + CM.CM_TC_READ + ' ' + address, verbal)


def write(address, value, verbal):
    """ Write 'value' to 'address'

    Keyword arguments:
    address -- address to be written to
    value -- value to be written to
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_TC + ' ' + CM.CM_TC_WRITE + ' ' + address + ' ' + value, verbal)


def list_configs(verbal):
    """ List the testchip configurations

    Keyword arguments:
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_TC + ' ' + CM.CM_TC_LIST, verbal)


def save_config(number, verbal):
    """ Save the testchip configuration to 'number' slot

    Keyword arguments:
    number -- slot number, from 0~9
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_TC + ' ' + CM.CM_TC_SAVE + ' ' + number + ' ' + datetime.now().strftime("%m/%d/%Y_%H:%M:%S"), verbal)


def load_config(number, verbal):
    """ Load the testchip configuration from 'number' slot

    Keyword arguments:
    number -- slot number, from 0~9
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_TC + ' ' + CM.CM_TC_LOAD + ' ' + number, verbal)


def decode(parameters):
    """ Decode the command

    Args:
        parameters (list): Command in List form.
    """
    if   parameters[1] == 'connect'   : connect     (                              True)
    elif parameters[1] == 'disconnect': disconnect  (                              True)
    elif parameters[1] == 'read'      : read        (parameters[2],                True)
    elif parameters[1] == 'write'     : write       (parameters[2], parameters[3], True)
    elif parameters[1] == 'list'      : list_configs(                              True)
    elif parameters[1] == 'save'      : save_config (parameters[2],                True)
    elif parameters[1] == 'load'      : load_config (parameters[2],                True)
    else: PT.unknown(parameters)
