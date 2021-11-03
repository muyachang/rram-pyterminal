from PyTerminal import PyTerminal

if __name__ == '__main__':
    pyterminal = PyTerminal()

    if pyterminal.connect():
        while 1:
            command = input("ICSRL> ")
            if command == 'exit':
                exit()
            elif command != '':
                pyterminal.decode_command(command)
    else:
        print('[ERROR] Connection failed, could not find the board')