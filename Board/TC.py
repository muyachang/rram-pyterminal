from datetime import datetime
from tkinter import Tk, filedialog
import CommandMap as CM
import PyTerminal as PT


def connect(verbal=True):
    """ Connect to the testchip, halt it, and get its ID (should be `0x2BA01477`)

    Args:
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    Returns:
        str: The ID if the testchip (should be `0x2BA01477`)

    """
    return PT.send_command(CM.CM_TC + ' ' + CM.CM_TC_CONNECT, verbal)


def disconnect(verbal=True):
    """ Unhalt the testchip and disconnect from it

    Args:
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_TC + ' ' + CM.CM_TC_DISCONNECT, verbal)


def read(address, verbal=True):
    """ Read the value from *address*

    Args:
        address (str): Address to be read from
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    return PT.send_command(CM.CM_TC + ' ' + CM.CM_TC_READ + ' ' + address, verbal)


def write(address, value, verbal=True):
    """ Write *value* to *address*

    Args:
        address (str): Address to be written to
        value (str): Value to be written to
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_TC + ' ' + CM.CM_TC_WRITE + ' ' + address + ' ' + value, verbal)


def list_configs(verbal=True):
    """ List the testchip configurations

    Args:
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_TC + ' ' + CM.CM_TC_LIST, verbal)


def save_config(number, force=False, verbal=True):
    """ Save the testchip configuration to slot *number*

    Args:
        number (str): Slot number, from *0*~*9*
        force  (bool, optional): Whether to force the save without confirming. Defaults to False
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    if force:
        PT.send_command(CM.CM_TC + ' ' + CM.CM_TC_SAVE + ' ' + number + ' ' + datetime.now().strftime("%m/%d/%Y_%H:%M:%S"), verbal)
    else:
        confirm = input(f'[WARNING] This will overwrite the config for chip #{number}, are you sure? (y/n)')
        if confirm.lower() == 'y':
            PT.send_command(CM.CM_TC + ' ' + CM.CM_TC_SAVE + ' ' + number + ' ' + datetime.now().strftime("%m/%d/%Y_%H:%M:%S"), verbal)


def load_config(number, verbal=True):
    """ Load the testchip configuration from slot *number*

    Args:
        number (str): Slot number, from *0*~*9*
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    PT.send_command(CM.CM_TC + ' ' + CM.CM_TC_LOAD + ' ' + number, verbal)


def download_config(verbal=True):
    """ Download and save the testchip configuration to local file.
         (Pretty slow for now, I'll see if I want to optimize someday 0u0)

    Args:
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    TC_CONFIG_START_ADDRESS = 0x20070000  # Start at 448 KB
    TC_CONFIG_SIZE          = 0x00010000  # 64 KB for each TC
    root = Tk()
    root.withdraw()
    f = filedialog.asksaveasfile(title = "Save config as",
                                 filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
    if f is None:
        print('No file specified')
        return

    for address in range(TC_CONFIG_START_ADDRESS, TC_CONFIG_START_ADDRESS+TC_CONFIG_SIZE, 4):
        if verbal:
            print(f'\r[INFO] Progress: {int((address-TC_CONFIG_START_ADDRESS)*100/TC_CONFIG_SIZE)}%', end='')
        f.write(read(str(address) + '\n', False))
    if verbal:
        print(f'\r[INFO] Progress: 100%')
    f.close()
    root.destroy()


def upload_config(verbal=True):
    """ Upload the testchip configuration from local file.
         (Pretty slow for now, I'll see if I want to optimize someday 0u0)

    Args:
        verbal (bool, optional): Whether to print the response or not. Defaults to True.

    """
    TC_CONFIG_START_ADDRESS = 0x20070000  # Start at 448 KB
    TC_CONFIG_SIZE          = 0x00010000  # 64 KB for each TC
    root = Tk()
    root.withdraw()
    f = filedialog.askopenfile(title = "Open a config",
                               filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
    if f is None:
        print('No file specified')
        return

    for address in range(TC_CONFIG_START_ADDRESS, TC_CONFIG_START_ADDRESS+TC_CONFIG_SIZE, 4):
        if verbal:
            print(f'\r[INFO] Progress: {int((address-TC_CONFIG_START_ADDRESS)*100/TC_CONFIG_SIZE)}%', end='')
        write(str(address), f.readline(), False)
    if verbal:
        print(f'\r[INFO] Progress: 100%')
    f.close()
    root.destroy()


def decode(parameters):
    """ Decode the command

    Args:
        parameters (list): Command in List form.

    """
    if   parameters[1] == 'connect'   : connect        (                            )
    elif parameters[1] == 'disconnect': disconnect     (                            )
    elif parameters[1] == 'read'      : read           (parameters[2],              )
    elif parameters[1] == 'write'     : write          (parameters[2], parameters[3])
    elif parameters[1] == 'list'      : list_configs   (                            )
    elif parameters[1] == 'save'      : save_config    (parameters[2],              )
    elif parameters[1] == 'load'      : load_config    (parameters[2],              )
    elif parameters[1] == 'download'  : download_config(                            )
    elif parameters[1] == 'upload'    : upload_config  (                            )
    else: PT.unknown(parameters)
