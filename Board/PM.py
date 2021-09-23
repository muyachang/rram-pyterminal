from Lib import CommandMap as CM

VoltDict = {'3V3'      : b'\x41'.decode('utf-8'), 
            'AVDD_WR'  : b'\x42'.decode('utf-8'),
            'AVDD_WL'  : b'\x43'.decode('utf-8'),
            'AVDD_RRAM': b'\x44'.decode('utf-8'),
            'VDD'      : b'\x45'.decode('utf-8'),
            'AVDD_SRAM': b'\x46'.decode('utf-8')}
            
def list(PT):
    for k, v in VoltDict.items():
        response = PT.sendCommand(CM.CM_PM + ' ' + CM.CM_PM_GET + ' ' + v, False)
        status = 'ON' if response.split()[0] == '1' else 'OFF'
        value = 'unadjustable' if response.split()[1] == '-1' else response.split()[1] + ' mV'
        print(f' - {k:>10}({status:>3}): {value:}')

def clear(PT):
    PT.sendCommand(CM.CM_PM + ' ' + CM.CM_PM_CLEAR, True)

def status(PT):
    PT.sendCommand(CM.CM_PM + ' ' + CM.CM_PM_STATUS, True)

def save(PT):
    PT.sendCommand(CM.CM_PM + ' ' + CM.CM_PM_SAVE, True)
    
def load(PT):
    PT.sendCommand(CM.CM_PM + ' ' + CM.CM_PM_LOAD, True)
    
def allon(PT):
    for k, v in VoltDict.items():
        PT.sendCommand(CM.CM_PM + ' ' + CM.CM_PM_ENABLE + ' ' + v, True)
        
def alloff(PT):
    for k, v in VoltDict.items():
        PT.sendCommand(CM.CM_PM + ' ' + CM.CM_PM_DISABLE + ' ' + v, True)
    
def reset(PT):
    PT.sendCommand(CM.CM_PM + ' ' + CM.CM_PM_RESET, True)
    
def enable(PT, target):
    PT.sendCommand(CM.CM_PM + ' ' + CM.CM_PM_ENABLE + ' ' + VoltDict[target], True)
    
def disable(PT, target):
    PT.sendCommand(CM.CM_PM + ' ' + CM.CM_PM_DISABLE + ' ' + VoltDict[target], True)
    
def increment(PT, target):
    PT.sendCommand(CM.CM_PM + ' ' + CM.CM_PM_INCR + ' ' + VoltDict[target], True)
    
def decrement(PT, target):
    PT.sendCommand(CM.CM_PM + ' ' + CM.CM_PM_DECR + ' ' + VoltDict[target], True)
    
def plus(PT, value, target):
    PT.sendCommand(CM.CM_PM + ' ' + CM.CM_PM_PLUS + ' ' + value + ' ' + VoltDict[target], True)
    
def minus(PT, value, target):
    PT.sendCommand(CM.CM_PM + ' ' + CM.CM_PM_MINUS + ' ' + value + ' ' + VoltDict[target], True)
    
def set(PT, value, target):
    PT.sendCommand(CM.CM_PM + ' ' + CM.CM_PM_SET + ' ' + value + ' ' + VoltDict[target], True)
    
def get(PT, target):
    response = PT.sendCommand(CM.CM_PM + ' ' + CM.CM_PM_GET + ' ' + VoltDict[target], False)
    status = 'ON' if response.split()[0] == '1' else 'OFF'
    value = 'unadjustable' if response.split()[1] == '-1' else response.split()[1] + ' mV'
    print(f'{target}({status}): {value:}')

def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')
        
def decode(PT, parameters):  
    if   parameters[1] == 'list'   : list     (PT)    
    elif parameters[1] == 'clear'  : clear    (PT)    
    elif parameters[1] == 'status' : status   (PT)    
    elif parameters[1] == 'save'   : save     (PT)        
    elif parameters[1] == 'load'   : load     (PT)        
    elif parameters[1] == 'allon'  : allon    (PT)            
    elif parameters[1] == 'alloff' : alloff   (PT)        
    elif parameters[1] == 'reset'  : reset    (PT)        
    elif parameters[1] == 'enable' : enable   (PT, parameters[2])        
    elif parameters[1] == 'disable': disable  (PT, parameters[2])        
    elif parameters[1] == '++'     : increment(PT, parameters[2])        
    elif parameters[1] == '--'     : decrement(PT, parameters[2])        
    elif parameters[1] == '+'      : plus     (PT, parameters[2], parameters[3])        
    elif parameters[1] == '-'      : minus    (PT, parameters[2], parameters[3])        
    elif parameters[1] == 'set'    : set      (PT, parameters[2], parameters[3])        
    elif parameters[1] == 'get'    : get      (PT, parameters[2])
    else                           : unknown  (parameters)
    