import CommandMap as CM

def list(PT):
    PT.sendCommand(CM.CM_DEMO + ' ' + CM.CM_DEMO_LIST, True)
        
def load(PT, target):
    PT.sendCommand(CM.CM_DEMO + ' ' + CM.CM_DEMO_LOAD + ' ' + target, True)
    
def run(PT):
    PT.sendCommand(CM.CM_DEMO + ' ' + CM.CM_DEMO_RUN, True)
    
def analyze(PT):
    PT.sendCommand(CM.CM_DEMO + ' ' + CM.CM_DEMO_ANALYZE, True)

def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')
          
def decode(PT, parameters):
    if   parameters[1] == 'list'   : list   (PT)
    elif parameters[1] == 'load'   : load   (PT, parameters[2])
    elif parameters[1] == 'run'    : run    (PT)
    elif parameters[1] == 'analyze': analyze(PT)
    else                           : unknown(parameters)