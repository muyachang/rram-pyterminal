from Lib import CommandMap as CM

DACDict = {'VTGT_BL': b'\x41'.decode('utf-8'), 
           'ADC_CAL': b'\x42'.decode('utf-8')}


def list_voltage_sources(pyterminal):
    for k, v in DACDict.items():
        response = pyterminal.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_GET + ' ' + v, False)
        value = response.split()[0] + ' mV'
        print(f' - {k:>7}: {value:}')


def increment(pyterminal, target):
    pyterminal.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_INCR + ' ' + DACDict[target], True)


def decrement(pyterminal, target):
    pyterminal.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_DECR + ' ' + DACDict[target], True)


def plus(pyterminal, value, target):
    pyterminal.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_PLUS + ' ' + value + ' ' + DACDict[target], True)


def minus(pyterminal, value, target):
    pyterminal.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_MINUS + ' ' + value + ' ' + DACDict[target], True)


def set_voltage_source(pyterminal, value, target):
    pyterminal.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_SET + ' ' + value + ' ' + DACDict[target], True)


def get_voltage_source(pyterminal, target):
    response = pyterminal.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_GET + ' ' + DACDict[target], False)
    value = response.split()[0] + ' mV'
    print(f'{target}: {value:}')   


def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')
            
            
def decode(pyterminal, parameters):
    if   parameters[1] == 'list': list_voltage_sources(pyterminal)
    elif parameters[1] == '++'  : increment           (pyterminal, parameters[2])
    elif parameters[1] == '--'  : decrement           (pyterminal, parameters[2])
    elif parameters[1] == '+'   : plus                (pyterminal, parameters[2], parameters[3])
    elif parameters[1] == '-'   : minus               (pyterminal, parameters[2], parameters[3])
    elif parameters[1] == 'set' : set_voltage_source  (pyterminal, parameters[2], parameters[3])
    elif parameters[1] == 'get' : get_voltage_source  (pyterminal, parameters[2])
    else: unknown(parameters)
