import PyTerminal as PT

if __name__ == '__main__':
    """ Initialize PyTerminal and try to connect to a board and start up the terminal

    Keyword arguments:
    """

    if PT.connect():
        while 1:
            command = input("ICSRL> ")
            if command == 'exit':
                exit()
            elif command != '':
                PT.decode_command(command)
            elif not PT.alive():
                decision = input('[WARNING] Evaluation board lost, do you want to exit (Y/N)? ')
                if decision.lower() == 'y':
                    exit()
    else:
        print('[ERROR] Connection failed, could not find the board')