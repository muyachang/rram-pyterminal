import CommandMap as CM
import PyTerminal as PT

DACDict = {'VTGT_BL': b'\x41'.decode('utf-8'), 
           'ADC_CAL': b'\x42'.decode('utf-8')}


def list_sources():
    """ List the available DAC sources

    Args:
    """
    print('---------------------------')
    print('| Output Name | Value(mV) |')
    print('---------------------------')
    for key, value in DACDict.items():
        response = PT.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_GET + ' ' + value, False)
        print(f'| {key:>11} | {response:>9} |')
    print('---------------------------')


def save(verbal):
    """ Save the current levels of the DAC to the EEPROM

    Args:
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_SAVE, verbal)


def load(verbal):
    """ Load the current levels of the DAC from the EEPROM

    Args:
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_LOAD, verbal)


def increment(target, verbal):
    """ Increase the 'target' source by 1 in it's binary format

    Args:
        target (str): The target source, could be 'VTGT_BL' or 'ADC_CAL'
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_INCR + ' ' + DACDict[target], verbal)


def decrement(target, verbal):
    """ Decrease the 'target' source by 1 in it's binary format

    Args:
        target (str): The target source, could be 'VTGT_BL' or 'ADC_CAL'
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_DECR + ' ' + DACDict[target], verbal)


def plus(value, target, verbal):
    """ Increase 'target' source by 'value' mV

    Args:
        value (str): Voltage (mV)
        target (str): The target source, could be 'VTGT_BL' or 'ADC_CAL'
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_PLUS + ' ' + value + ' ' + DACDict[target], verbal)


def minus(value, target, verbal):
    """ Decrease 'target' source by 'value' mV

    Args:
        value (str): Voltage (mV)
        target (str): The target source, could be 'VTGT_BL' or 'ADC_CAL'
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_MINUS + ' ' + value + ' ' + DACDict[target], verbal)


def set_source(value, target, verbal):
    """ Set 'target' source to 'value' mV

    Args:
        value (str): Voltage (mV)
        target (str): The target source, could be 'VTGT_BL' or 'ADC_CAL'
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_SET + ' ' + value + ' ' + DACDict[target], verbal)


def get_source(target, verbal):
    """ Get the current voltage value of 'target' source

    Args:
        target (str): The target source, could be 'VTGT_BL' or 'ADC_CAL'
        verbal (bool): Whether to print the response or not.
    Returns:
        The current voltage value of 'target' source
    """
    return int(PT.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_GET + ' ' + DACDict[target], verbal))
            
            
def decode(parameters):
    """ Decode the command

    Args:
        parameters (list): Command in List form.
    """
    if   parameters[1] == 'list': list_sources(                                  )
    elif parameters[1] == 'save': save        (                              True)
    elif parameters[1] == 'load': load        (                              True)
    elif parameters[1] == '++'  : increment   (parameters[2],                True)
    elif parameters[1] == '--'  : decrement   (parameters[2],                True)
    elif parameters[1] == '+'   : plus        (parameters[2], parameters[3], True)
    elif parameters[1] == '-'   : minus       (parameters[2], parameters[3], True)
    elif parameters[1] == 'set' : set_source  (parameters[2], parameters[3], True)
    elif parameters[1] == 'get' : get_source  (parameters[2],                True)
    else: pyterminal.unknown(parameters)
