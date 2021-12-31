import PyTerminal as PT

import random
import time
import numpy as np
import io
import torch

import RRAM, DNN

from tkinter import *
from tkinter import font

from PIL import Image, ImageTk


class MNIST_GUI:
    def __init__(self):
        self.master = Tk()
        self.initUI()
        self.master.resizable(False, False)
        self.master.mainloop()


    def initUI(self):
        self.master.title("MNIST Demo")

        # Change default font
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family="Arial", size=12)

        # Control Panel
        frm_controls = Frame(self.master, padx=5)
        frm_controls.pack(side=LEFT)


        frm_data_index = Frame(frm_controls, borderwidth=5, relief='ridge')
        frm_data_index.pack(pady=5)

        lbl_data_index = Label(frm_data_index, text='Image Index', width=12, font='Arial 14 bold')
        lbl_data_index.pack()

        self.txt_data_index = Entry(frm_data_index, width=5, font='Arial 14')
        self.txt_data_index.pack(side=LEFT, padx=5)

        self.btn_random_icon = ImageTk.PhotoImage(Image.open('Applications/btn_random.png').resize((20, 20)))
        btn_random = Button(frm_data_index, image=self.btn_random_icon, command=self.random_image)
        btn_random.pack(side=RIGHT, padx=5)

        self.btn_load_icon = ImageTk.PhotoImage(Image.open('Applications/btn_load.png').resize((20, 20)))
        btn_load = Button(frm_data_index, image=self.btn_load_icon, command=self.load_image)
        btn_load.pack(side=RIGHT, padx=5)


        frm_network = Frame(frm_controls, borderwidth=5, relief='ridge')
        frm_network.pack(pady=5)

        lbl_network = Label(frm_network, text='Network Type', width=12, font='Arial 14 bold')
        lbl_network.pack()

        networks = ('MLP', 'CONV')
        self.network_var = StringVar(value=networks[0])
        self.change_network()
        op_network = OptionMenu(frm_network, self.network_var, *networks)
        op_network.pack(side=LEFT, padx=5)

        self.btn_config_icon = ImageTk.PhotoImage(Image.open('Applications/btn_load.png').resize((20, 20)))
        btn_config = Button(frm_network, image=self.btn_config_icon, command=self.change_network)
        btn_config.pack(side=RIGHT, padx=5)


        frm_wl_scheme = Frame(frm_controls, borderwidth=5, relief='ridge')
        frm_wl_scheme.pack(pady=5)

        lbl_WL = Label(frm_wl_scheme, text='WL Scheme', width=12, font='Arial 14 bold')
        lbl_WL.pack()

        self.sld_WL = Scale(frm_wl_scheme, from_=1, to=9, orient=HORIZONTAL)
        self.sld_WL.pack()


        frm_operation = Frame(frm_controls, borderwidth=5, relief='ridge')
        frm_operation.pack(pady=5)

        lbl_operation = Label(frm_operation, text='Operation', width=12, font='Arial 14 bold')
        lbl_operation.pack()

        self.btn_clear_icon = ImageTk.PhotoImage(Image.open('Applications/btn_clear.png').resize((20, 20)))
        btn_clear = Button(frm_operation, image=self.btn_clear_icon, command=self.clear)
        btn_clear.pack(side=LEFT, padx=5)

        btn_inference = Button(frm_operation, text="Inference", command=self.inference, font='Arial 12')
        btn_inference.pack(side=RIGHT, padx=5)


        # Result Panel
        frm_results = Frame(self.master, padx=5)
        frm_results.pack(side=RIGHT)


        frm_golden = Frame(frm_results, borderwidth=5, relief='ridge')
        frm_golden.pack(pady=5)

        lbl_golden = Label(frm_golden, text='Golden', width=12, font='Arial 14 bold')
        lbl_golden.pack()

        self.text_golden = StringVar(value='N/A')
        lbl_golden_var = Label(frm_golden, textvariable=self.text_golden, font=('Arial', 48))
        lbl_golden_var.pack()


        frm_duration = Frame(frm_results, borderwidth=5, relief='ridge')
        frm_duration.pack(pady=5)

        lbl_duration = Label(frm_duration, text='Duration (s)', width=12, font='Arial 14 bold')
        lbl_duration.pack()

        self.text_duration = StringVar(value='N/A')
        lbl_duration_var = Label(frm_duration, textvariable=self.text_duration, font=('Arial', 32))
        lbl_duration_var.pack()


        frm_prediction = Frame(frm_results, borderwidth=5, relief='ridge')
        frm_prediction.pack(pady=5)

        lbl_prediction = Label(frm_prediction, text='Prediction', width=12, font='Arial 14 bold')
        lbl_prediction.pack()

        self.text_prediction = StringVar(value='N/A')
        lbl_prediction_var = Label(frm_prediction, textvariable=self.text_prediction, font=('Arial', 48))
        lbl_prediction_var.pack()


        # Canvas Panel
        self.old_x = None
        self.old_y = None
        self.c = Canvas(self.master, width=400, height=400, bg='white', borderwidth=10, relief='ridge')
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
        self.c.pack()


    def paint(self, e):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, e.x, e.y, width=40, stipple='gray50', capstyle=ROUND)
        self.old_x = e.x
        self.old_y = e.y


    def reset(self, e):
        self.old_x = None
        self.old_y = None


    def clear(self):
        self.c.delete(ALL)
        self.text_golden.set('N/A')
        self.text_prediction.set('N/A')
        self.text_duration.set('N/A')
        self.txt_data_index.delete(0, 'end')


    def change_network(self):
        network = self.network_var.get()
        config_network(network, False)

    def load_image(self):
        index = int(self.txt_data_index.get())

        # Paint the image onto the canvas
        tkimage = np.invert(4*images[index])
        tkimage = Image.fromarray(tkimage)
        tkimage = tkimage.resize((self.c.winfo_width(), self.c.winfo_height()))
        self.tkimage = ImageTk.PhotoImage(image=tkimage)
        self.c.create_image(0, 0, anchor="nw", image=self.tkimage)

        # Load golden and clear prediction/duration
        self.text_golden.set(targets[index])
        self.text_prediction.set('N/A')
        self.text_duration.set('N/A')

    def random_image(self):
        self.txt_data_index.delete(0, 'end')
        self.txt_data_index.insert(0, str(random.randint(0, 10000)))
        self.load_image()

    def capture_image(self):
        # Capture the image from Canvas
        ps = self.c.postscript(colormode='gray')
        image = Image.open(io.BytesIO(ps.encode('utf-8')))
        image = image.convert(mode='L').resize((image_len, image_len))
        image = np.uint8(image.getdata())
        image = np.floor_divide(np.invert(image), 4)
        image = np.reshape(image, (image_len, image_len))
        return image


    def inference(self):
        # Clear the prediction and duration first
        self.text_prediction.set('N/A')
        self.text_duration.set('N/A')
        self.master.update()

        # Upload the image
        if self.txt_data_index.get() != '':
            upload_image(str(self.txt_data_index.get()), False)
        else:
            image = self.capture_image()
            DNN.in_conf_len(str(image_len), True)
            for i in range(image_len):
                for j in range(image_len):
                    if image[i][j] != 0:
                        DNN.in_fill(str(i*16+j), str(image[i][j]), True)

        # Print the result
        tick = time.time()
        pred = DNN.forward(str(self.sld_WL.get()), False)
        passed_time = time.time()-tick
        self.text_duration.set(f'{passed_time:.2f}')
        self.text_prediction.set(pred)


def config_network(network, verbal):
    # Some global variabls
    global folder_dir
    global qmodel
    global images
    global image_len
    global targets
    global sim_preds

    if network == 'MLP':
        folder_dir = 'D:\Dropbox (GaTech)\GaTech\ICSRL\Projects\9. RRAM\Evaluation Board\MNIST\data_256_fc32_fc10'

        # Build the network
        DNN.nn_clear(False)

        DNN.nn_conf_rrams   ('0', '9'                  , False)
        DNN.nn_conf_type    ('0', '0'                  , False)
        DNN.nn_conf_input   ('0', '256', '1'           , False)
        DNN.nn_conf_kernel  ('0', '256', '1', '32', '0', False)
        DNN.nn_conf_output  ('0', '32', '1', '1'       , False)
        DNN.nn_conf_output_q('0', '555', '0'          , False)

        DNN.nn_conf_rrams   ('1', '12'                , False)
        DNN.nn_conf_type    ('1', '0'                 , False)
        DNN.nn_conf_input   ('1', '32', '1'           , False)
        DNN.nn_conf_kernel  ('1', '32', '1', '10', '0', False)
        DNN.nn_conf_output  ('1', '10', '1', '0'      , False)

        DNN.nn_conf_type    ('2', '3'                 , False)
        DNN.nn_conf_input   ('2', '10', '1'           , False)


    elif network == 'CONV':
        folder_dir = 'D:\Dropbox (GaTech)\GaTech\ICSRL\Projects\9. RRAM\Evaluation Board\MNIST\data_256_conv16_conv32_fc10'

        # Build the network
        DNN.nn_clear(False)

        DNN.nn_conf_rrams   ('0', '16'               , False)
        DNN.nn_conf_type    ('0', '1'                , False)
        DNN.nn_conf_input   ('0', '16', '1'          , False)
        DNN.nn_conf_kernel  ('0', '3', '1', '16', '1', False)
        DNN.nn_conf_output  ('0', '14', '16', '1'    , False)
        DNN.nn_conf_output_q('0', '145', '0'         , False)

        DNN.nn_conf_type    ('1', '2'                 , False)
        DNN.nn_conf_input   ('1', '14', '16'          , False)
        DNN.nn_conf_kernel  ('1', '2', '1', '16', '2' , False)
        DNN.nn_conf_output  ('1', '7', '16', '0'      , False)

        DNN.nn_conf_rrams   ('2', '21'                , False)
        DNN.nn_conf_type    ('2', '1'                 , False)
        DNN.nn_conf_input   ('2', '7', '16'           , False)
        DNN.nn_conf_kernel  ('2', '3', '16', '32', '1', False)
        DNN.nn_conf_output  ('2', '5', '32', '1'      , False)
        DNN.nn_conf_output_q('2', '593', '0'          , False)

        DNN.nn_conf_type    ('3', '2'                , False)
        DNN.nn_conf_input   ('3', '5', '32'          , False)
        DNN.nn_conf_kernel  ('3', '2', '1', '32', '2', False)
        DNN.nn_conf_output  ('3', '2', '32', '0'     , False)

        DNN.nn_conf_rrams   ('4', '22'                 , False)
        DNN.nn_conf_type    ('4', '0'                  , False)
        DNN.nn_conf_input   ('4', '128', '1'           , False)
        DNN.nn_conf_kernel  ('4', '128', '1', '10', '0', False)
        DNN.nn_conf_output  ('4', '10', '1', '0'       , False)

        DNN.nn_conf_type    ('5', '3'                 , False)
        DNN.nn_conf_input   ('5', '10', '1'           , False)

    if verbal:
        DNN.nn_print(True)

    # Load network model
    qmodel = torch.load(folder_dir + '\\qmodel.pt')
    #print(qmodel)

    # Load input data
    images = np.uint8(torch.load(folder_dir + '\\data.pt'))
    image_len = images.shape[1]

    # Load targets
    targets = np.uint8(torch.load(folder_dir + '\\targets.pt'))

    # Load predictions
    sim_preds = np.uint8(torch.load(folder_dir + '\\sim_preds.pt'))

def upload_weights(network):
    def write_weights_to_rram(weights, type, rram_index):
        print(f'Writing {type} weights to RRAM #{rram_index}')
        RRAM.switch(str(rram_index), False)
        np_weights = np.int8(weights)

        if type == 'CONV':
            (k_number, k_channel, k_width, k_height) = np_weights.shape
            blocks_per_row = int(32 / (k_width*k_height))

            print('-----------------------------------')
            print('| (row, col) | Gold | Real | Diff |')
            print('-----------------------------------')
            for n in range(k_number):
                brow = int(n / blocks_per_row)
                bcol = int(n % blocks_per_row)
                for krow in range(k_width):
                    for kcol in range(k_height):
                        for ch in range(k_channel):
                            row = brow * k_channel + ch
                            col = bcol * (k_width*k_height) + krow * k_width + kcol
                            addr = row * 256 + col
                            golden = int(np_weights[n][ch][krow][kcol])
                            #print(f'Write {golden:>5} @ ({n:>2}, {ch:>2}, {krow:>2}, {kcol:>2}) to ({row:>3}, {col:>3})')
                            RRAM.write_byte_iter(str(addr), str(golden), True)
                            readout = int(RRAM.read_byte(str(addr), '0', '0x1', False))
                            if readout != golden:
                                print(f'| ({row:>3}, {col:>3}) | {golden:>4} | {readout:>4} | {golden-readout:>4} |')
            print('-----------------------------------')

        elif type == 'MLP':
            (k_number, k_channel) = np_weights.shape

            print('-----------------------------------')
            print('| (row, col) | Gold | Read | Diff |')
            print('-----------------------------------')
            for n in range(k_number):
                for ch in range(k_channel):
                    row = ch
                    col = n
                    addr = row * 256 + col
                    golden = int(np_weights[n][ch])
                    #print(f'Write {golden:>5} @ ({n:>2}, {ch:>2}) to ({row:>3}, {col:>3})')
                    RRAM.write_byte_iter(str(addr), str(golden), True)
                    readout = int(RRAM.read_byte(str(addr), '0', '0x1', False))
                    if readout != golden:
                        print(f'| ({row:>3}, {col:>3}) | {golden:>4} | {readout:>4} | {golden-readout:>4} |')
            print('-----------------------------------')

    if network == 'MLP':
        write_weights_to_rram(qmodel['fc1._packed_params._packed_params'][0].int_repr(), 'MLP' , 9  )
        write_weights_to_rram(qmodel['fc2._packed_params._packed_params'][0].int_repr(), 'MLP' , 12 )

    elif network == 'CONV':
        write_weights_to_rram(qmodel['conv1.weight'].int_repr()                        , 'CONV', 16 )
        write_weights_to_rram(qmodel['conv2.weight'].int_repr()                        , 'CONV', 21 )
        write_weights_to_rram(qmodel['fc3._packed_params._packed_params'][0].int_repr(), 'MLP' , 22 )


def upload_image(index, verbal):
    image = images[int(index)]

    # Upload the image
    DNN.in_conf_len(str(image_len), True)
    for i in range(image_len):
        for j in range(image_len):
            if image[i][j] != 0:
                DNN.in_fill(str(i*image_len + j), str(image[i][j]), True)

    # Print the image if required
    if verbal:
        DNN.in_print(True)


def test_inference(WL, count):
    # Read the image and do th inference
    print( '---------------------------')
    print(f'| Index | Gold | Sim | TC |')
    print( '---------------------------')
    count = int(count)
    ltargets = np.resize(targets,  count)
    lsim_preds = np.resize(sim_preds,  count)
    tc_preds = np.empty(count, dtype=np.uint8)
    tick = time.time()
    for index in range(count):
        # Upload image
        upload_image(index, False)

        # Inference
        tc_preds[index] = int(DNN.forward(WL, False))

        # Print the result
        print(f'| {index:>5} | {ltargets[index]:>4} | {lsim_preds[index]:>3} | {tc_preds[index]:>2} |')
    passed_time = time.time()-tick
    print( '---------------------------')
    print(f'| Pred Acc:   {np.sum(lsim_preds == ltargets):5d}/{count:5d} |')
    print(f'|   TC Acc:   {np.sum(tc_preds == ltargets):5d}/{count:5d} |')
    print(f'| Duration: {passed_time:9.2f} sec |')
    print( '---------------------------')


def gui():
    MNIST_GUI()


def decode(parameters):
    """ Decode the split version of the command

    Keyword arguments:
    pyterminal -- current connected COM port
    parameters -- split version of the command
    """
    if   parameters[1] == 'config_network': config_network(parameters[2], True         )
    elif parameters[1] == 'upload_weights': upload_weights(parameters[2]               )
    elif parameters[1] == 'upload_image'  : upload_image  (parameters[2], True         )
    elif parameters[1] == 'test_inference': test_inference(parameters[2], parameters[3])
    elif parameters[1] == 'gui'           : gui           (                            )
    else: PT.unknown(parameters)
