import time
import serial
from Lib import DEMO, ASCII, RRAM, VECTOR, DNN
from Board import EEPROM, PM, LED, DF, DAC, TC, BOARD
import USER
import CommandMap as CM

VID = '0x03EB'    # Atmel
PID = '0x204B'    # LUFA USB to Serial Demo Application
BAUDRATE = 115200 #
TIMEOUT = 3      # Seconds

class PyTerminal:
    def __init__(self):
        """ Constructor for the class

        Keyword arguments:
        """
        self.ser = serial.Serial()

    def __del__(self):
        """ Constructor for the class

        Keyword arguments:
        """
        self.ser.__del__()

    def connect(self):
        """ Automatically connect to the board based on the VID and PID information, and get the board version to make
            sure the correct board is connected.

        Keyword arguments:
        """
        from serial.tools import list_ports
        for port in list_ports.comports():
            if port.vid == int(VID, 0) and port.pid == int(PID, 0):
                self.ser = serial.Serial(port.name, baudrate=BAUDRATE, timeout=TIMEOUT)
                try:
                    version = BOARD.version(self, False)
                    print('[INFO] Evaluation board with version ' + version + ' connected @ ' + port.name)
                    # Fix the problem so that we don't have to init the TC every time we relaunch PyTerminal
                    self.ser.write(str.encode(CM.CM_RRAM + ' \n'))
                    return True
                except:
                    print('[ERROR] Unable to retrieve board version')
                    break
        return False

    def alive(self):
        """ Check if the board is still connected, if not we try to connect it again

        Keyword arguments:
        """
        try:
            self.ser.in_waiting
            return True
        except:
            return self.connect()

    def send_command(self, command, verbal):
        """ Send the command to the board through COM port, print the response, and return the response.

        Keyword arguments:
        verbal -- whether to print the response or not
        """
        # Send out the command and Give it some time to process
        self.ser.reset_output_buffer()
        self.ser.reset_input_buffer()
        self.ser.write(str.encode(command + '\n'))

        # Wait for EOT
        response = b''
        while 1:
            char = self.ser.read(1)
            if char == ASCII.EOT:
                # For readability, we insert \n for some cases
                if verbal and response != b'' and response.decode('utf-8')[-1] != '\n':
                    print('')
                break
            elif char == b'':
                print('Read Timeout')
                break
            elif verbal:
                print(char.decode('utf-8'), end='', flush=True)
            response += char

        return response.decode('utf-8')

    @staticmethod
    def unknown(parameters):
        """ Print out the unknown command

        Keyword arguments:
        parameters -- the split version of the command
        """
        print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')

    def decode_command(self, command):
        """ Split the command and decode it based on the first parameter

        Keyword arguments:
        command -- the original human readable command
        """
        try:
            # Split the command and fill up to 8 list elements
            parameters = command.split()
            for i in range(len(parameters), 16):
                parameters.append('')

            if   parameters[0] == "BOARD" :  BOARD.decode(self, parameters)
            elif parameters[0] == "PM"    :     PM.decode(self, parameters)
            elif parameters[0] == "DAC"   :    DAC.decode(self, parameters)
            elif parameters[0] == "DF"    :     DF.decode(self, parameters)
            elif parameters[0] == "EEPROM": EEPROM.decode(self, parameters)
            elif parameters[0] == "LED"   :    LED.decode(self, parameters)
            elif parameters[0] == "TC"    :     TC.decode(self, parameters)
            elif parameters[0] == "DEMO"  :   DEMO.decode(self, parameters)
            elif parameters[0] == "RRAM"  :   RRAM.decode(self, parameters)
            elif parameters[0] == "VECTOR": VECTOR.decode(self, parameters)
            elif parameters[0] == "DNN"   :    DNN.decode(self, parameters)
            elif parameters[0] == "USER"  :   USER.decode(self, parameters)
            else: self.unknown(parameters)
        
        # If the atmel is reset, we need to reopen it again
        except serial.SerialException:
            self.ser.close()
            self.ser.open()
            self.decode_command(command)
        except Exception as e:
            print('[ERROR] Wrong command format')
            print(e)
