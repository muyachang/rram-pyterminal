import PyTerminal as PT
import random
import time
import math

import RRAM, DNN

from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import numpy as np

import io

class pad:
    def __init__(self, master):
        self.WL = 8
        self.master = master
        self.old_x = None
        self.old_y = None
        self.drawWidgets()
        self.c.bind('<B1-Motion>', self.paint) #drwaing the line
        self.c.bind('<ButtonRelease-1>', self.reset)

    def paint(self, e):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, e.x, e.y, width=40, fill='black', capstyle=ROUND, smooth=False)
        self.old_x = e.x
        self.old_y = e.y

    def reset(self, e):    #reseting or cleaning the canvas
        self.old_x = None
        self.old_y = None

    def clear(self):
        self.c.delete(ALL)

    def load_image(self):
        image_path = filedialog.askopenfilename()
        if image_path == '':
            return
        image = []
        f = open(image_path, 'r')
        for line in f:
            image.extend(line.split())
        f.close()
        img = Image.fromarray(2*(255-np.uint8(image).reshape(16,16))).resize((400, 400))
        self.img = ImageTk.PhotoImage(image=img)
        self.c.create_image(0, 0, anchor="nw", image=self.img)
        self.inference(image)

    def capture_image(self):
        ps = self.c.postscript(colormode='mono')
        image = Image.open(io.BytesIO(ps.encode('utf-8')))
        image = image.convert('L').resize((16, 16))
        image = np.array(image.getdata())
        for i in range(256):
            image[i] = (255 - image[i])/2.5
        self.inference(image)

    def inference(self, image):
        # Write the image
        DNN.clean_input(True)
        for i in range(256):
            if image[i] != 0:
                DNN.fill_input(str(i), str(image[i]), True)

        # Print the result
        pred = DNN.forward(str(self.WL), False)
        self.prediction.set(pred)

    def drawWidgets(self):
        self.controls = Frame(self.master, padx=5, pady=5)
        self.button = ttk.Button(self.controls, text="Clear", command=self.clear).grid(row=0, column=0)
        self.button = ttk.Button(self.controls, text="Load Image", command=self.load_image).grid(row=1, column=0)
        self.button = ttk.Button(self.controls, text="Inference", command=self.capture_image).grid(row=2, column=0)
        Label(self.controls, text='Prediction', font=('18')).grid(row=3, column=0)
        self.prediction = StringVar()
        self.prediction.set('')
        Label(self.controls, textvariable=self.prediction, font=('Arial', 48)).grid(row=4, column=0)
        self.controls.pack(side=LEFT)
        self.c = Canvas(self.master, width=400, height=400, bg='white')
        self.c.pack(fill=BOTH, expand=True)


def sweep_chip_VRef():
    """ Sweep reference voltages for the whole chip

    Keyword arguments:
    """
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('| Module | Offset | Step |  VRef[0] |  VRef[1] |  VRef[2] |  VRef[3] |  VRef[4] |  VRef[5] |  VRef[6] |  VRef[7] |  VRef[8] |  VRef[9] | VRef[10] | VRef[11] | VRef[12] | VRef[13] | VRef[14] |')
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    for module in range(0, 288):
        # Set to the new module and clear it
        RRAM.switch(str(module), True)
        time.sleep(1)

        # Find the (offset, step)
        response = RRAM.calibrate_voltage_references(str(module), '120', '700', '5', False)
        offset = int(response.split()[0])
        step = int(response.split()[1])

        # Config the ADC and Sweep the VRef
        RRAM.conf_ADC(str(offset), str(step), '0x7FFF', False)
        RRAM.sweep_voltage_references(str(module), '0', '900', '2', False)

        # Find the VRef
        response = RRAM.list_voltage_references(str(module), False)
        vrefs = response.split('\n')[3].split('|')[2:17]

        # Print out the result
        print(f'| {module:>6} | {offset:>6} | {step:>4} |', end='')
        for i in range(0, 15):
            print(f' {vrefs[i]:>8} |', end='')
        print('')
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')


def test_write_byte(row, num):
    """ Test function for writing a byte at (row, col)

    Keyword arguments:
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
        RRAM.write_byte_iter(str(addr), str(golden), False)
        readout = int(RRAM.read_byte(str(addr), '0', '0x1', False))
        print(f'| ( {row:>3}, {col:>3}) | {golden:>6} | {readout:>7} | {golden-readout:>10} |')
    print('-----------------------------------------------')


def test_bit_cim(row, col):
    """ Test function for computer in memory (CIM) at bit level

    Keyword arguments:
    row -- from '0'~'255'
    col -- from '0'~'255'
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


def test_byte_cim(row, col, num):
    """ Test function for computer in memory (CIM) at byte level

    Keyword arguments:
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
    print('----------------------------------------')
    print('| Data | Readout | Golden | Difference |')
    print('----------------------------------------')
    for n in range(1, 2**num):
        print(f'| {hex(n):>4} | {readouts[n]:>7} | {goldens[n]:>6} | {goldens[n]-readouts[n]:>10} |')
    print('----------------------------------------')


def mnist_config(network):
    if network == 'MLP':
        # Build the network
        DNN.nn_clear(False)

        DNN.nn_conf_type('0', '0', False)
        DNN.nn_conf_rrams('0', '9', False)
        DNN.nn_conf_input('0', '256', '1', False)
        DNN.nn_conf_kernel('0', '256', '32', '0', False)
        DNN.nn_conf_act('0', '1', False)
        DNN.nn_conf_quant('0', '975', '0', False)

        DNN.nn_conf_type('1', '0', False)
        DNN.nn_conf_rrams('1', '12', False)
        DNN.nn_conf_input('1', '32', '1', False)
        DNN.nn_conf_kernel('1', '32', '10', '0', False)
        DNN.nn_conf_act('1', '0', False)

    DNN.nn_print(True)


def mnist_write_weights(network):
    if network == 'MLP':
        # Some configuration
        folder_dir = 'D:\Dropbox (GaTech)\GaTech\ICSRL\Projects\9. RRAM\Evaluation Board\MNIST\data_256_fc32_fc10'

        # Read the layer 1 weights
        RRAM.switch('9', False)
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
                RRAM.write_byte_iter(str(addr), str(golden), True)
                readout = int(RRAM.read_byte(str(addr), '0', '0x1', False))
                if readout != golden:
                    print(f'| ( {row:>3}, {col:>3}) | {golden:>6} | {readout:>7} | {golden-readout:>10} |')
                count += 1
        print('-----------------------------------------------')

        #  Read the layer 2 weights
        RRAM.switch('12', False)
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
                RRAM.write_byte_iter(str(addr), str(golden), True)
                readout = int(RRAM.read_byte(str(addr), '0', '0x1', False))
                if readout != golden:
                    print(f'| ( {row:>3}, {col:>3}) | {golden:>6} | {readout:>7} | {golden-readout:>10} |')
                count += 1
        print('-----------------------------------------------')


def mnist_inference(network, WL):
    mnist_config(network)

    # Some configuration
    if network == 'MLP':
        folder_dir = 'D:\Dropbox (GaTech)\GaTech\ICSRL\Projects\9. RRAM\Evaluation Board\MNIST\data_256_fc32_fc10'

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

    # Read the image and do th inference
    print( '---------------------------')
    print(f'| Index | Gold | Sim | TC |')
    print( '---------------------------')
    tc_preds = []
    for index in range(50):
        # Upload image
        mnist_upload(network, index, False)

        # Inference
        tc_preds.append(DNN.forward(WL, False))

        # Print the result
        print(f'| {index:>5} | {labels[index]:>4} | {sim_preds[index]:>3} | {tc_preds[index]:>2} |')
    print( '---------------------------')


def mnist_demo(pyterminal):
    root = Tk()
    pad(root, pyterminal)
    root.title('MNIST Demo')
    root.mainloop()


def mnist_upload(network, index, print_image):
    # Read the image
    if network == 'MLP':
        folder_dir = 'D:\Dropbox (GaTech)\GaTech\ICSRL\Projects\9. RRAM\Evaluation Board\MNIST\data_256_fc32_fc10'
    image_path = folder_dir + '\image' + str(index) + '.txt'
    image = []
    f = open(image_path, 'r')
    for line in f:
        image.extend(line.split())
    f.close()
    image_len = int(math.sqrt(len(image)))

    # Upload the image
    DNN.in_conf_len(str(image_len), True)
    for i in range(256):
        if image[i] != '0':
            DNN.in_fill(str(i), image[i], True)

    # Print the image if required
    if print_image:
        DNN.in_print(True)


def decode(parameters):
    """ Decode the split version of the command

    Keyword arguments:
    pyterminal -- current connected COM port
    parameters -- split version of the command
    """
    if   parameters[1] == 'sweep_chip_VRef'    : sweep_chip_VRef    (                                           )
    elif parameters[1] == 'test_write_byte'    : test_write_byte    (parameters[2], parameters[3]               )
    elif parameters[1] == 'test_bit_cim'       : test_bit_cim       (parameters[2], parameters[3]               )
    elif parameters[1] == 'test_byte_cim'      : test_byte_cim      (parameters[2], parameters[3], parameters[4])
    elif parameters[1] == 'mnist_config'       : mnist_config       (parameters[2]                              )
    elif parameters[1] == 'mnist_write_weights': mnist_write_weights(parameters[2]                              )
    elif parameters[1] == 'mnist_upload'       : mnist_upload       (parameters[2], parameters[3], True         )
    elif parameters[1] == 'mnist_inference'    : mnist_inference    (parameters[2], parameters[3]               )
    elif parameters[1] == 'mnist_demo'         : mnist_demo         (                                           )
    else: PT.unknown(parameters)
