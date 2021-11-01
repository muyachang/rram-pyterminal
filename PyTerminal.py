import glob
import time
import sys
import serial
from Lib import DEMO, ASCII, RRAM, VECTOR
from Board import EEPROM, PM, LED, DF, DAC, TC
import USER
import CommandMap as CM


class PyTerminal:
    
    def __init__(self):
        print('Available ports:')
        available_ports = self.list_ports()
        for i, p in enumerate(available_ports):
            print('Port[' + str(i) + '] = ' + p)
        index = input("Enter the index of the port: ")
        self.ser = serial.Serial(port=available_ports[int(index)], baudrate=115200, timeout=20)

        # Fix the problem so that we don't have to init the TC every time we relaunch PyTerminal
        self.ser.write(str.encode(CM.CM_RRAM + ' \n'))

    def __del__(self):
        self.ser.close()
        
    def send_command(self, command, verbal):
        # Send out the command and Give it some time to process
        self.ser.reset_output_buffer()
        self.ser.reset_input_buffer()
        self.ser.write(str.encode(command + '\n'))
        time.sleep(0.001)
        
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
    def list_ports():
        """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result

    @staticmethod
    def unknown(parameters):
        print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')
    
    def decode_command(self, command):
        try:
            # Split the command and fill up to 8 list elements
            parameters = command.split()
            for i in range(len(parameters), 16):
                parameters.append('')

            if   parameters[0] == "PM"    :     PM.decode(self, parameters)
            elif parameters[0] == "DAC"   :    DAC.decode(self, parameters)
            elif parameters[0] == "DF"    :     DF.decode(self, parameters)
            elif parameters[0] == "EEPROM": EEPROM.decode(self, parameters)
            elif parameters[0] == "LED"   :    LED.decode(self, parameters)
            elif parameters[0] == "TC"    :     TC.decode(self, parameters)
            elif parameters[0] == "DEMO"  :   DEMO.decode(self, parameters)
            elif parameters[0] == "RRAM"  :   RRAM.decode(self, parameters)
            elif parameters[0] == "VECTOR": VECTOR.decode(self, parameters)
            elif parameters[0] == "USER"  :   USER.decode(self, parameters)
            else: self.unknown(parameters)
        
        # If the atmel is reset, we need to reopen it again
        except serial.SerialException:
            self.ser.close()
            self.ser.open()
            self.decode_command(command)
