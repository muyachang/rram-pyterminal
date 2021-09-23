from Lib import CommandMap as CM


def read(PT, address):
    PT.sendCommand(CM.CM_EEPROM + ' ' + CM.CM_EEPROM_READ + ' ' + address, True)
        
def write(PT, address, value):
    PT.sendCommand(CM.CM_EEPROM + ' ' + CM.CM_EEPROM_WRITE + ' ' + address + ' ' + value, True)

def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')
          
def decode(PT, parameters):    
    if   parameters[1] == 'read' : read (PT, parameters[2])
    elif parameters[1] == 'write': write(PT, parameters[2], parameters[3])
    else                         : unknown(parameters)
        