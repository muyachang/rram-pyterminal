import CommandMap as CM
import PyTerminal as PT

dict = {'VTGT_BL': b'\x41'.decode('utf-8'),
        'ADC_CAL': b'\x42'.decode('utf-8')}
"""DAC output source dictionary from *string* to *ASCII*"""

def list_sources():
    """ List the available DAC output sources

    """
    print('╔═════════════╦═══════════╗')
    print('║ Output Name ║ Value(mV) ║')
    print('╟─────────────╫───────────╢')
    for key, value in dict.items():
        response = PT.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_GET + ' ' + value, False)
        print(f'║ {key:>11} ║ {response:>9} ║')
    print('╚═════════════╩═══════════╝')


def save(verbal=True):
    """ Save the current levels of the DAC output sources to EEPROM

    Args:
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_SAVE, verbal)


def load(verbal=True):
    """ Load the current levels of the DAC output sources from EEPROM

    Args:
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_LOAD, verbal)


def increment(target, verbal=True):
    """ Increase *target* by 1 in it's binary format

    Args:
        target (str): The target output source, could be *VTGT_BL* or *ADC_CAL*
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_INCR + ' ' + dict[target], verbal)


def decrement(target, verbal=True):
    """ Decrease *target* by 1 in it's binary format

    Args:
        target (str): The target output source, could be *VTGT_BL* or *ADC_CAL*
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_DECR + ' ' + dict[target], verbal)


def plus(value, target, verbal=True):
    """ Increase *target* by *value* mV

    Args:
        value (str): Voltage (mV)
        target (str): The target output source, could be *VTGT_BL* or *ADC_CAL*
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_PLUS + ' ' + value + ' ' + dict[target], verbal)


def minus(value, target, verbal=True):
    """ Decrease *target* by *value* mV

    Args:
        value (str): Voltage (mV)
        target (str): The target output source, could be *VTGT_BL* or *ADC_CAL*
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_MINUS + ' ' + value + ' ' + dict[target], verbal)


def set_source(value, target, verbal=True):
    """ Set *target* to *value* mV

    Args:
        value (str): Voltage (mV)
        target (str): The target output source, could be *VTGT_BL* or *ADC_CAL*
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_SET + ' ' + value + ' ' + dict[target], verbal)


def get_source(target, verbal=True):
    """ Get the current voltage value of *target*

    Args:
        target (str): The target output source, could be *VTGT_BL* or *ADC_CAL*
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    Returns:
        int: The current voltage value of *target*

    """
    return int(PT.send_command(CM.CM_DAC + ' ' + CM.CM_DAC_GET + ' ' + dict[target], verbal))
            
            
def decode(parameters):
    """ Decode the command

    Args:
        parameters (list): Command in List form.

    """
    if   parameters[1] == 'list': list_sources(                            )
    elif parameters[1] == 'save': save        (                            )
    elif parameters[1] == 'load': load        (                            )
    elif parameters[1] == '++'  : increment   (parameters[2],              )
    elif parameters[1] == '--'  : decrement   (parameters[2],              )
    elif parameters[1] == '+'   : plus        (parameters[2], parameters[3])
    elif parameters[1] == '-'   : minus       (parameters[2], parameters[3])
    elif parameters[1] == 'set' : set_source  (parameters[2], parameters[3])
    elif parameters[1] == 'get' : get_source  (parameters[2],              )
    else: PT.unknown(parameters)
