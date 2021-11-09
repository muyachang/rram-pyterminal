from Lib import CommandMap as CM


def enable(pyterminal, target, verbal):
    """ Enable 'target' LED source

    Keyword arguments:
    pyterminal -- current connected COM port
    target -- the target LED source (could be 'TX' or 'RX')
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_LED + ' ' + CM.CM_LED_ENABLE + ' ' + target, verbal)


def disable(pyterminal, target, verbal):
    """ Disable 'target' LED source

    Keyword arguments:
    pyterminal -- current connected COM port
    target -- the target LED source (could be 'TX' or 'RX')
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_LED + ' ' + CM.CM_LED_DISABLE + ' ' + target, verbal)


def toggle(pyterminal, target, verbal):
    """ Toggle 'target' LED source

    Keyword arguments:
    pyterminal -- current connected COM port
    target -- the target LED source (could be 'TX' or 'RX')
    verbal -- whether to print the response or not
    """
    pyterminal.send_command(CM.CM_LED + ' ' + CM.CM_LED_TOGGLE + ' ' + target, verbal)


def unknown(parameters):
    """ Print out the unknown command

    Keyword arguments:
    parameters -- the split version of the command
    """
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    if   parameters[1] == 'enable' : enable (pyterminal, parameters[2], True)
    elif parameters[1] == 'disable': disable(pyterminal, parameters[2], True)
    elif parameters[1] == 'toggle' : toggle (pyterminal, parameters[2], True)
    else                           : unknown(parameters)
