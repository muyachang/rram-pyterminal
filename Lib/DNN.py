import CommandMap as CM
import PyTerminal as PT

def in_clear(verbal):
    """

    Keyword arguments:
        verbal -- whether to print the response or not
    """
    return PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_IN_CLEAR, verbal)


def in_conf_len(length, verbal):
    """

    Keyword arguments:
        verbal -- whether to print the response or not
    """
    return PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_IN_CONF_LEN + ' ' + length, verbal)



def in_fill(address, value, verbal):
    """

    Keyword arguments:
        verbal -- whether to print the response or not
    """
    return PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_IN_FILL + ' ' + address + ' ' + value, verbal)


def in_print(verbal):
    """

    Keyword arguments:
        verbal -- whether to print the response or not
    """
    return PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_IN_PRINT, verbal)


def nn_clear       (verbal):
    """

    Keyword arguments:
        verbal -- whether to print the response or not
    """
    return PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_NN_CLEAR, verbal)


def nn_conf_type   (layer, type, verbal):
    """

    Keyword arguments:
        verbal -- whether to print the response or not
    """
    return PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_NN_CONF_TYPE + ' ' + layer + ' ' + type, verbal)


def nn_conf_rrams  (layer, rrams, verbal):
    """

    Keyword arguments:
        verbal -- whether to print the response or not
    """
    return PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_NN_CONF_RRAMS + ' ' + layer + ' ' + rrams, verbal)


def nn_conf_input  (layer, input_length, input_channel, verbal):
    """

    Keyword arguments:
        verbal -- whether to print the response or not
    """
    return PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_NN_CONF_INPUT + ' ' + layer + ' ' + input_length + ' ' + input_channel, verbal)


def nn_conf_kernel (layer, kernel_length, kernel_number, stride, verbal):
    """

    Keyword arguments:
        verbal -- whether to print the response or not
    """
    return PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_NN_CONF_KERNEL + ' ' + layer + ' ' + kernel_length + ' ' + kernel_number + ' ' + stride, verbal)


def nn_conf_act    (layer, activation, verbal):
    """

    Keyword arguments:
        verbal -- whether to print the response or not
    """
    return PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_NN_CONF_ACT + ' ' + layer + ' ' + activation, verbal)


def nn_conf_quant  (layer, q_scale, q_zero_point, verbal):
    """

    Keyword arguments:
        verbal -- whether to print the response or not
    """
    return PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_NN_CONF_QUANT + ' ' + layer + ' ' + q_scale + ' ' + q_zero_point, verbal)


def nn_conf_ecc    (layer, ecc, verbal):
    """

    Keyword arguments:
        verbal -- whether to print the response or not
    """
    return PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_NN_CONF_ECC + ' ' + layer + ' ' + ecc, verbal)


def nn_print       (verbal):
    """

    Keyword arguments:
        verbal -- whether to print the response or not
    """
    return PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_NN_PRINT, verbal)


def forward(WL, verbal):
    """

    Keyword arguments:
        verbal -- whether to print the response or not
    """
    return PT.send_command(CM.CM_DNN + ' ' + CM.CM_DNN_FORWARD + ' ' + WL, verbal)


def decode(parameters):
    """ Decode the split version of the command

    Keyword arguments:
        parameters -- split version of the command
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
