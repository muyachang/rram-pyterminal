from PyTerminal import PyTerminal

PT = PyTerminal()

print('<< TC Terminal >>')
while 1 :
    command = input("ICSRL> ")
    if command == 'exit':
        exit()
    elif command != '':
        PT.decodeCommand(command)