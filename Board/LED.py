from Lib import CommandMap as CM


def enable(pyterminal, target):
    pyterminal.send_command(CM.CM_LED + ' ' + CM.CM_LED_ENABLE + ' ' + target, True)


def disable(pyterminal, target):
    pyterminal.send_command(CM.CM_LED + ' ' + CM.CM_LED_DISABLE + ' ' + target, True)


def toggle(pyterminal, target):
    pyterminal.send_command(CM.CM_LED + ' ' + CM.CM_LED_TOGGLE + ' ' + target, True)


def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    if   parameters[1] == 'enable' : enable (pyterminal, parameters[2])
    elif parameters[1] == 'disable': disable(pyterminal, parameters[2])
    elif parameters[1] == 'toggle' : toggle (pyterminal, parameters[2])
    else                           : unknown(parameters)
