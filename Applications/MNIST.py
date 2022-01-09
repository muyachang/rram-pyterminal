import CommandMap as CM
import PyTerminal as PT

import importlib
import random
import time
import numpy as np
import io
import torch
import math

import RRAM, DNN

from tkinter import *
from tkinter import font

from PIL import Image, ImageTk


def conf_network(network, verbal):
    """ Configure MNIST network type

    Args:
        network (str): Network type
        verbal (bool): Whether to print the configured network or not.
    """

    # Some global variabls
    global folder_dir
    global weights, targets, sim_preds
    global images, image_len
    global mapping
    global layers

    # Folder directory
    if 'folder_dir' in globals():
        sys.path.remove(folder_dir)

    if network == 'MLP':
        folder_dir = 'D:\Dropbox (GaTech)\GaTech\ICSRL\Projects\9. RRAM\Evaluation Board\MNIST\data_256_fc32_fc10'
    elif network == 'MLP2':
        folder_dir = 'D:\Dropbox (GaTech)\GaTech\ICSRL\Projects\9. RRAM\Evaluation Board\MNIST\data_484_fc64_fc10'
    elif network == 'CONV':
        folder_dir = 'D:\Dropbox (GaTech)\GaTech\ICSRL\Projects\9. RRAM\Evaluation Board\MNIST\data_256_conv16_conv32_fc10'

    sys.path.append(folder_dir)

    # Load network model
    weights = torch.load(folder_dir + '\\weights.pt')

    # Read the mapping and run sanity check against weights
    f = open(folder_dir + '\\mapping.txt', 'r')
    mapping = eval(f.readline())

    # Load input data
    images = np.uint8(torch.load(folder_dir + '\\images.pt'))
    image_len = images.shape[1]

    # Load targets
    targets = np.uint8(torch.load(folder_dir + '\\targets.pt'))

    # Load predictions
    sim_preds = np.uint8(torch.load(folder_dir + '\\sim_preds.pt'))

    # Load the model and configure the network
    import model
    model = importlib.reload(model)

    layer = 0
    layers = []
    trainable_layer = 0
    input_length = image_len
    scale = 1

    for name, module in model.Net.named_modules(model.Net()):
        if isinstance(module, torch.ao.quantization.stubs.QuantStub) or \
           isinstance(module, torch.ao.quantization.stubs.DeQuantStub) or \
           isinstance(module, model.Net):
            continue

        layers.append({})
        #print(f'Name: {name}, Module: {module}')

        # If it's a trainable layer (containing weights)
        if hasattr(module, 'weight'):
            #print(f'\tmapping layer {layer} to rram {mapping[trainable_layer][0]}')
            layers[layer]['rrams'] = mapping[trainable_layer]
            trainable_layer += 1
            if isinstance(module, torch.nn.modules.linear.Linear):
                layers[layer]['weights'] = weights[name + '._packed_params._packed_params'][0]
                scale = int(weights[name + '.scale']/weights[name + '._packed_params._packed_params'][0].q_scale())
            elif isinstance(module, torch.nn.modules.conv.Conv2d):
                layers[layer]['weights'] = weights[name + '.weight']
                scale = int(weights[name + '.scale']/weights[name + '.weight'].q_scale())
        else:
            layers[layer]['rrams'] = []
            layers[layer]['weights'] = []

        if isinstance(module, torch.nn.modules.linear.Linear):
            layers[layer]['type'          ] = CM.CM_DNN_TYPE_LINEAR
            layers[layer]['input_length'  ] = module.in_features
            layers[layer]['input_channel' ] = 0
            layers[layer]['kernel_length' ] = module.in_features
            layers[layer]['kernel_channel'] = 0
            layers[layer]['kernel_number' ] = module.out_features
            layers[layer]['stride'        ] = 0
            layers[layer]['output_length' ] = module.out_features
            layers[layer]['output_channel'] = 0
            layers[layer]['output_q_scale'] = 1
            layers[layer]['output_q_zp'   ] = 0
        elif isinstance(module, torch.nn.modules.conv.Conv2d):
            layers[layer]['type'          ] = CM.CM_DNN_TYPE_CONV
            layers[layer]['input_length'  ] = input_length
            layers[layer]['input_channel' ] = module.in_channels
            layers[layer]['kernel_length' ] = module.kernel_size[0]
            layers[layer]['kernel_channel'] = module.in_channels
            layers[layer]['kernel_number' ] = module.out_channels
            layers[layer]['stride'        ] = module.stride[0]
            layers[layer]['output_length' ] = int((input_length - module.kernel_size[0])/module.stride[0] + 1)
            layers[layer]['output_channel'] = module.out_channels
            layers[layer]['output_q_scale'] = 1
            layers[layer]['output_q_zp'   ] = 0
        elif isinstance(module, torch.nn.modules.pooling.MaxPool2d):
            layers[layer]['type'          ] = CM.CM_DNN_TYPE_MAXPOOL
            layers[layer]['input_length'  ] = input_length
            layers[layer]['input_channel' ] = layers[layer-1]['output_channel']
            layers[layer]['kernel_length' ] = module.kernel_size
            layers[layer]['kernel_channel'] = 1
            layers[layer]['kernel_number' ] = layers[layer-1]['output_channel']
            layers[layer]['stride'        ] = module.stride
            layers[layer]['output_length' ] = int((input_length - module.kernel_size)/module.stride + 1)
            layers[layer]['output_channel'] = layers[layer-1]['output_channel']
            layers[layer]['output_q_scale'] = 1
            layers[layer]['output_q_zp'   ] = 0
        elif isinstance(module, torch.nn.modules.activation.ReLU):
            layers[layer]['type'          ] = CM.CM_DNN_TYPE_RELU
            layers[layer]['input_length'  ] = input_length
            layers[layer]['input_channel' ] = layers[layer-1]['output_channel']
            layers[layer]['kernel_length' ] = 0
            layers[layer]['kernel_channel'] = 0
            layers[layer]['kernel_number' ] = 0
            layers[layer]['stride'        ] = 0
            layers[layer]['output_length' ] = input_length
            layers[layer]['output_channel'] = layers[layer-1]['output_channel']
            layers[layer]['output_q_scale'] = scale
            layers[layer]['output_q_zp'   ] = 0

        input_length = layers[layer]['output_length']
        layer += 1

    layers.append({})
    layers[layer]['rrams'         ] = []
    layers[layer]['weights'       ] = []
    layers[layer]['type'          ] = CM.CM_DNN_TYPE_ARGMAX
    layers[layer]['input_length'  ] = input_length
    layers[layer]['input_channel' ] = layers[layer-1]['output_channel']
    layers[layer]['kernel_length' ] = 0
    layers[layer]['kernel_channel'] = 0
    layers[layer]['kernel_number' ] = 0
    layers[layer]['stride'        ] = 0
    layers[layer]['output_length' ] = 0
    layers[layer]['output_channel'] = 0
    layers[layer]['output_q_scale'] = 1
    layers[layer]['output_q_zp'   ] = 0

    DNN.nn_clear(False)
    for layer_index, layer_info in enumerate(layers):
        for index_r, row in enumerate(layer_info['rrams']):
            for index_c, col in enumerate(row):
                DNN.nn_conf_rrams   (str(layer_index), str(index_r), str(index_c), str(layer_info['rrams'][index_r][index_c]), False)
        DNN.nn_conf_type    (str(layer_index), str(layer_info['type']), False)
        DNN.nn_conf_input   (str(layer_index), str(layer_info['input_length']), str(layer_info['input_channel']), False)
        DNN.nn_conf_kernel  (str(layer_index), str(layer_info['kernel_length']), str(layer_info['kernel_channel']), str(layer_info['kernel_number']), str(layer_info['stride']), False)
        DNN.nn_conf_output  (str(layer_index), str(layer_info['output_length']), str(layer_info['output_channel']), False)
        DNN.nn_conf_output_q(str(layer_index), str(layer_info['output_q_scale']), str(layer_info['output_q_zp']), False)
    if verbal:
        DNN.nn_print(True)


def upload_weights(verbal):
    """ Upload MNIST weights on the current network

    Args:
        verbal (bool): Whether to print the uploading progress or not.
    """
    def write_weights_to_rram(weights, type, rram_indices):
        if type == 0: # MLP
            np_weights = np.int8(weights.int_repr())
            (k_number, k_channel) = np_weights.shape

            for tile_ch in range(math.ceil(k_channel/256)):
                for tile_n in range(math.ceil(k_number/32)):
                    ch_offset = tile_ch*256
                    n_offset = tile_n*32
                    print(f'Writing Type \'{type}\' weights[{tile_ch}][{tile_n}] to RRAM #{rram_indices[tile_ch][tile_n]}')
                    RRAM.switch(str(rram_indices[tile_ch][tile_n]), False)

                    if verbal:
                        print('╔════════════╦══════╦══════╦══════╗')
                        print('║ (row, col) ║ Gold ║ Read ║ Diff ║')
                        print('╟────────────╫──────╫──────╫──────╢')
                    for ch in range(min(256, k_channel-tile_ch*256)):
                        for n in range(min(32, k_number-tile_n*32)):
                            golden = int(np_weights[n_offset+n][ch_offset+ch])
                            #print(f'Write {golden:>5} @ ({n:>2}, {ch:>2}) to ({row:>3}, {col:>3})')
                            local_addr = ch * 256 + n
                            RRAM.write_byte_iter(str(local_addr), str(golden), True)
                            if verbal:
                                readout = int(RRAM.read_byte(str(local_addr), '0', '0x1', False))
                                if readout != golden:
                                    print(f'║ ({ch:>3}, {n:>3}) ║ {golden:>4} ║ {readout:>4} ║ {golden-readout:>4} ║')
                    if verbal:
                        print('╚════════════╩══════╩══════╩══════╝')

        elif type == 1: # CONV
            np_weights = np.int8(weights.int_repr())
            (k_number, k_channel, k_width, k_height) = np_weights.shape
            blocks_per_row = int(32 / (k_width*k_height))

            if verbal:
                print('╔════════════╦══════╦══════╦══════╗')
                print('║ (row, col) ║ Gold ║ Read ║ Diff ║')
                print('╟────────────╫──────╫──────╫──────╢')
            for n in range(k_number):
                brow = int(n / blocks_per_row)
                bcol = int(n % blocks_per_row)
                for krow in range(k_width):
                    for kcol in range(k_height):
                        for ch in range(k_channel):
                            row = brow * k_channel + ch
                            col = bcol * (k_width*k_height) + krow * k_width + kcol
                            local_addr = row * 256 + col
                            golden = int(np_weights[n][ch][krow][kcol])
                            #print(f'Write {golden:>5} @ ({n:>2}, {ch:>2}, {krow:>2}, {kcol:>2}) to ({row:>3}, {col:>3})')
                            RRAM.write_byte_iter(str(local_addr), str(golden), True)
                            if verbal:
                                readout = int(RRAM.read_byte(str(local_addr), '0', '0x1', False))
                                if readout != golden:
                                    print(f'║ ({row:>3}, {col:>3}) ║ {golden:>4} ║ {readout:>4} ║ {golden-readout:>4} ║')
            if verbal:
                    print('╚════════════╩══════╩══════╩══════╝')

    for layer_index, layer_info in enumerate(layers):
        write_weights_to_rram(layer_info['weights'], layer_info['type'], layer_info['rrams'])


def upload_image(index, verbal):
    """ Upload a MNIST image on the current network

    Args:
        index (str): Index of the image
        verbal (bool): Whether to print the uploaded image or not.
    """
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


def test_inference(network, WL_start, WL_end, count, verbal):
    """ Test MNIST inference

    Args:
        network (str): Network type
        WL_start (str): Starting WL Scheme (1~9)
        WL_end (str): Endding WL Scheme (WL_start~9)
        count (str): Number of images that want to inference on
        verbal (bool): Whether to print the result for each image or not.
    """
    verbal = eval(verbal)
    WL_start = int(WL_start)
    WL_end = int(WL_end)
    conf_network(network, False)

    for WL in range(WL_start, WL_end+1):
        print(f'[INFO] WL Scheme: {WL}')
        # Read the image and do th inference
        if verbal:
            print( '╔═══════╦══════╦═════╦════╗')
            print(f'║ Index ║ Gold ║ Sim ║ TC ║')
            print( '╟───────╫──────╫─────╫────╢')
        count = int(count)
        local_targets = np.resize(targets,  count)
        local_sim_preds = np.resize(sim_preds,  count)
        tc_preds = np.empty(count, dtype=np.uint8)
        tick = time.time()
        for index in range(count):
            if not verbal:
                print(f'\r\tImage {index}', end='')

            # Upload image
            upload_image(index, False)

            # Inference
            tc_preds[index] = int(DNN.forward(str(WL), False))

            # Print the result
            if verbal:
                print(f'║ {index:>5} ║ {local_targets[index]:>4} ║ {local_sim_preds[index]:>3} ║ {tc_preds[index]:>2} ║')
        passed_time = time.time()-tick
        if verbal:
            print( '╟───────╨──────╨─────╨────╢')
        else:
            print('')
            print( '╔═════════════════════════╗')
        print(f'║ Pred Acc:   {np.sum(local_sim_preds == local_targets):5d}/{count:5d} ║')
        print(f'║   TC Acc:   {np.sum(tc_preds == local_targets):5d}/{count:5d} ║')
        print(f'║ Duration: {passed_time:9.2f} sec ║')
        print( '╚═════════════════════════╝')


class GUI:
    def __init__(self):
        """ MNIST GUI Demo Class

        """

        # Initialize the main Panel
        self.master = Tk()
        self.master.title("MNIST GUI")

        # Change default font
        font.nametofont("TkDefaultFont").configure(family="Arial", size=12)

        # Sub panels
        frm_controls = Frame(self.master, padx=5)
        frm_canvas = Frame(self.master, padx=5)
        frm_results = Frame(self.master, padx=5)
        frm_controls.pack(side=LEFT)
        frm_canvas.pack(side=LEFT)
        frm_results.pack(side=LEFT)

        # Sub frames in Control Panel
        frm_image_index = Frame(frm_controls, borderwidth=5, relief='ridge')
        frm_network = Frame(frm_controls, borderwidth=5, relief='ridge')
        frm_wl_scheme = Frame(frm_controls, borderwidth=5, relief='ridge')
        frm_operation = Frame(frm_controls, borderwidth=5, relief='ridge')
        frm_image_index.pack(pady=5)
        frm_network.pack(pady=5)
        frm_wl_scheme.pack(pady=5)
        frm_operation.pack(pady=5)

        # Sub frames in Result Panel
        frm_golden = Frame(frm_results, borderwidth=5, relief='ridge')
        frm_duration = Frame(frm_results, borderwidth=5, relief='ridge')
        frm_prediction = Frame(frm_results, borderwidth=5, relief='ridge')
        frm_golden.pack(pady=5)
        frm_duration.pack(pady=5)
        frm_prediction.pack(pady=5)

        # In Image Index Frame
        Label(frm_image_index, text='Image Index', width=14, font='Arial 14 bold').pack()

        self.txt_image_index = Entry(frm_image_index, width=6, font='Arial 14')
        self.txt_image_index.pack(side=LEFT, padx=5)

        self.btn_random_icon = ImageTk.PhotoImage(Image.open('Applications/btn_random.png').resize((20, 20)))
        Button(frm_image_index, image=self.btn_random_icon, command=self.image_random).pack(side=RIGHT, padx=5)

        self.btn_load_icon = ImageTk.PhotoImage(Image.open('Applications/btn_load.png').resize((20, 20)))
        Button(frm_image_index, image=self.btn_load_icon, command=self.image_load).pack(side=RIGHT, padx=5)

        # In Network Type Frame
        Label(frm_network, text='Network Type', width=14, font='Arial 14 bold').pack()

        networks = ('MLP', 'MLP2')
        self.network_var = StringVar(value=networks[0])
        OptionMenu(frm_network, self.network_var, *networks).pack(side=LEFT, padx=5)
        self.network_change(False)

        self.btn_display_network_icon = ImageTk.PhotoImage(Image.open('Applications/btn_display_network_icon.png').resize((20, 20)))
        Button(frm_network, image=self.btn_display_network_icon, command=self.network_print).pack(side=RIGHT, padx=5)

        self.btn_config_network_icon = ImageTk.PhotoImage(Image.open('Applications/btn_load.png').resize((20, 20)))
        Button(frm_network, image=self.btn_config_network_icon, command=self.network_change).pack(side=RIGHT, padx=5)

        # In WL Scheme Frame
        Label(frm_wl_scheme, text='WL Scheme', width=14, font='Arial 14 bold').pack()

        self.sld_WL = Scale(frm_wl_scheme, from_=1, to=9, orient=HORIZONTAL)
        self.sld_WL.pack()

        # In Operation Frame
        Label(frm_operation, text='Operation', width=14, font='Arial 14 bold').pack()

        self.btn_clear_icon = ImageTk.PhotoImage(Image.open('Applications/btn_clear.png').resize((20, 20)))
        Button(frm_operation, image=self.btn_clear_icon, command=self.clear).pack(side=LEFT, padx=5)

        Button(frm_operation, text="Inference", command=self.image_inference, font='Arial 12').pack(side=RIGHT, padx=5)

        # In Canvas Panel
        self.old_xy = None
        self.canvas = Canvas(frm_canvas, width=400, height=400, bg='white', borderwidth=10, relief='ridge')
        self.canvas.bind('<B1-Motion>', self.canvas_paint)
        self.canvas.bind('<ButtonRelease-1>', self.canvas_reset)
        self.canvas.pack()

        # In Golden Result Frame
        Label(frm_golden, text='Golden', width=12, font='Arial 14 bold').pack()

        self.text_golden = StringVar(value='N/A')
        Label(frm_golden, textvariable=self.text_golden, font=('Arial', 48)).pack()

        # In Duration Frame
        Label(frm_duration, text='Duration (s)', width=12, font='Arial 14 bold').pack()

        self.text_duration = StringVar(value='N/A')
        Label(frm_duration, textvariable=self.text_duration, font=('Arial', 32)).pack()

        # In Prediction Frame
        Label(frm_prediction, text='Prediction', width=12, font='Arial 14 bold').pack()

        self.text_prediction = StringVar(value='N/A')
        Label(frm_prediction, textvariable=self.text_prediction, font=('Arial', 48)).pack()

        # Make it not resizable and place it at center
        self.master.resizable(False, False)
        self.window_center(self.master)
        self.master.mainloop()

    def window_center(self, window):
        """ Place the window at the center of the monitor

        Args:
            window (Tk or Toplevel): The target window
        """
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        frm_width = window.winfo_rootx() - window.winfo_x()
        win_width = width + 2 * frm_width
        titlebar_height = window.winfo_rooty() - window.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = window.winfo_screenwidth() // 2 - win_width // 2
        y = window.winfo_screenheight() // 2 - win_height // 2
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        window.deiconify()


    def canvas_paint(self, new_xy):
        """ Callback for canvas painting

        Args:
            new_xy (tuple): new (x, y)
        """
        if self.old_xy:
            self.canvas.create_line(self.old_xy.x, self.old_xy.y, new_xy.x, new_xy.y, width=40, stipple='gray50', capstyle=ROUND)
        self.old_xy = new_xy


    def canvas_reset(self, new_xy):
        """ Callback for canvas reset

        Args:
            new_xy (tuple): new (x, y), but not used in this function

        """
        self.old_xy = None
        self.txt_image_index.delete(0, 'end')


    def canvas_capture(self):
        """ Capture what's on the canvas

        Returns:
            np.uint8: 2D numpy array

        """
        # Capture the image from Canvas
        ps = self.canvas.postscript(colormode='gray')
        image = Image.open(io.BytesIO(ps.encode('utf-8')))
        image = image.convert(mode='L').resize((image_len, image_len))
        image = np.uint8(image.getdata())
        image = np.floor_divide(np.invert(image), 4)
        image = np.reshape(image, (image_len, image_len))
        return image


    def clear(self):
        """ Clean the canvas and other related information

        """
        self.canvas.delete(ALL)
        self.text_golden.set('N/A')
        self.text_prediction.set('N/A')
        self.text_duration.set('N/A')
        self.txt_image_index.delete(0, 'end')


    def network_change(self, verbal=True):
        """ Change the network type

        Args:
            verbal (bool, optional): Whether to print the response or not. Defaults to True.

        """
        network = self.network_var.get()
        conf_network(network, False)
        if verbal:
            self.network_print('Network Architecture Updated')


    def network_print(self, win_title='Current Network Architecture'):
        """ Pop up a new window showing the updated network

        Args:
            win_title (str): Title of the popped up window

        """
        win_network = Toplevel()
        win_network.title(win_title)
        Label(win_network, text=DNN.nn_print(False), justify= LEFT, font='Courier 14 bold').pack(fill='both', pady=5)
        Button(win_network, text="Okay", command=win_network.destroy).pack(pady=5)
        self.window_center(win_network)


    def image_load(self):
        """ Load image index from 'txt_image_index'

        """
        index = int(self.txt_image_index.get())

        # Paint the image onto the canvas
        tkimage = np.invert(4*images[index])
        tkimage = Image.fromarray(tkimage)
        tkimage = tkimage.resize((self.canvas.winfo_width(), self.canvas.winfo_height()))
        self.tkimage = ImageTk.PhotoImage(image=tkimage)
        self.canvas.create_image(0, 0, anchor="nw", image=self.tkimage)

        # Load golden and clear prediction/duration
        self.text_golden.set(targets[index])
        self.text_prediction.set('N/A')
        self.text_duration.set('N/A')


    def image_random(self):
        """ Choose a random image

        """
        self.txt_image_index.delete(0, 'end')
        self.txt_image_index.insert(0, str(random.randint(0, 10000)))
        self.image_load()


    def image_inference(self):
        """ Upload the image and run inference

        """
        # Clear the prediction and duration first
        self.text_prediction.set('N/A')
        self.text_duration.set('N/A')
        self.master.update()

        # Upload the image
        if self.txt_image_index.get() != '':
            upload_image(str(self.txt_image_index.get()), False)
        else:
            image = self.canvas_capture()
            DNN.in_conf_len(str(image_len), True)
            for i in range(image_len):
                for j in range(image_len):
                    if image[i][j] != 0:
                        DNN.in_fill(str(i*image_len+j), str(image[i][j]), True)

        # Print the result
        tick = time.time()
        pred = DNN.forward(str(self.sld_WL.get()), False)
        passed_time = time.time()-tick
        self.text_duration.set(f'{passed_time:.2f}')
        self.text_prediction.set(pred)


def decode(parameters):
    """ Decode the command

    Args:
        parameters (list): Command in List form.
    """
    if   parameters[1] == 'conf_network'  : conf_network(parameters[2], True         )
    elif parameters[1] == 'upload_weights': upload_weights(True                        )
    elif parameters[1] == 'upload_image'  : upload_image  (parameters[2], True         )
    elif parameters[1] == 'test_inference': test_inference(parameters[2], parameters[3], parameters[4], parameters[5], parameters[6])
    elif parameters[1] == 'gui'           : GUI           (                            )
    else: PT.unknown(parameters)
