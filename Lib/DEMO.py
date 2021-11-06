import CommandMap as CM


def list_demos(pyterminal, verbal):
    pyterminal.send_command(CM.CM_DEMO + ' ' + CM.CM_DEMO_LIST, verbal)


def load(pyterminal, target, verbal):
    pyterminal.send_command(CM.CM_DEMO + ' ' + CM.CM_DEMO_LOAD + ' ' + str(target), verbal)


def run(pyterminal, verbal):
    pyterminal.send_command(CM.CM_DEMO + ' ' + CM.CM_DEMO_RUN, verbal)


def analyze(pyterminal, verbal):
    pyterminal.send_command(CM.CM_DEMO + ' ' + CM.CM_DEMO_ANALYZE, verbal)


def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    if   parameters[1] == 'list'   : list_demos(pyterminal,                     True)
    elif parameters[1] == 'load'   : load      (pyterminal, int(parameters[2]), True)
    elif parameters[1] == 'run'    : run       (pyterminal,                     True)
    elif parameters[1] == 'analyze': analyze   (pyterminal,                     True)
    else: unknown(parameters)
