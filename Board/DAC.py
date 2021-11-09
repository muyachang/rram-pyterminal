from Lib import CommandMap as CM

DACDict = {'VTGT_BL': b'\x41'.decode('utf-8'), 
           'ADC_CAL': b'\x42'.decode('utf-8')}


def list_sources(pyterminal):
    print('---------------------------')
    print('| Output Name | Value(mV) |')
    print('---------------------------')
    for key, value in DACDict.items():
        response = pyterminal.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_GET + ' ' + value, False)
        print(f'| {key:>11} | {response:>9} |')
    print('---------------------------')


def increment(pyterminal, target, verbal):
    pyterminal.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_INCR + ' ' + DACDict[target], verbal)


def decrement(pyterminal, target, verbal):
    pyterminal.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_DECR + ' ' + DACDict[target], verbal)


def plus(pyterminal, value, target, verbal):
    pyterminal.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_PLUS + ' ' + value + ' ' + DACDict[target], verbal)


def minus(pyterminal, value, target, verbal):
    pyterminal.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_MINUS + ' ' + value + ' ' + DACDict[target], verbal)


def set_source(pyterminal, value, target, verbal):
    pyterminal.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_SET + ' ' + value + ' ' + DACDict[target], verbal)


def get_source(pyterminal, target, verbal):
    return int(pyterminal.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_GET + ' ' + DACDict[target], verbal))


def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')
            
            
def decode(pyterminal, parameters):
    if   parameters[1] == 'list': list_sources(pyterminal                                    )
    elif parameters[1] == '++'  : increment   (pyterminal, parameters[2],                True)
    elif parameters[1] == '--'  : decrement   (pyterminal, parameters[2],                True)
    elif parameters[1] == '+'   : plus        (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == '-'   : minus       (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'set' : set_source  (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'get' : get_source  (pyterminal, parameters[2],                True)
    else: unknown(parameters)
