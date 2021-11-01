from Lib import CommandMap as CM
from datetime import datetime


def connect(pyterminal, verbal):
    pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_CONNECT, verbal)


def disconnect(pyterminal, verbal):
    pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_DISCONNECT, verbal)


def read(pyterminal, address, verbal):
    pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_READ + ' ' + address, verbal)


def write(pyterminal, address, value, verbal):
    pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_WRITE + ' ' + address + ' ' + value, verbal)


def list_configs(pyterminal, verbal):
    pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_LIST, verbal)


def save_config(pyterminal, number, verbal):
    pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_SAVE + ' ' + number + ' ' + datetime.now().strftime("%m/%d/%Y_%H:%M:%S"), verbal)


def load_config(pyterminal, number, verbal):
    pyterminal.send_command(CM.CM_TC + ' ' + CM.CM_TC_LOAD + ' ' + number, verbal)


def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    if   parameters[1] == 'connect'   : connect     (pyterminal, True)
    elif parameters[1] == 'disconnect': disconnect  (pyterminal, True)
    elif parameters[1] == 'read'      : read        (pyterminal, parameters[2], True)
    elif parameters[1] == 'write'     : write       (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'list'      : list_configs(pyterminal, True)
    elif parameters[1] == 'save'      : save_config (pyterminal, parameters[2], True)
    elif parameters[1] == 'load'      : load_config (pyterminal, parameters[2], True)
    else: unknown(parameters)
