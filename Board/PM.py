import CommandMap as CM
import PyTerminal as PT

VoltDict = {'3V3'      : b'\x41'.decode('utf-8'), 
            'AVDD_WR'  : b'\x42'.decode('utf-8'),
            'AVDD_WL'  : b'\x43'.decode('utf-8'),
            'AVDD_RRAM': b'\x44'.decode('utf-8'),
            'VDD'      : b'\x45'.decode('utf-8'),
            'AVDD_SRAM': b'\x46'.decode('utf-8')}
"""Voltage output dictionary from *string* to *ASCII*"""
            

def list_sources():
    """ List the available voltage sources

    """
    print('╔═════════════╦════════╦════════════╗')
    print('║ Output Name ║ Status ║ Value (mV) ║')
    print('╟─────────────╫────────╫────────────╢')
    for key, value in VoltDict.items():
        response = PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_GET + ' ' + value, False)
        output_status = 'On' if response.split()[0] == '1' else 'Off'
        output_value = 'Analog' if response.split()[1] == '-1' else response.split()[1]
        print(f'║ {key:>11} ║ {output_status:>6} ║ {output_value:>10} ║')
    print('╚═════════════╩════════╩════════════╝')


def clear(verbal=True):
    """ Clear the interrupt register in the voltage regulator

    Args:
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_CLEAR, verbal)


def status(verbal=True):
    """ Get the current status of the voltage regulator

    Args:
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    Returns:
        str: The current status of the voltage regulator

    """
    return PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_STATUS, verbal)


def save(verbal=True):
    """ Save the current configuration of the voltage regulator to the EEPROM

    Args:
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_SAVE, verbal)
    

def load(verbal=True):
    """ Load the configuration of the voltage regulator from the EEPROM

    Args:
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_LOAD, verbal)
    

def enable_all(verbal=True):
    """ Enable all the voltage sources

    Args:
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    for k, v in VoltDict.items():
        PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_ENABLE + ' ' + v, verbal)
        

def disable_all(verbal=True):
    """ Disable all the voltage sources

    Args:
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    for k, v in VoltDict.items():
        PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_DISABLE + ' ' + v, verbal)
    

def reset(verbal=True):
    """ Reset the voltage regulator, this will cause the board to disconnect

    Args:
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_RESET, verbal)
    

def enable(target, verbal=True):
    """ Enable `target`

    Args:
        target (str): Target voltage source, could be `3V3`, `AVDD_WR`, `AVDD_WL`, `AVDD_RRAM`, `VDD`, `AVDD_SRAM`
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_ENABLE + ' ' + VoltDict[target], verbal)
    

def disable(target, verbal=True):
    """ Disable `target`

    Args:
        target (str): Target voltage source, could be `3V3`, `AVDD_WR`, `AVDD_WL`, `AVDD_RRAM`, `VDD`, `AVDD_SRAM`
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_DISABLE + ' ' + VoltDict[target], verbal)
    

def increment(target, verbal=True):
    """ Increase `target` by 1 in it's binary format. (The real voltage change will depend on the feedback ratio)

    Args:
        target (str): Target voltage source, could be `3V3`, `AVDD_WR`, `AVDD_WL`, `AVDD_RRAM`, `VDD`, `AVDD_SRAM`
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_INCR + ' ' + VoltDict[target], verbal)
    

def decrement(target, verbal=True):
    """ Decrease `target` in it's binary format. (The real voltage change will depend on the feedback ratio)

    Args:
        target (str): Target voltage source, could be `3V3`, `AVDD_WR`, `AVDD_WL`, `AVDD_RRAM`, `VDD`, `AVDD_SRAM`
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_DECR + ' ' + VoltDict[target], verbal)
    

def plus(value, target, verbal=True):
    """ Increase `target` by `value` mV

    Args:
        value (str): Voltage (mV)
        target (str): Target voltage source, could be `3V3`, `AVDD_WR`, `AVDD_WL`, `AVDD_RRAM`, `VDD`, `AVDD_SRAM`
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_PLUS + ' ' + value + ' ' + VoltDict[target], verbal)
    

def minus(value, target, verbal=True):
    """ Decrease `target` by `value` mV

    Args:
        value (str): Voltage (mV)
        target (str): Target voltage source, could be `3V3`, `AVDD_WR`, `AVDD_WL`, `AVDD_RRAM`, `VDD`, `AVDD_SRAM`
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_MINUS + ' ' + value + ' ' + VoltDict[target], verbal)
    

def set_source(value, target, verbal=True):
    """ Set `target` to `value` mV

    Args:
        value (str): Voltage (mV)
        target (str): Target voltage source, could be `3V3`, `AVDD_WR`, `AVDD_WL`, `AVDD_RRAM`, `VDD`, `AVDD_SRAM`
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_SET + ' ' + value + ' ' + VoltDict[target], verbal)


def set_source_safe(value, target, verbal=True):
    """ Set `target` to `value` mV **safely** by disabling it first, and enabling last to avoid overshoot

    Args:
        value (str): Voltage (mV)
        target (str): Target voltage source, could be `3V3`, `AVDD_WR`, `AVDD_WL`, `AVDD_RRAM`, `VDD`, `AVDD_SRAM`
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_SET_SAFE + ' ' + value + ' ' + VoltDict[target], verbal)


def get_source(target, verbal=True):
    """ Get the current voltage value of `target`

    Args:
        target (str): Target voltage source, could be `3V3`, `AVDD_WR`, `AVDD_WL`, `AVDD_RRAM`, `VDD`, `AVDD_SRAM`
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    Returns:
        (str, str): The current status and voltage value of *target*

    """
    return PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_GET + ' ' + VoltDict[target], verbal).split()


def decode(parameters):
    """ Decode the command

    Args:
        parameters (list): Command in List form.

    """
    if   parameters[1] == 'list'       : list_sources   (                            )
    elif parameters[1] == 'clear'      : clear          (                            )
    elif parameters[1] == 'status'     : status         (                            )
    elif parameters[1] == 'save'       : save           (                            )
    elif parameters[1] == 'load'       : load           (                            )
    elif parameters[1] == 'reset'      : reset          (                            )
    elif parameters[1] == 'enable_all' : enable_all     (                            )
    elif parameters[1] == 'disable_all': disable_all    (                            )
    elif parameters[1] == 'enable'     : enable         (parameters[2],              )
    elif parameters[1] == 'disable'    : disable        (parameters[2],              )
    elif parameters[1] == '++'         : increment      (parameters[2],              )
    elif parameters[1] == '--'         : decrement      (parameters[2],              )
    elif parameters[1] == '+'          : plus           (parameters[2], parameters[3])
    elif parameters[1] == '-'          : minus          (parameters[2], parameters[3])
    elif parameters[1] == 'set'        : set_source     (parameters[2], parameters[3])
    elif parameters[1] == 'set_safe'   : set_source_safe(parameters[2], parameters[3])
    elif parameters[1] == 'get'        : get_source     (parameters[2],              )
    else: PT.unknown(parameters)
