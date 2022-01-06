import CommandMap as CM
import PyTerminal as PT
import random
import time

import RRAM

def check_chip_VRef():
    """ Check ADC settings (i.e. Offset/Step) for the whole chip and mark the ones that are faulty

    """
    for module in range(0, 288):
        print(f'\rChecking Module {module} ... ', end='')

        # Set to the new module and clear it
        RRAM.switch(str(module), False)

        # Find the (offset, step)
        response = RRAM.calibrate_VRef('120', '700', '5', False)
        offset = int(response.split()[0])
        step = int(response.split()[1])

        if offset == 0 or offset == 63 or step == 0 or step == 63:
            RRAM.mod_conf(str(CM.CM_RRAM_API_MOD_STATUS_ADC_FATAL), False)
    print('')

    RRAM.mod_status(True)

def sweep_chip_VRef():
    """ Sweep VRef for the whole chip

    """
    print('╔════════╦════════╦══════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╗')
    print('║ Module ║ Offset ║ Step ║  VRef[0] ║  VRef[1] ║  VRef[2] ║  VRef[3] ║  VRef[4] ║  VRef[5] ║  VRef[6] ║  VRef[7] ║  VRef[8] ║  VRef[9] ║ VRef[10] ║ VRef[11] ║ VRef[12] ║ VRef[13] ║ VRef[14] ║')
    print('╟────────╫────────╫──────╫──────────╫──────────╫──────────╫──────────╫──────────╫──────────╫──────────╫──────────╫──────────╫──────────╫──────────╫──────────╫──────────╫──────────╫──────────╢')
    for module in range(0, 288):
        # Set to the new module and clear it
        RRAM.switch(str(module), False)

        # Find the (offset, step)
        response = RRAM.calibrate_VRef('120', '700', '5', False)
        offset = int(response.split()[0])
        step = int(response.split()[1])

        # Config the ADC and Sweep the VRef
        RRAM.conf_ADC(str(offset), str(step), '0x7FFF', False)
        RRAM.sweep_VRef('0', '800', '2', False)

        # Find the VRef
        response = RRAM.list_VRef(False)
        vrefs = response.split('\n')[3].split('║')[2:17]

        # Print out the result
        print(f'║ {module:>6} ║ {offset:>6} ║ {step:>4} ║', end='')
        for i in range(0, 15):
            print(f' {vrefs[i]:>8} ║', end='')
        print('')
    print('╚════════╩════════╩══════╩══════════╩══════════╩══════════╩══════════╩══════════╩══════════╩══════════╩══════════╩══════════╩══════════╩══════════╩══════════╩══════════╩══════════╩══════════╝')


def write_byte(row, num):
    """ Test function for writing a byte at (row, col)

    Args:
        row (str): from 0~255
        col (str): from 0~255
    """
    row = int(row)
    num = int(num)
    print('╔═════════════╦════════╦═════════╦════════════╗')
    print('║ ( row, col) ║ Golden ║ Readout ║ Difference ║')
    print('╟─────────────╫────────╫─────────╫────────────╢')
    for col in range(0, num):
        addr = row * 256 + col
        golden = random.randint(-128, 127)
        RRAM.write_byte_iter(str(addr), str(golden), False)
        readout = int(RRAM.read_byte(str(addr), '0', '0x1', False))
        print(f'║ ( {row:>3}, {col:>3}) ║ {golden:>6} ║ {readout:>7} ║ {golden-readout:>10} ║')
    print('╚═════════════╩════════╩═════════╩════════════╝')


def cim_bit(row, col):
    """ Test function for computer in memory (CIM) at bit level

    Args:
        row (str): from 0~255
        col (str): from 0~255
    """
    row = int(row)
    col = int(col)

    # Reset first 9 cells
    for row_offset in range(0, 9):
        addr = (row+row_offset) * 256 + col
        RRAM.reset('cell', str(addr), True)

    # Set second 9 cells
    for row_offset in range(9, 18):
        addr = (row+row_offset) * 256 + col
        RRAM.set('cell', str(addr), True)

    # Compute-In-Memory
    raws = [[''] * 10 for i in range(10)]
    for value in range(0, 10):
        for ones in range(max(1, value), 10):
            row_offset = 9 - ones + value
            addr = (row + row_offset) * 256 + col
            raws[value][ones] = RRAM.read_lane(str(addr), str(hex(2**ones - 1)), False)

    # Print it out nicely
    print('╔════════════╦════════╦════════╦════════╦════════╦════════╦════════╦════════╦════════╦════════╗')
    print('║ Value\Ones ║      1 ║      2 ║      3 ║      4 ║      5 ║      6 ║      7 ║      8 ║      9 ║')
    print('╟────────────╫────────╫────────╫────────╫────────╫────────╫────────╫────────╫────────╫────────╢')
    for value in reversed(range(0, 10)):
        print(f'║ {value:>10} ║', end='')
        for ones in range(1, 10):
            print(f' {raws[value][ones]:>6} ║', end='')
        print('')
    print('╚════════════╩════════╩════════╩════════╩════════╩════════╩════════╩════════╩════════╩════════╝')

    return raws


def cim_byte(row, col, num):
    """ Test function for computer in memory (CIM) at byte level

    Args:
        row (str): from 0~255
        col (str): from 0~255
        num (str): from 1~9
    """
    row = int(row)
    col = int(col)
    num = int(num)
    values = [0] * num
    goldens = [0] * (2**num)
    readouts = [0] * (2**num)

    # Write the values
    for n in range(num):
        addr = (row+n) * 256 + col
        values[n] = random.randint(-128, 127)
        print(f'Writing {values[n]:>4} to ( {row+n:>3}, {col:>3})')
        RRAM.write_byte_iter(str(addr), str(values[n]), False)

    # Compute the goldens
    for n in range(1, 2**num):
        for i in range(num):
            if n & 2**i:
                goldens[n] += values[i]

    # CIM
    for n in range(1, 2**num):
        readouts[n] = int(RRAM.read_byte(str(row*256 + col), '0', hex(n), False))

    # Print the result nicely
    print('╔══════╦═════════╦════════╦════════════╗')
    print('║ Data ║ Readout ║ Golden ║ Difference ║')
    print('╟──────╫─────────╫────────╫────────────╢')
    for n in range(1, 2**num):
        print(f'║ {hex(n):>4} ║ {readouts[n]:>7} ║ {goldens[n]:>6} ║ {goldens[n]-readouts[n]:>10} ║')
    print('╚══════╩═════════╩════════╩════════════╝')


def decode(parameters):
    """ Decode the command

    Args:
        parameters (list): Command in List form.
    """
    if   parameters[1] == 'check_chip_VRef': check_chip_VRef(                                           )
    elif parameters[1] == 'sweep_chip_VRef': sweep_chip_VRef(                                           )
    elif parameters[1] == 'write_byte'     : write_byte     (parameters[2], parameters[3]               )
    elif parameters[1] == 'cim_bit'        : cim_bit        (parameters[2], parameters[3]               )
    elif parameters[1] == 'cim_byte'       : cim_byte       (parameters[2], parameters[3], parameters[4])
    else: PT.unknown(parameters)
