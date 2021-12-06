import random
import time
from ctypes import c_int8

import DAC, DNN
from Lib import RRAM

def sweep_chip_VRef(pyterminal):
    """ Sweep reference voltages for the whole chip

    Keyword arguments:
    pyterminal -- current connected COM port
    """
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('| Module | Offset | Step |  VRef[0] |  VRef[1] |  VRef[2] |  VRef[3] |  VRef[4] |  VRef[5] |  VRef[6] |  VRef[7] |  VRef[8] |  VRef[9] | VRef[10] | VRef[11] | VRef[12] | VRef[13] | VRef[14] |')
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    for module in range(0, 288):
        # Set to the new module and clear it
        RRAM.switch(pyterminal, str(module), True)
        time.sleep(1)

        # Find the (offset, step)
        response = RRAM.calibrate_voltage_references(pyterminal, str(module), '120', '700', '5', False)
        offset = int(response.split()[0])
        step = int(response.split()[1])

        # Config the ADC and Sweep the VRef
        RRAM.conf_ADC(pyterminal, str(offset), str(step), '0x7FFF', False)
        RRAM.sweep_voltage_references(pyterminal, str(module), '0', '900', '2', False)

        # Find the VRef
        response = RRAM.list_voltage_references(pyterminal, str(module), False)
        vrefs = response.split('\n')[3].split('|')[2:17]

        # Print out the result
        print(f'| {module:>6} | {offset:>6} | {step:>4} |', end='')
        for i in range(0, 15):
            print(f' {vrefs[i]:>8} |', end='')
        print('')
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')


def test_write_byte(pyterminal, row, num):
    """ Test function for writing a byte at (row, col)

    Keyword arguments:
    pyterminal -- current connected COM port
    row -- from '0'~'255'
    col -- from '0'~'255'
    """
    row = int(row)
    num = int(num)
    print('-----------------------------------------------')
    print('| ( row, col) | Golden | Readout | Difference |')
    print('-----------------------------------------------')
    for col in range(0, num):
        addr = row * 256 + col
        golden = random.randint(-128, 127)
        RRAM.write_byte_iter(pyterminal, str(addr), str(golden), False)
        readout = int(RRAM.read_byte(pyterminal, str(addr), '0', '0x1', False))
        print(f'| ( {row:>3}, {col:>3}) | {golden:>6} | {readout:>7} | {golden-readout:>10} |')
    print('-----------------------------------------------')


def test_bit_cim(pyterminal, row, col):
    """ Test function for computer in memory (CIM) at bit level

    Keyword arguments:
    pyterminal -- current connected COM port
    row -- from '0'~'255'
    col -- from '0'~'255'
    """
    row = int(row)
    col = int(col)

    # Reset first 9 cells
    for row_offset in range(0, 9):
        addr = (row+row_offset) * 256 + col
        RRAM.reset(pyterminal, 'cell', str(addr), True)

    # Set second 9 cells
    for row_offset in range(9, 18):
        addr = (row+row_offset) * 256 + col
        RRAM.set(pyterminal, 'cell', str(addr), True)

    # Compute-In-Memory
    raws = [[''] * 10 for i in range(10)]
    for value in range(0, 10):
        for ones in range(max(1, value), 10):
            row_offset = 9 - ones + value
            addr = (row + row_offset) * 256 + col
            raws[value][ones] = RRAM.read_lane(pyterminal, str(addr), str(hex(2**ones - 1)), False)

    # Print it out nicely
    print('-----------------------------------------------------------------------------------------------')
    print('| Value\Ones |      1 |      2 |      3 |      4 |      5 |      6 |      7 |      8 |      9 |')
    print('-----------------------------------------------------------------------------------------------')
    for value in reversed(range(0, 10)):
        print(f'| {value:>10} |', end='')
        for ones in range(1, 10):
            print(f' {raws[value][ones]:>6} |', end='')
        print('')
    print('-----------------------------------------------------------------------------------------------')

    return raws


def test_byte_cim(pyterminal, row, col, num):
    """ Test function for computer in memory (CIM) at byte level

    Keyword arguments:
    pyterminal -- current connected COM port
    row -- from '0'~'255'
    col -- from '0'~'255'
    num -- from '1'~'9'
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
        RRAM.write_byte_iter(pyterminal, str(addr), str(values[n]), False)

    # Compute the goldens
    for n in range(1, 2**num):
        for i in range(num):
            if n & 2**i:
                goldens[n] += values[i]

    # CIM
    for n in range(1, 2**num):
        readouts[n] = int(RRAM.read_byte(pyterminal, str(row*256 + col), '0', hex(n), False))

    # Print the result nicely
    print('----------------------------------------')
    print('| Data | Readout | Golden | Difference |')
    print('----------------------------------------')
    for n in range(1, 2**num):
        print(f'| {hex(n):>4} | {readouts[n]:>7} | {goldens[n]:>6} | {goldens[n]-readouts[n]:>10} |')
    print('----------------------------------------')


def mnist_write_weights(pyterminal):
    # For 256_10
    #   Layer 1: 5

    # For 256_32_10
    # Layer 1: 9
    # Layer 2: 12

    # Some configuration
    folder_dir = 'D:\Dropbox (GaTech)\GaTech\ICSRL\Projects\9. RRAM\Evaluation Board\MNIST_MLP\data_256_32_10'

    # Read the layer 1 weights
    RRAM.module(pyterminal, 'set', '9', False)
    RRAM.conf_ADC(pyterminal, '1', '12', '0x7FFF', False)
    weight_path = folder_dir + '\\fc1.txt'
    f = open(weight_path, 'r')
    count = 0
    print('-----------------------------------------------')
    print('| ( row, col) | Golden | Readout | Difference |')
    print('-----------------------------------------------')
    for line in f:
        for w in line.split():
            row = count % 256 # fc1
            col = int(count/256) # fc1
            addr = row * 256 + col
            golden = int(w)
            #print(f'{golden:>4} @ ({row:>3}, {col:>3})')
            RRAM.write_byte_iter(pyterminal, str(addr), str(golden), True)
            readout = int(RRAM.read_byte(pyterminal, str(addr), '0', '0x1', False))
            print(f'| ( {row:>3}, {col:>3}) | {golden:>6} | {readout:>7} | {golden-readout:>10} |')
            count += 1
    print('-----------------------------------------------')

    #  Read the layer 2 weights
    RRAM.module(pyterminal, 'set', '12', False)
    RRAM.conf_ADC(pyterminal, '8', '28', '0x7FFF', False)
    weight_path = folder_dir + '\\fc2.txt'
    f = open(weight_path, 'r')
    count = 0
    print('-----------------------------------------------')
    print('| ( row, col) | Golden | Readout | Difference |')
    print('-----------------------------------------------')
    for line in f:
        for w in line.split():
            row = count % 32 # fc2
            col = int(count/32) # fc2
            addr = row * 256 + col
            golden = int(w)
            #print(f'{golden:>4} @ ({row:>3}, {col:>3})')
            RRAM.write_byte_iter(pyterminal, str(addr), str(golden), True)
            readout = int(RRAM.read_byte(pyterminal, str(addr), '0', '0x1', False))
            print(f'| ( {row:>3}, {col:>3}) | {golden:>6} | {readout:>7} | {golden-readout:>10} |')
            count += 1
    print('-----------------------------------------------')


def mnist_inference(pyterminal):

    # Some configuration
    folder_dir = 'D:\Dropbox (GaTech)\GaTech\ICSRL\Projects\9. RRAM\Evaluation Board\MNIST_MLP\data_256_32_10'
    num_WL = 1

    # Read labels
    label_path = folder_dir + '\labels.txt'
    f = open(label_path, 'r')
    labels = f.readline().split()
    f.close()

    # Read predictions
    pred_path = folder_dir + '\predictions.txt'
    f = open(pred_path, 'r')
    sim_preds = f.readline().split()
    f.close()

    # Read quantizations
    fc1_q = 0
    fc2_q = 0
    q_path = folder_dir + '\\fc1_q.txt'
    f = open(q_path, 'r')
    fc1_q = f.readline().split()
    f.close()
    q_path = folder_dir + '\\fc2_q.txt'
    f = open(q_path, 'r')
    fc2_q = f.readline().split()
    f.close()

    # Read the image and do th inference
    print( '---------------------------')
    print(f'| Index | Gold | Sim | TC |')
    print( '---------------------------')
    tc_preds = []
    for index in range(1000):
        # Read the image
        image_path = folder_dir + '\image' + str(index) + '.txt'
        image = []
        f = open(image_path, 'r')
        for line in f:
            image.extend(line.split())
        f.close()

        # Write the image
        DNN.clean_input(pyterminal, True)
        for i in range(256):
            if image[i] != '0':
                DNN.config_input(pyterminal, str(i), image[i], True)

        # Inference
        tc_preds.append(DNN.forward(pyterminal, '1', False))

        # Print the result
        print(f'| {index:>5} | {labels[index]:>4} | {sim_preds[index]:>3} | {tc_preds[index]:>2} |')
    print( '---------------------------')


def unknown(parameters):
    """ Print out the unknown command

    Keyword arguments:
    parameters -- the split version of the command
    """
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    """ Decode the split version of the command

    Keyword arguments:
    pyterminal -- current connected COM port
    parameters -- split version of the command
    """
    if   parameters[1] == 'sweep_chip_VRef'    : sweep_chip_VRef    (pyterminal)
    elif parameters[1] == 'test_write_byte'    : test_write_byte    (pyterminal, parameters[2], parameters[3])
    elif parameters[1] == 'test_bit_cim'       : test_bit_cim       (pyterminal, parameters[2], parameters[3])
    elif parameters[1] == 'test_byte_cim'      : test_byte_cim      (pyterminal, parameters[2], parameters[3], parameters[4])
    elif parameters[1] == 'mnist_write_weights': mnist_write_weights(pyterminal)
    elif parameters[1] == 'mnist_inference'    : mnist_inference    (pyterminal)
    else: unknown(parameters)
