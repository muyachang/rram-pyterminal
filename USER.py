import time
import math
from Lib import RRAM
from Board import PM, DAC


def clear(pyterminal):
    # Clear up some registers
    RRAM.read(pyterminal, 'set', 'enable', '1', True)
    RRAM.read(pyterminal, 'set', 'counter', '7', True)
    RRAM.read(pyterminal, 'toggle', '', '', True)
    RRAM.read(pyterminal, 'set', 'counter', '0', True)
    RRAM.read(pyterminal, 'toggle', '', '', True)
    RRAM.read(pyterminal, 'set', 'enable', '0', True)

    # Configurations
    RRAM.conf_form(pyterminal, '3200', '1700', '1600', True)
    RRAM.conf_set(pyterminal, '1700', '1700', '2', True)
    RRAM.conf_reset(pyterminal, '2500', '2500', '160', True)
    RRAM.conf_read(pyterminal, '1100', '3', True)


def sweep_on_state_cells(pyterminal, col):
    # Set first 9 cells
    for i in range(0, 9):
        RRAM.set(pyterminal, str(i * 256 + int(col)), True)

    # Rest second 9 cells
    for i in range(9, 18):
        RRAM.reset(pyterminal, str(i * 256 + int(col)), True)

    # Read 10 cells (0 On-State ~ 9 On-State)
    for i in range(0, 10):
        RRAM.read_raw(pyterminal, str(i * 256 + int(col)), '0', '0x1FF', True)
    print('')
    for i in range(1, 10):
        RRAM.read_raw(pyterminal, str(i * 256 + int(col)), '0', '0x0FF', True)
    print('')
    for i in range(2, 10):
        RRAM.read_raw(pyterminal, str(i * 256 + int(col)), '0', '0x07F', True)
    print('')
    for i in range(3, 10):
        RRAM.read_raw(pyterminal, str(i * 256 + int(col)), '0', '0x03F', True)
    print('')
    for i in range(4, 10):
        RRAM.read_raw(pyterminal, str(i * 256 + int(col)), '0', '0x01F', True)
    print('')
    for i in range(5, 10):
        RRAM.read_raw(pyterminal, str(i * 256 + int(col)), '0', '0x00F', True)
    print('')
    for i in range(6, 10):
        RRAM.read_raw(pyterminal, str(i * 256 + int(col)), '0', '0x007', True)
    print('')
    for i in range(7, 10):
        RRAM.read_raw(pyterminal, str(i * 256 + int(col)), '0', '0x003', True)
    print('')
    for i in range(8, 10):
        RRAM.read_raw(pyterminal, str(i * 256 + int(col)), '0', '0x001', True)
    print('')


def sweep_reference_voltages(pyterminal):
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('| Module | Offset | Step |  VRef[0] |  VRef[1] |  VRef[2] |  VRef[3] |  VRef[4] |  VRef[5] |  VRef[6] |  VRef[7] |  VRef[8] |  VRef[9] | VRef[10] | VRef[11] | VRef[12] | VRef[13] | VRef[14] |')
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    for module in range(0, 288):
        # Set to the new module and clear it
        RRAM.module(pyterminal, 'set', str(module), True)
        clear(pyterminal)
        # Find the (offset, step)
        response = RRAM.calibrate_voltage_references(pyterminal, str(module), '50', '700', '5', False)
        offset = int(response.split()[0])
        step = int(response.split()[1])

        # Find the VRef
        RRAM.conf_ADC(pyterminal, str(offset), str(step), '0x7FFF', True)
        response = RRAM.list_voltage_references(pyterminal, str(module), '0', '1000', '2', False)
        vrefs = response.split()

        # Print out the result
        print(f'| {module:>6} | {offset:>6} | {step:>4} |', end='')
        for i in range(0, 15):
            print(f' {vrefs[i]:>8} |', end='')
        print('')




def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    if   parameters[1] == 'clear'            : clear                   (pyterminal)
    elif parameters[1] == 'cim'              : sweep_on_state_cells    (pyterminal, parameters[2])
    elif parameters[1] == 'sweep_VRef'       : sweep_reference_voltages(pyterminal)
    else: unknown(parameters)
