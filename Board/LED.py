from Lib import CommandMap as CM


def enable(pyterminal, target, verbal):
    pyterminal.send_command(CM.CM_LED + ' ' + CM.CM_LED_ENABLE + ' ' + target, verbal)


def disable(pyterminal, target, verbal):
    pyterminal.send_command(CM.CM_LED + ' ' + CM.CM_LED_DISABLE + ' ' + target, verbal)


def toggle(pyterminal, target, verbal):
    pyterminal.send_command(CM.CM_LED + ' ' + CM.CM_LED_TOGGLE + ' ' + target, verbal)


def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    if   parameters[1] == 'enable' : enable (pyterminal, parameters[2], True)
    elif parameters[1] == 'disable': disable(pyterminal, parameters[2], True)
    elif parameters[1] == 'toggle' : toggle (pyterminal, parameters[2], True)
    else                           : unknown(parameters)
