from Lib import CommandMap as CM


def connect(PT):
    response = PT.sendCommand(CM.CM_TC + ' ' + CM.CM_TC_CONNECT, False)
    print('Testchip ID: ' + response.split()[0])
    
def read(PT, address):
    PT.sendCommand(CM.CM_TC + ' ' + CM.CM_TC_READ + ' ' + address, True)

def write(PT, address, value):
    PT.sendCommand(CM.CM_TC + ' ' + CM.CM_TC_WRITE + ' ' + address + ' ' + value, True)

def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')
          
def decode(PT, parameters):
    if   parameters[1] == 'connect': connect(PT)
    elif parameters[1] == 'read'   : read   (PT, parameters[2])
    elif parameters[1] == 'write'  : write  (PT, parameters[2], parameters[3])
    else                           : unknown(parameters)