import CommandMap as CM
import PyTerminal as PT

def in_clear(verbal):
    """ Clear the input image

    Args:
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_IN_CLEAR, verbal)


def in_conf_len(length, verbal):
    """ Configure the length of input image

    Args:
        length (str): The length of input picture (assume the picture is square)
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_IN_CONF_LEN + ' ' + length, verbal)



def in_fill(address, value, verbal):
    """ Write `value` to `address`

    Args:
        address (str): Address to be written to
        value (str): Value to be written to
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_IN_FILL + ' ' + address + ' ' + value, verbal)


def in_print(verbal):
    """ Print the input image

    Args:
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_IN_PRINT, verbal)


def nn_clear(verbal):
    """ Clear the network

    Args:
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_NN_CLEAR, verbal)


def nn_conf_type(layer, type, verbal):
    """ Configure layer type for `layer`

    Args:
        layer (str): Layer number, could be `0` ~ `19`
        type (str): Layer type, could be `0` for FC or `1` for Convolution
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_NN_CONF_TYPE + ' ' + layer + ' ' + type, verbal)


def nn_conf_rrams(layer, rrams, verbal):
    """ Configure RRAM module location for `layer`

    Args:
        layer (str): Layer number, could be `0` ~ `19`
        rrams (str): RRAM Module number that this layer resides at
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_NN_CONF_RRAMS + ' ' + layer + ' ' + rrams, verbal)


def nn_conf_input(layer, input_length, input_channel, verbal):
    """ Configure input for `layer`

    Args:
        layer (str): Layer number, could be `0` ~ `19`
        input_length (str): The length of input activation at `layer` (assume the activation is square)
        input_channel (str): The channel of input activation at `layer`
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_NN_CONF_INPUT + ' ' + layer + ' ' + input_length + ' ' + input_channel, verbal)


def nn_conf_kernel(layer, kernel_length, kernel_number, stride, verbal):
    """ Configure kernel for `layer`

    Args:
        layer (str): Layer number, could be `0` ~ `19`
        kernel_length (str): The length of kernel at `layer`  (assume the activation is square)
        kernel_number (str): The number of kernel at `layer`
        stride (str): The stride of kernel at `layer`
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_NN_CONF_KERNEL + ' ' + layer + ' ' + kernel_length + ' ' + kernel_number + ' ' + stride, verbal)


def nn_conf_act(layer, activation, verbal):
    """ Configure activation setting for `layer`

    Args:
        layer (str): Layer number, could be `0` ~ `19`
        activation (str): Whether the output of `layer` is activation
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_NN_CONF_ACT + ' ' + layer + ' ' + activation, verbal)


def nn_conf_quant(layer, q_scale, q_zero_point, verbal):
    """ Configure Quantization for `layer`

    Args:
        layer (str): Layer number, could be `0` ~ `19`
        q_scale (str): Scale of the quantization at `layer`
        q_zero_point (str): Zero Point of the quantization at `layer`
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_NN_CONF_QUANT + ' ' + layer + ' ' + q_scale + ' ' + q_zero_point, verbal)


def nn_conf_ecc(layer, ecc, verbal):
    """ Configure ECC for `layer`

    Args:
        layer (str): Layer number, could be `0` ~ `19`
        ecc (str): Whether the weights at `layer` is ECC enabled.
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_NN_CONF_ECC + ' ' + layer + ' ' + ecc, verbal)


def nn_print       (verbal):
    """ Print the network

    Args:
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_NN_PRINT, verbal)


def forward(WL, verbal):
    """ Run 1 forward inference

    Args:
        WL (str): The Compute-In-Memory (CIM) scheme, could be `1`~`9`
        verbal (bool): Whether to print the response or not.
    Returns:
        The prediction of inference
    """
    return PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_FORWARD + ' ' + WL, verbal)


def decode(parameters):
    """ Decode the command

    Args:
        parameters (list): Command in List form.
    """
    if   parameters[1] == 'in_clear'      : in_clear    (True)
    elif parameters[1] == 'in_conf_len'   : in_conf_len (parameters[2], True)
    elif parameters[1] == 'in_fill'       : in_fill     (parameters[2], parameters[3], True)
    elif parameters[1] == 'in_print'      : in_print    (True)

    elif parameters[1] == 'nn_clear'      : nn_clear       (True)
    elif parameters[1] == 'nn_conf_type'  : nn_conf_type   (parameters[2], parameters[3], True)
    elif parameters[1] == 'nn_conf_rrams' : nn_conf_rrams  (parameters[2], parameters[3], True)
    elif parameters[1] == 'nn_conf_input' : nn_conf_input  (parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'nn_conf_kernel': nn_conf_kernel (parameters[2], parameters[3], parameters[4], parameters[5], True)
    elif parameters[1] == 'nn_conf_act'   : nn_conf_act    (parameters[2], parameters[3], True)
    elif parameters[1] == 'nn_conf_quant' : nn_conf_quant  (parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'nn_conf_ecc'   : nn_conf_ecc    (parameters[2], parameters[3], True)
    elif parameters[1] == 'nn_print'      : nn_print       (True)

    elif parameters[1] == 'forward'     : forward     (parameters[2], True)
    else: PT.unknown(parameters)
