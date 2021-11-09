from PyTerminal import PyTerminal

if __name__ == '__main__':
    """ Initialize PyTerminal and try to connect to a board and start up the terminal

    Keyword arguments:
    """

    pyterminal = PyTerminal()

    if pyterminal.connect():
        while 1:
            command = input("ICSRL> ")
            if command == 'exit':
                exit()
            elif command != '':
                pyterminal.decode_command(command)
            elif not pyterminal.alive():
                decision = input('[WARNING] Evaluation board lost, do you want to exit (Y/N)? ')
                if decision.lower() == 'y':
                    exit()
    else:
        print('[ERROR] Connection failed, could not find the board')