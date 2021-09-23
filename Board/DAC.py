from Lib import CommandMap as CM

DACDict = {'VTGT_BL': b'\x41'.decode('utf-8'), 
           'ADC_CAL': b'\x42'.decode('utf-8')}
            
def list(PT):
    for k, v in DACDict.items():
        response = PT.sendCommand(CM.CM_DAC + ' ' + CM.CM_DAC_GET + ' ' + v, False)
        value = response.split()[0] + ' mV'
        print(f' - {k:>7}: {value:}')
        
def increment(PT, target):
  PT.sendCommand(CM.CM_DAC + ' ' + CM.CM_DAC_INCR + ' ' + DACDict[target], True)
  
def decrement(PT, target):
  PT.sendCommand(CM.CM_DAC + ' ' + CM.CM_DAC_DECR + ' ' + DACDict[target], True)
  
def plus(PT, value, target):
  PT.sendCommand(CM.CM_DAC + ' ' + CM.CM_DAC_PLUS + ' ' + value + ' ' + DACDict[target], True)
  
def minus(PT, value, target):
  PT.sendCommand(CM.CM_DAC + ' ' + CM.CM_DAC_MINUS + ' ' + value + ' ' + DACDict[target], True)
  
def set(PT, value, target):
  PT.sendCommand(CM.CM_DAC + ' ' + CM.CM_DAC_SET + ' ' + value + ' ' + DACDict[target], True)
  
def get(PT, target):
    response = PT.sendCommand(CM.CM_DAC + ' ' + CM.CM_DAC_GET + ' ' + DACDict[target], False)
    value = response.split()[0] + ' mV'
    print(f'{target}: {value:}')   

def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')
            
            
def decode(PT, parameters):
    if   parameters[1] == 'list': list     (PT)
    elif parameters[1] == '++'  : increment(PT, parameters[2])        
    elif parameters[1] == '--'  : decrement(PT, parameters[2])        
    elif parameters[1] == '+'   : plus     (PT, parameters[2], parameters[3])        
    elif parameters[1] == '-'   : minus    (PT, parameters[2], parameters[3])       
    elif parameters[1] == 'set' : set      (PT, parameters[2], parameters[3])        
    elif parameters[1] == 'get' : get      (PT, parameters[2])
    else                        : unknown  (parameters)

    