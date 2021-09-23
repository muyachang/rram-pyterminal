from Lib import CommandMap as CM


def enable(PT, target):
    PT.sendCommand(CM.CM_LED + ' ' + CM.CM_LED_ENABLE + ' ' + target, True)
        
def disable(PT, target):
    PT.sendCommand(CM.CM_LED + ' ' + CM.CM_LED_DISABLE + ' ' + target, True)
    
def toggle(PT, target):
    PT.sendCommand(CM.CM_LED + ' ' + CM.CM_LED_TOGGLE + ' ' + target, True)

def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')
          
def decode(PT, parameters):    
    if   parameters[1] == 'enable' : enable (PT, parameters[2])
    elif parameters[1] == 'disable': disable(PT, parameters[2])
    elif parameters[1] == 'toggle' : toggle (PT, parameters[2])
    else                           : unknown(parameters)