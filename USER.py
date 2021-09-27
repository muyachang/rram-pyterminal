import time
import math
from Lib import RRAM
from Board import PM, DAC


def clear(pyterminal):
    RRAM.read(pyterminal, 'set', 'enable', '1', True)
    RRAM.read(pyterminal, 'set', 'counter', '7', True)
    RRAM.read(pyterminal, 'toggle', '', '', True)
    RRAM.read(pyterminal, 'set', 'counter', '0', True)
    RRAM.read(pyterminal, 'toggle', '', '', True)
    RRAM.read(pyterminal, 'set', 'enable', '0', True)


def calibrate(pyterminal, low, high, tolerance, verbal):
    # Enable Calibration mode and Read mode
    RRAM.adc(pyterminal, 'set', 'cal', '1', True)
    RRAM.read(pyterminal, 'set', 'enable', '1', True)
    
    # Enable the comparators
    conf_ADC(pyterminal, '0', '0', '0x7FFF', True)
    
    # Set DAC to 'low'
    DAC.set_voltage_source(pyterminal, low, 'ADC_CAL')
    time.sleep(1)
    # Binary search for lower bound
    offset_low = 0
    offset_high = 63
    if verbal:
        print(' << Looking for the best offset >> ')
    while offset_high - offset_low > 2:
        if verbal:
            print('low: ' + str(offset_low) + '; high: ' + str(offset_high))
        offset_mid = (offset_low+offset_high)/2
        RRAM.adc(pyterminal, 'set', 'offset', str(offset_mid), True)
        RRAM.read(pyterminal, 'toggle', '', '', True)
        adc_raw = RRAM.adc(pyterminal, 'get', 'raw', '', False)[:-1]
        if verbal:
            print('adc_raw: ' + adc_raw)
        if adc_raw == '0x7FFF':
            # Set DAC to 'low' + 'tolerance'
            DAC.set_voltage_source(pyterminal, str(int(low) + int(tolerance)), 'ADC_CAL')
            time.sleep(0.25)
            RRAM.read(pyterminal, 'toggle', '', '', True)
            adc_raw = RRAM.adc(pyterminal, 'get', 'raw', '', False)[:-1]
            if verbal:
                print('adc_raw (+tole): ' + adc_raw)
            if adc_raw == '0x7FFE':
                break
            else:
                offset_low = round(offset_mid)
        elif adc_raw == '0x7FFE':
            # Set DAC to 'low' - 'tolerance'
            DAC.set_voltage_source(pyterminal, str(int(low) - int(tolerance)), 'ADC_CAL')
            time.sleep(0.25)
            RRAM.read(pyterminal, 'toggle', '', '', True)
            adc_raw = RRAM.adc(pyterminal, 'get', 'raw', '', False)[:-1]
            if verbal:
                print('adc_raw (-tole): ' + adc_raw)
            if adc_raw == '0x7FFF':
                break
            else:
                offset_high = round(offset_mid)
        else:
            offset_high = round(offset_mid)
            
    # Set DAC to 'high'
    DAC.set_voltage_source(pyterminal, high, 'ADC_CAL')
    time.sleep(1)
    # Binary search for upper bound
    step_low = 0
    step_high = 63
    if verbal:
        print(' << Looking for the best step >> ')
    while step_high - step_low > 2:
        if verbal:
            print('low: ' + str(step_low) + '; high: ' + str(step_high))
        step_mid = (step_low+step_high)/2
        RRAM.adc(pyterminal, 'set', 'step', str(step_mid), True)
        RRAM.read(pyterminal, 'toggle', '', '', True)
        adc_raw = RRAM.adc(pyterminal, 'get', 'raw', '', False)[:-1]
        if verbal:
            print('adc_raw: ' + adc_raw)
        if adc_raw == '0x0000':
            # Set DAC to 'high' - 'tolerance'
            DAC.set_voltage_source(pyterminal, str(int(high) - int(tolerance)), 'ADC_CAL')
            time.sleep(0.25)
            RRAM.read(pyterminal, 'toggle', '', '', True)
            adc_raw = RRAM.adc(pyterminal, 'get', 'raw', '', False)[:-1]
            if verbal:
                print('adc_raw (-tole): ' + adc_raw)
            if adc_raw == '0x4000':
                break
            else:
                step_high = round(step_mid)
        elif adc_raw == '0x4000':
            # Set DAC to 'high' + 'tolerance'
            DAC.set_voltage_source(pyterminal, str(int(high) + int(tolerance)), 'ADC_CAL')
            time.sleep(0.25)
            RRAM.read(pyterminal, 'toggle', '', '', True)
            adc_raw = RRAM.adc(pyterminal, 'get', 'raw', '', False)[:-1]
            if verbal:
                print('adc_raw (+tole): ' + adc_raw)
            if adc_raw == '0x0000':
                break
            else:
                step_low = round(step_mid)
        else:
            step_low = round(step_mid)
        
    offset = round((offset_high+offset_low)/2)
    step = round((step_high+step_low)/2)
    if verbal:
        print('(offset, step) = (' + str(offset) + ', ' + str(step) + ')')
    
    # Disable Calibration mode and Read mode
    RRAM.read(pyterminal, 'set', 'enable', '0', True)
    RRAM.adc(pyterminal, 'set', 'cal', '0', True)
    
    # Return the offset and the step
    return offset, step


def list_reference_voltages(pyterminal, low, high, step, verbal):
    # Enable Calibration mode and Read mode
    RRAM.adc(pyterminal, 'set', 'cal', '1', True)
    RRAM.read(pyterminal, 'set', 'enable', '1', True)
    
    # First DAC set may take longer
    DAC.set_voltage_source(pyterminal, low, 'ADC_CAL')
    time.sleep(1)
    
    reference_voltages = []
    cur_raw = '0x7FFF'
    # Sweep from 0 mV to 1000 mV
    for adc_cal in range(int(low), int(high), int(step)):
        DAC.set_voltage_source(pyterminal, str(adc_cal), 'ADC_CAL')
        time.sleep(0.25)
        RRAM.read(pyterminal, 'toggle', '', '', True)
        new_raw = RRAM.adc(pyterminal, 'get', 'raw', '', False)[:-1]
        RRAM.read(pyterminal, 'toggle', '', '', True)
        new_raw2 = RRAM.adc(pyterminal, 'get', 'raw', '', False)[:-1]
        RRAM.read(pyterminal, 'toggle', '', '', True)
        new_raw3 = RRAM.adc(pyterminal, 'get', 'raw', '', False)[:-1]
        if new_raw == new_raw2 and new_raw2 == new_raw3 and int(new_raw, 0) < int(cur_raw, 0):
            if verbal:
                print(cur_raw + ' -> ' + new_raw + ' @ ' + str(adc_cal) + ' mV', flush=True)
            cur_raw = new_raw
            reference_voltages.append(adc_cal)
            if new_raw == '0x0000':
                break
    
    # Disable Calibration mode and Read mode
    RRAM.read(pyterminal, 'set', 'enable', '0', True)
    RRAM.adc(pyterminal, 'set', 'cal', '0', True)
    
    # Return the VRefs
    return reference_voltages


def conf_write_voltages(pyterminal, AVDD_WL, AVDD_WR, verbal):
    PM.set_source(pyterminal, AVDD_WR, 'AVDD_WR')
    PM.set_source(pyterminal, AVDD_WL, 'AVDD_WL')
    time.sleep(1)


def conf_write(pyterminal, address, mode, cycle, verbal):
    RRAM.address(pyterminal, 'set', address, True)
    RRAM.write(pyterminal, 'set', 'cycle', cycle, True)
    RRAM.write(pyterminal, 'set', 'mode', mode, True)


def write(pyterminal, verbal):
    RRAM.write(pyterminal, 'set', 'enable', '1', True)
    RRAM.write(pyterminal, 'trigger', '', '', True)
    RRAM.write(pyterminal, 'set', 'enable', '0', True)


def conf_read_voltages(pyterminal, AVDD_WL, verbal):
    PM.set_source(pyterminal, AVDD_WL, 'AVDD_WL')
    time.sleep(1)


def conf_read(pyterminal, address, cycle, counter, data, verbal):
    RRAM.address(pyterminal, 'set', address, True)
    RRAM.read(pyterminal, 'set', 'cycle', cycle, True)
    RRAM.read(pyterminal, 'set', 'counter', counter, True)
    RRAM.read(pyterminal, 'set', 'data', data, True)


def read(pyterminal, verbal):
    RRAM.read(pyterminal, 'set', 'enable', '1', True)
    RRAM.read(pyterminal, 'toggle', '', '', True)
    RRAM.read(pyterminal, 'set', 'enable', '0', True)
    
    adc_raw = RRAM.adc(pyterminal, 'get', 'raw', '', False)[:-1]
    if verbal:
        print('adc_raw: ' + adc_raw)
    return adc_raw    


def conf_ADC(pyterminal, offset, step, comp, verbal):
    RRAM.adc(pyterminal, 'set', 'offset', offset, True)
    RRAM.adc(pyterminal, 'set', 'step', step, True)
    RRAM.adc(pyterminal, 'set', 'comp', comp, True)


def conf_MAC(pyterminal, mode, resolution, verbal):
    RRAM.mac(pyterminal, 'set', 'mode', mode, True)
    RRAM.mac(pyterminal, 'set', 'resolution', resolution, True)


def sweep_reference_voltages(pyterminal):
    for module in range(0, 288):
        print(f'Module: {module:3} ==> ', end='')
        # Set to the new module and clear it
        RRAM.module(pyterminal, 'set', str(module), True)
        clear(pyterminal)
        # Find the (offset, step)
        (offset, step) = calibrate(pyterminal, '50', '700', '5', False)
        # Find the VRef
        conf_ADC(pyterminal, str(offset), str(step), '0x7FFF', True)
        VRef = list_reference_voltages(pyterminal, '0', '1000', '2', False)
        # Print them out
        print(f'(Offset, Step) = ({offset:3}, {step:3}) ==> ', end='')
        print(VRef)


def sweep_on_state_cells(pyterminal):
    RRAM.module(pyterminal, 'set', '0', True)
    clear(pyterminal)
    
    # Calibrate ADC
    (offset, step) = calibrate(pyterminal, '50', '800', '5', False)
    conf_ADC(pyterminal, str(offset), str(step), '0x7FFF', True)
        
    # Form 18 cells
    conf_write_voltages(pyterminal, '1600', '3000', True)
    for address in range(0, 18):
        conf_write(pyterminal, str(address * 256), '1', '1600', True)
        write(pyterminal, True)
    
    # Set first 9 cells
    conf_write_voltages(pyterminal, '2400', '2400', True)
    for address in range(0, 9):
        conf_write(pyterminal, str(address * 256), '1', '2', True)
        write(pyterminal, True)
       
    # Rest second 9 cells
    conf_write_voltages(pyterminal, '2800', '2800', True)
    for address in range(9, 18):
        conf_write(pyterminal, str(address * 256), '0', '160', True)
        write(pyterminal, True)

    # Read 10 cells (0 On-State ~ 9 On-State)
    conf_read_voltages(pyterminal, '1700', True)
    for address in range(0, 10):
        conf_read(pyterminal, str(address * 256), '3', '0', '0x1FF', True)
        read(pyterminal, True)


def check_on_off(pyterminal, address):
    RRAM.module(pyterminal, 'set', '0', True)
    clear(pyterminal)
    
    # Calibrate ADC
    #(offset, step) = calibrate(PT, '50', '800', '5', False)
    #confADC(PT, str(offset), str(step), '0x7FFF', True)
    #conf_ADC(pyterminal, '62', '4', '0x7FFF', True)

    # Choose the right lane
    RRAM.lane(pyterminal, 'set', str(math.floor(int(address) / 32)), True)
    
    # Form 1 cells
    #conf_write_voltages(pyterminal, '1700', '3200', True)
    #conf_write(pyterminal, address, '1', '1600', True)
    #write(pyterminal, True)
    
    # Set 1 cells and read it
    conf_write_voltages(pyterminal, '1700', '1700', True)
    conf_write(pyterminal, address, '1', '2', True)
    write(pyterminal, True)
    
    conf_read_voltages(pyterminal, '1100', True)
    conf_read(pyterminal, address, '3', '0', '0x001', True)
    print('After SET  , ', end='')
    read(pyterminal, True)
        
    # Rest 1 cells and read it
    conf_write_voltages(pyterminal, '2500', '2500', True)
    conf_write(pyterminal, address, '0', '160', True)
    write(pyterminal, True)
    
    conf_read_voltages(pyterminal, '1100', True)
    conf_read(pyterminal, address, '3', '0', '0x001', True)
    print('After RESET, ', end='')
    read(pyterminal, True)


def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')


def decode(pyterminal, parameters):
    if   parameters[1] == 'clear'            : clear                   (pyterminal)
    elif parameters[1] == 'calibrate'        : calibrate               (pyterminal, parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'listVRef'         : list_reference_voltages (pyterminal, parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'confWriteVoltages': conf_write_voltages     (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'confWrite'        : conf_write              (pyterminal, parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'write'            : write                   (pyterminal, True)
    elif parameters[1] == 'confReadVoltages' : conf_read_voltages      (pyterminal, parameters[2], True)
    elif parameters[1] == 'confRead'         : conf_read               (pyterminal, parameters[2], parameters[3], parameters[4], parameters[5], True)
    elif parameters[1] == 'read'             : read                    (pyterminal, True)
    elif parameters[1] == 'confADC'          : conf_ADC                (pyterminal, parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'confMAC'          : conf_MAC                (pyterminal, parameters[2], parameters[3], True)
    elif parameters[1] == 'checkOnOff'       : check_on_off            (pyterminal, parameters[2])
    elif parameters[1] == 'func1'            : sweep_reference_voltages(pyterminal)
    elif parameters[1] == 'func2'            : sweep_on_state_cells    (pyterminal)
    else: unknown(parameters)
