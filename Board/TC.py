from Lib import CommandMap as CM
from datetime import datetime


def connect(pyterminal, verbal):
    return pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_CONNECT, verbal)


def disconnect(pyterminal, verbal):
    pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_DISCONNECT, verbal)


def read(pyterminal, address, verbal):
    return pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_READ + ' ' + str(address), verbal)


def write(pyterminal, address, value, verbal):
    pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_WRITE + ' ' + str(address) + ' ' + str(value), verbal)


def list_configs(pyterminal, verbal):
    pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_LIST, verbal)


def save_config(pyterminal, number, verbal):
    pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_SAVE + ' ' + str(number) + ' ' + datetime.now().strftime("%m/%d/%Y_%H:%M:%S"), verbal)


def load_config(pyterminal, number, verbal):
    pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_LOAD + ' ' + str(number), verbal)


def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    if   parameters[1] == 'connect'   : connect     (pyterminal,                                               True)
    elif parameters[1] == 'disconnect': disconnect  (pyterminal,                                               True)
    elif parameters[1] == 'read'      : read        (pyterminal, int(parameters[2], 0),                        True)
    elif parameters[1] == 'write'     : write       (pyterminal, int(parameters[2], 0), int(parameters[3], 0), True)
    elif parameters[1] == 'list'      : list_configs(pyterminal,                                               True)
    elif parameters[1] == 'save'      : save_config (pyterminal, int(parameters[2]   ),                        True)
    elif parameters[1] == 'load'      : load_config (pyterminal, int(parameters[2]   ),                        True)
    else: unknown(parameters)
