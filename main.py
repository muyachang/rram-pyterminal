from PyTerminal import PyTerminal
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
0
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    PT = PyTerminal()

    print('<< TC Terminal >>')
    while 1 :
        command = input("ICSRL> ")
        if command == 'exit':
            exit()
        elif command != '':
            PT.decodeCommand(command)