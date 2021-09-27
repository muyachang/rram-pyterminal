import CommandMap as CM


def list_demos(pyterminal):
    pyterminal.send_command(CM.CM_DEMO + ' ' + CM.CM_DEMO_LIST, True)


def load(pyterminal, target):
    pyterminal.send_command(CM.CM_DEMO + ' ' + CM.CM_DEMO_LOAD + ' ' + target, True)


def run(pyterminal):
    pyterminal.send_command(CM.CM_DEMO + ' ' + CM.CM_DEMO_RUN, True)


def analyze(pyterminal):
    pyterminal.send_command(CM.CM_DEMO + ' ' + CM.CM_DEMO_ANALYZE, True)


def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    if   parameters[1] == 'list'   : list_demos(pyterminal)
    elif parameters[1] == 'load'   : load      (pyterminal, parameters[2])
    elif parameters[1] == 'run'    : run       (pyterminal)
    elif parameters[1] == 'analyze': analyze   (pyterminal)
    else: unknown(parameters)
