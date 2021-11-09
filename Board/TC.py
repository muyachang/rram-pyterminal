from Lib import CommandMap as CM
from datetime import datetime


def connect(pyterminal, verbal):
    """ Connect to the testchip (and halt it), and get its id (should be '0x2BA01477')

    Keyword arguments:
    pyterminal -- current connected COM port
    verbal -- whether to print the response or not
    """
    return pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_CONNECT, verbal)


def disconnect(pyterminal, verbal):
    """ Unhalt from the testchip and disconnect from it

    Keyword arguments:
    pyterminal -- current connected COM port
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_DISCONNECT, verbal)


def read(pyterminal, address, verbal):
    """ Read the value from 'address'

    Keyword arguments:
    pyterminal -- current connected COM port
    address -- address to be read from
    verbal -- whether to print the response or not
    """
    return pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_READ + ' ' + address, verbal)


def write(pyterminal, address, value, verbal):
    """ Write 'value' to 'address'

    Keyword arguments:
    pyterminal -- current connected COM port
    address -- address to be written to
    value -- value to be written to
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_WRITE + ' ' + address + ' ' + value, verbal)


def list_configs(pyterminal, verbal):
    """ List the testchip configurations

    Keyword arguments:
    pyterminal -- current connected COM port
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_LIST, verbal)


def save_config(pyterminal, number, verbal):
    """ Save the testchip configuration to 'number' slot

    Keyword arguments:
    pyterminal -- current connected COM port
    number -- slot number, from 0~9
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_SAVE + ' ' + number + ' ' + datetime.now().strftime("%m/%d/%Y_%H:%M:%S"), verbal)


def load_config(pyterminal, number, verbal):
    """ Load the testchip configuration from 'number' slot

    Keyword arguments:
    pyterminal -- current connected COM port
    number -- slot number, from 0~9
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_LOAD + ' ' + number, verbal)


def unknown(parameters):
    """ Print out the unknown command

    Keyword arguments:
    parameters -- the split version of the command
    """
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    """ Decode the split version of the command

    Keyword arguments:
    pyterminal -- current connected COM port
    parameters -- split version of the command
    """
    if   parameters[1] == 'connect'   : connect     (pyterminal,                               True)
    elif parameters[1] == 'disconnect': disconnect  (pyterminal,                               True)
    elif parameters[1] == 'read'      : read        (pyterminal, parameters[2],                True)
    elif parameters[1] == 'write'     : write       (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'list'      : list_configs(pyterminal,                               True)
    elif parameters[1] == 'save'      : save_config (pyterminal, parameters[2],                True)
    elif parameters[1] == 'load'      : load_config (pyterminal, parameters[2],                True)
    else: unknown(parameters)
