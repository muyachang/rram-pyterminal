import CommandMap as CM
import PyTerminal as PT

VoltDict = {'3V3'      : b'\x41'.decode('utf-8'), 
            'AVDD_WR'  : b'\x42'.decode('utf-8'),
            'AVDD_WL'  : b'\x43'.decode('utf-8'),
            'AVDD_RRAM': b'\x44'.decode('utf-8'),
            'VDD'      : b'\x45'.decode('utf-8'),
            'AVDD_SRAM': b'\x46'.decode('utf-8')}
            

def list_sources():
    """ List the available voltage sources

    Keyword arguments:
    """
    print('-------------------------------------')
    print('| Output Name | Status | Value (mV) |')
    print('-------------------------------------')
    for key, value in VoltDict.items():
        response = PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_GET + ' ' + value, False)
        output_status = 'On' if response.split()[0] == '1' else 'Off'
        output_value = 'Analog' if response.split()[1] == '-1' else response.split()[1]
        print(f'| {key:>11} | {output_status:>6} | {output_value:>10} |')
    print('-------------------------------------')


def clear(verbal):
    """ Clear the interrupt register in the voltage regulator

    Keyword arguments:
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_CLEAR, verbal)


def status(verbal):
    """ Get the current status of the voltage regulator

    Keyword arguments:
    verbal -- whether to print the response or not
    """
    return PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_STATUS, verbal)


def save(verbal):
    """ Save the current configuration of the voltage regulator to the EEPROM

    Keyword arguments:
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_SAVE, verbal)
    

def load(verbal):
    """ Load the configuration of the voltage regulator from the EEPROM

    Keyword arguments:
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_LOAD, verbal)
    

def allon(verbal):
    """ Enable all the voltage sources

    Keyword arguments:
    verbal -- whether to print the response or not
    """
    for k, v in VoltDict.items():
        PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_ENABLE + ' ' + v, verbal)
        

def alloff(verbal):
    """ Disable all the voltage sources

    Keyword arguments:
    verbal -- whether to print the response or not
    """
    for k, v in VoltDict.items():
        PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_DISABLE + ' ' + v, verbal)
    

def reset(verbal):
    """ Reset the voltage regulator, this will cause the board to disconnect

    Keyword arguments:
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_RESET, verbal)
    

def enable(target, verbal):
    """ Enable 'target' voltage source

    Keyword arguments:
    target -- target voltage source, could be '3V3', 'AVDD_WR', 'AVDD_WL', 'AVDD_RRAM', 'VDD', 'AVDD_SRAM'
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_ENABLE + ' ' + VoltDict[target], verbal)
    

def disable(target, verbal):
    """ Disable 'target' voltage source

    Keyword arguments:
    target -- target voltage source, could be '3V3', 'AVDD_WR', 'AVDD_WL', 'AVDD_RRAM', 'VDD', 'AVDD_SRAM'
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_DISABLE + ' ' + VoltDict[target], verbal)
    

def increment(target, verbal):
    """ Increase 'target' voltage source by 1 of its value register.
        The real voltage change will depend on the feedback ratio

    Keyword arguments:
    target -- target voltage source, could be '3V3', 'AVDD_WR', 'AVDD_WL', 'AVDD_RRAM', 'VDD', 'AVDD_SRAM'
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_INCR + ' ' + VoltDict[target], verbal)
    

def decrement(target, verbal):
    """ Decrease 'target' voltage source by 1 of its value register.
        The real voltage change will depend on the feedback ratio

    Keyword arguments:
    target -- target voltage source, could be '3V3', 'AVDD_WR', 'AVDD_WL', 'AVDD_RRAM', 'VDD', 'AVDD_SRAM'
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_DECR + ' ' + VoltDict[target], verbal)
    

def plus(value, target, verbal):
    """ Increase 'target' voltage source by 'value' mV

    Keyword arguments:
    value -- voltage (mV)
    target -- target voltage source, could be '3V3', 'AVDD_WR', 'AVDD_WL', 'AVDD_RRAM', 'VDD', 'AVDD_SRAM'
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_PLUS + ' ' + value + ' ' + VoltDict[target], verbal)
    

def minus(value, target, verbal):
    """ Decrease 'target' voltage source by 'value' mV

    Keyword arguments:
    value -- voltage (mV)
    target -- target voltage source, could be '3V3', 'AVDD_WR', 'AVDD_WL', 'AVDD_RRAM', 'VDD', 'AVDD_SRAM'
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_MINUS + ' ' + value + ' ' + VoltDict[target], verbal)
    

def set_source(value, target, verbal):
    """ Set 'target' voltage source to 'value' mV

    Keyword arguments:
    value -- voltage (mV)
    target -- target voltage source, could be '3V3', 'AVDD_WR', 'AVDD_WL', 'AVDD_RRAM', 'VDD', 'AVDD_SRAM'
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_SET + ' ' + value + ' ' + VoltDict[target], verbal)


def set_safe_source(value, target, verbal):
    """ Set 'target' voltage source to 'value' mV 'safely' by disabling it first, and enabling last to avoid overshoot

    Keyword arguments:
    value -- voltage (mV)
    target -- target voltage source, could be '3V3', 'AVDD_WR', 'AVDD_WL', 'AVDD_RRAM', 'VDD', 'AVDD_SRAM'
    verbal -- whether to print the response or not
    """
    PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_SET_SAFE + ' ' + value + ' ' + VoltDict[target], verbal)


def get_source(target, verbal):
    """ Get the current voltage of 'target' source

    Keyword arguments:
    target -- target voltage source, could be '3V3', 'AVDD_WR', 'AVDD_WL', 'AVDD_RRAM', 'VDD', 'AVDD_SRAM'
    verbal -- whether to print the response or not
    """
    return PT.send_command(CM.CM_PM + ' ' + CM.CM_PM_GET + ' ' + VoltDict[target], verbal).split()


def decode(parameters):
    """ Decode the command

    Args:
        parameters (list): Command in List form.
    """
    if   parameters[1] == 'list'    : list_sources   (                                  )
    elif parameters[1] == 'clear'   : clear          (                              True)
    elif parameters[1] == 'status'  : status         (                              True)
    elif parameters[1] == 'save'    : save           (                              True)
    elif parameters[1] == 'load'    : load           (                              True)
    elif parameters[1] == 'allon'   : allon          (                              True)
    elif parameters[1] == 'alloff'  : alloff         (                              True)
    elif parameters[1] == 'reset'   : reset          (                              True)
    elif parameters[1] == 'enable'  : enable         (parameters[2],                True)
    elif parameters[1] == 'disable' : disable        (parameters[2],                True)
    elif parameters[1] == '++'      : increment      (parameters[2],                True)
    elif parameters[1] == '--'      : decrement      (parameters[2],                True)
    elif parameters[1] == '+'       : plus           (parameters[2], parameters[3], True)
    elif parameters[1] == '-'       : minus          (parameters[2], parameters[3], True)
    elif parameters[1] == 'set'     : set_source     (parameters[2], parameters[3], True)
    elif parameters[1] == 'set_safe': set_safe_source(parameters[2], parameters[3], True)
    elif parameters[1] == 'get'     : get_source     (parameters[2],                True)
    else: PT.unknown(parameters)
    