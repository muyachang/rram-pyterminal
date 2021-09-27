from Lib import CommandMap as CM

VoltDict = {'3V3'      : b'\x41'.decode('utf-8'), 
            'AVDD_WR'  : b'\x42'.decode('utf-8'),
            'AVDD_WL'  : b'\x43'.decode('utf-8'),
            'AVDD_RRAM': b'\x44'.decode('utf-8'),
            'VDD'      : b'\x45'.decode('utf-8'),
            'AVDD_SRAM': b'\x46'.decode('utf-8')}
            

def list_sources(pyterminal):
    for k, v in VoltDict.items():
        response = pyterminal.send_command(CM.CM_PM + ' ' + CM.CM_PM_GET + ' ' + v, False)
        source_status = 'ON' if response.split()[0] == '1' else 'OFF'
        value = 'unadjustable' if response.split()[1] == '-1' else response.split()[1] + ' mV'
        print(f' - {k:>10}({source_status:>3}): {value:}')


def clear(pyterminal):
    pyterminal.send_command(CM.CM_PM + ' ' + CM.CM_PM_CLEAR, True)


def status(pyterminal):
    pyterminal.send_command(CM.CM_PM + ' ' + CM.CM_PM_STATUS, True)


def save(pyterminal):
    pyterminal.send_command(CM.CM_PM + ' ' + CM.CM_PM_SAVE, True)
    

def load(pyterminal):
    pyterminal.send_command(CM.CM_PM + ' ' + CM.CM_PM_LOAD, True)
    

def allon(pyterminal):
    for k, v in VoltDict.items():
        pyterminal.send_command(CM.CM_PM + ' ' + CM.CM_PM_ENABLE + ' ' + v, True)
        

def alloff(pyterminal):
    for k, v in VoltDict.items():
        pyterminal.send_command(CM.CM_PM + ' ' + CM.CM_PM_DISABLE + ' ' + v, True)
    

def reset(pyterminal):
    pyterminal.send_command(CM.CM_PM + ' ' + CM.CM_PM_RESET, True)
    

def enable(pyterminal, target):
    pyterminal.send_command(CM.CM_PM + ' ' + CM.CM_PM_ENABLE + ' ' + VoltDict[target], True)
    

def disable(pyterminal, target):
    pyterminal.send_command(CM.CM_PM + ' ' + CM.CM_PM_DISABLE + ' ' + VoltDict[target], True)
    

def increment(pyterminal, target):
    pyterminal.send_command(CM.CM_PM + ' ' + CM.CM_PM_INCR + ' ' + VoltDict[target], True)
    

def decrement(pyterminal, target):
    pyterminal.send_command(CM.CM_PM + ' ' + CM.CM_PM_DECR + ' ' + VoltDict[target], True)
    

def plus(pyterminal, value, target):
    pyterminal.send_command(CM.CM_PM + ' ' + CM.CM_PM_PLUS + ' ' + value + ' ' + VoltDict[target], True)
    

def minus(pyterminal, value, target):
    pyterminal.send_command(CM.CM_PM + ' ' + CM.CM_PM_MINUS + ' ' + value + ' ' + VoltDict[target], True)
    

def set_source(pyterminal, value, target):
    pyterminal.send_command(CM.CM_PM + ' ' + CM.CM_PM_SET + ' ' + value + ' ' + VoltDict[target], True)
    

def get_source(pyterminal, target):
    response = pyterminal.send_command(CM.CM_PM + ' ' + CM.CM_PM_GET + ' ' + VoltDict[target], False)
    source_status = 'ON' if response.split()[0] == '1' else 'OFF'
    value = 'unadjustable' if response.split()[1] == '-1' else response.split()[1] + ' mV'
    print(f'{target}({source_status}): {value:}')


def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')
        

def decode(pyterminal, parameters):
    if   parameters[1] == 'list'   : list_sources(pyterminal)
    elif parameters[1] == 'clear'  : clear       (pyterminal)
    elif parameters[1] == 'status' : status      (pyterminal)
    elif parameters[1] == 'save'   : save        (pyterminal)
    elif parameters[1] == 'load'   : load        (pyterminal)
    elif parameters[1] == 'allon'  : allon       (pyterminal)
    elif parameters[1] == 'alloff' : alloff      (pyterminal)
    elif parameters[1] == 'reset'  : reset       (pyterminal)
    elif parameters[1] == 'enable' : enable      (pyterminal, parameters[2])
    elif parameters[1] == 'disable': disable     (pyterminal, parameters[2])
    elif parameters[1] == '++'     : increment   (pyterminal, parameters[2])
    elif parameters[1] == '--'     : decrement   (pyterminal, parameters[2])
    elif parameters[1] == '+'      : plus        (pyterminal, parameters[2], parameters[3])
    elif parameters[1] == '-'      : minus       (pyterminal, parameters[2], parameters[3])
    elif parameters[1] == 'set'    : set_source  (pyterminal, parameters[2], parameters[3])
    elif parameters[1] == 'get'    : get_source  (pyterminal, parameters[2])
    else: unknown(parameters)
    