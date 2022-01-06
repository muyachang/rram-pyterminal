import PyTerminal as PT

def example_function1():
    """ Example function

    """
    print("This is an example function, feel free to add more of yours in this module")


def decode(parameters):
    """ Decode the command

    Args:
        parameters (list): Command in List form.
    """
    if   parameters[1] == 'example_function1'  : example_function1()
    else: PT.unknown(parameters)
