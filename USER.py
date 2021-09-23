import time, math
from Lib import RRAM
from Board import PM, DAC


def clear(PT):
    RRAM.read  (PT, 'set', 'enable', '1', True)
    RRAM.read  (PT, 'set', 'counter', '7', True)
    RRAM.read  (PT, 'toggle', '', '', True)
    RRAM.read  (PT, 'set', 'counter', '0', True)
    RRAM.read  (PT, 'toggle', '', '', True)
    RRAM.read  (PT, 'set', 'enable', '0', True)

def calibrate(PT, low, high, tolerance, verbal):
    # Enable Calibration mode and Read mode
    RRAM.adc   (PT, 'set', 'cal', '1', True)
    RRAM.read  (PT, 'set', 'enable', '1', True)
    
    # Enable the comparators
    confADC(PT, '0', '0', '0x7FFF', True)
    
    # Set DAC to 'low'
    DAC.set(PT, low, 'ADC_CAL')
    time.sleep(1)
    # Binary search for lower bound
    offset_low  = 0
    offset_high = 63
    if verbal: print(' << Looking for the best offset >> ')
    while offset_high - offset_low > 2:
        if verbal: print('low: ' + str(offset_low) + '; high: ' + str(offset_high))
        offset_mid  = (offset_low+offset_high)/2
        RRAM.adc(PT, 'set', 'offset', str(offset_mid), True)
        RRAM.read  (PT, 'toggle', '', '', True)
        adc_raw = RRAM.adc(PT, 'get', 'raw', '', False)[:-1]
        if verbal: print('adc_raw: ' + adc_raw)
        if adc_raw == '0x7FFF':
            # Set DAC to 'low' + 'tolerance'
            DAC.set(PT, str(int(low) + int(tolerance)), 'ADC_CAL')
            time.sleep(0.25)
            RRAM.read  (PT, 'toggle', '', '', True)
            adc_raw = RRAM.adc(PT, 'get', 'raw', '', False)[:-1]
            if verbal: print('adc_raw (+tole): ' + adc_raw)
            if adc_raw == '0x7FFE': break
            else: offset_low = round(offset_mid)
        elif adc_raw == '0x7FFE':
            # Set DAC to 'low' - 'tolerance'
            DAC.set(PT, str(int(low) - int(tolerance)), 'ADC_CAL')
            time.sleep(0.25)
            RRAM.read  (PT, 'toggle', '', '', True)
            adc_raw = RRAM.adc(PT, 'get', 'raw', '', False)[:-1]
            if verbal: print('adc_raw (-tole): ' + adc_raw)
            if adc_raw == '0x7FFF': break
            else: offset_high = round(offset_mid)
        else:
            offset_high = round(offset_mid)
            
    # Set DAC to 'high'
    DAC.set(PT, high, 'ADC_CAL')
    time.sleep(1)
    # Binary search for upper bound
    step_low  = 0
    step_high = 63
    if verbal: print(' << Looking for the best step >> ')
    while step_high - step_low > 2:
        if verbal: print('low: ' + str(step_low) + '; high: ' + str(step_high))
        step_mid  = (step_low+step_high)/2
        RRAM.adc(PT, 'set', 'step', str(step_mid), True)
        RRAM.read  (PT, 'toggle', '', '', True)
        adc_raw = RRAM.adc(PT, 'get', 'raw', '', False)[:-1]
        if verbal: print('adc_raw: ' + adc_raw)
        if adc_raw == '0x0000':
            # Set DAC to 'high' - 'tolerance'
            DAC.set(PT, str(int(high) - int(tolerance)), 'ADC_CAL')
            time.sleep(0.25)
            RRAM.read  (PT, 'toggle', '', '', True)
            adc_raw = RRAM.adc(PT, 'get', 'raw', '', False)[:-1]
            if verbal: print('adc_raw (-tole): ' + adc_raw)
            if adc_raw == '0x4000': break
            else: step_high = round(step_mid)
        elif adc_raw == '0x4000':
            # Set DAC to 'high' + 'tolerance'
            DAC.set(PT, str(int(high) + int(tolerance)), 'ADC_CAL')
            time.sleep(0.25)
            RRAM.read  (PT, 'toggle', '', '', True)
            adc_raw = RRAM.adc(PT, 'get', 'raw', '', False)[:-1]
            if verbal: print('adc_raw (+tole): ' + adc_raw)
            if adc_raw == '0x0000': break
            else: step_low = round(step_mid)
        else:
            step_low = round(step_mid)
        
    offset = round((offset_high+offset_low)/2)
    step = round((step_high+step_low)/2)
    if verbal: print('(offset, step) = (' + str(offset) + ', ' + str(step) + ')')
    
    # Disable Calibration mode and Read mode
    RRAM.read  (PT, 'set', 'enable', '0', True)
    RRAM.adc   (PT, 'set', 'cal', '0', True)    
    
    # Return the offset and the step
    return (offset, step)
        
def listVRef(PT, low, high, step, verbal):
    # Enable Calibration mode and Read mode
    RRAM.adc   (PT, 'set', 'cal', '1', True)
    RRAM.read  (PT, 'set', 'enable', '1', True)
    
    # Fisrt DAC set may take longer
    DAC.set(PT, low, 'ADC_CAL')
    time.sleep(1)
    
    VRef = []
    curRaw = '0x7FFF'
    newRaw = ''
    # Sweep from 0 mV to 1000 mV
    for adc_cal in range(int(low), int(high), int(step)):
        DAC.set(PT, str(adc_cal), 'ADC_CAL')
        time.sleep(0.25)
        RRAM.read  (PT, 'toggle', '', '', True)
        newRaw  = RRAM.adc(PT, 'get', 'raw', '', False)[:-1]
        RRAM.read  (PT, 'toggle', '', '', True)
        newRaw2 = RRAM.adc(PT, 'get', 'raw', '', False)[:-1]
        RRAM.read  (PT, 'toggle', '', '', True)
        newRaw3 = RRAM.adc(PT, 'get', 'raw', '', False)[:-1]
        if newRaw == newRaw2 and newRaw2 == newRaw3 and int(newRaw,0) < int(curRaw,0):
            if verbal: print(curRaw + ' -> ' + newRaw + ' @ ' + str(adc_cal) + ' mV', flush = True)
            curRaw = newRaw
            VRef.append(adc_cal)
            if newRaw == '0x0000':
                break;
    
    # Disable Calibration mode and Read mode
    RRAM.read  (PT, 'set', 'enable', '0', True)
    RRAM.adc   (PT, 'set', 'cal', '0', True)
    
    # Return the VRefs
    return VRef
    
def confWriteVoltages(PT, AVDD_WL, AVDD_WR, verbal):
    PM.set(PT, AVDD_WR, 'AVDD_WR')
    PM.set(PT, AVDD_WL, 'AVDD_WL')
    time.sleep(1)
    
def confWrite(PT, address, mode, cycle, verbal):
    RRAM.address(PT, 'set', address, True)
    RRAM.write(PT, 'set', 'cycle', cycle, True)
    RRAM.write(PT, 'set', 'mode', mode, True)
    
def write(PT, verbal):
    RRAM.write(PT, 'set', 'enable', '1', True)
    RRAM.write(PT, 'trigger', '', '', True)
    RRAM.write(PT, 'set', 'enable', '0', True)

def confReadVoltages(PT, AVDD_WL, verbal):
    PM.set(PT, AVDD_WL, 'AVDD_WL')
    time.sleep(1)
    
def confRead(PT, address, cycle, counter, data, verbal):
    RRAM.address(PT, 'set', address, True)
    RRAM.read(PT, 'set', 'cycle', cycle, True)
    RRAM.read(PT, 'set', 'counter', counter, True)
    RRAM.read(PT, 'set', 'data', data, True)
    
def read(PT, verbal):
    RRAM.read(PT, 'set', 'enable', '1', True)
    RRAM.read(PT, 'toggle', '', '', True)
    RRAM.read(PT, 'set', 'enable', '0', True)
    
    adc_raw = RRAM.adc(PT, 'get', 'raw', '', False)[:-1]
    if verbal: print('adc_raw: ' + adc_raw)
    return adc_raw    

def confADC(PT, offset, step, comp, verbal):
    RRAM.adc(PT, 'set', 'offset', offset, True)
    RRAM.adc(PT, 'set', 'step', step, True)
    RRAM.adc(PT, 'set', 'comp', comp, True)
    
def confMAC(PT, mode, resolution, verbal):
    RRAM.mac   (PT, 'set', 'mode', mode, True)
    RRAM.mac   (PT, 'set', 'resolution', resolution, True)
    
def sweepVRef(PT):
    for module in range(0, 288):
        print(f'Module: {module:3} ==> ', end = '')
        # Set to the new module and clear it
        RRAM.module(PT, 'set', str(module), True)
        clear(PT)
        # Find the (offset, step)
        (offset, step) = calibrate(PT, '50', '700', '5', False)
        # Find the VRef
        confADC(PT, str(offset), str(step), '0x7FFF', True)
        VRef = listVRef(PT, '0', '1000', '2', False)
        # Print them out
        print(f'(Offset, Step) = ({offset:3}, {step:3}) ==> ', end ='')
        print(VRef)

def sweepOnStateCells(PT):
    RRAM.module(PT, 'set', '0', True)
    clear(PT)
    
    # Calibrate ADC
    (offset, step) = calibrate(PT, '50', '800', '5', False)
    confADC(PT, str(offset), str(step), '0x7FFF', True)
        
    # Form 18 cells
    confWriteVoltages(PT, '1600', '3000', True)
    for address in range(0, 18):
        confWrite(PT, str(address*256), '1', '1600', True)
        write(PT, True)
    
    # Set first 9 cells
    confWriteVoltages(PT, '2400', '2400', True)
    for address in range(0, 9):
        confWrite(PT, str(address*256), '1', '2', True)
        write(PT, True)
       
    # Rest second 9 cells
    confWriteVoltages(PT, '2800', '2800', True)
    for address in range(9, 18):
        confWrite(PT, str(address*256), '0', '160', True)
        write(PT, True)

    # Read 10 cells (0 On-State ~ 9 On-State)
    confReadVoltages(PT, '1700', True)
    for address in range(0, 10):
        confRead(PT, str(address*256), '3', '0', '0x1FF', True)
        read(PT, True)

def checkOnOff(PT, address):
    RRAM.module(PT, 'set', '0', True)
    clear(PT)
    
    ## Calibrate ADC
    #(offset, step) = calibrate(PT, '50', '800', '5', False)
    #confADC(PT, str(offset), str(step), '0x7FFF', True)
    confADC(PT, '62', '4', '0x7FFF', True)

    # Choose the right lane
    RRAM.lane(PT, 'set', str(math.floor(int(address) / 32)), True)
    
    ## Form 1 cells
    #confWriteVoltages(PT, '1700', '3200', True)
    #confWrite(PT, address, '1', '1600', True)
    #write(PT, True)
    
    # Set 1 cells and read it
    confWriteVoltages(PT, '1700', '1700', True)
    confWrite(PT, address, '1', '2', True)
    write(PT, True)
    
    confReadVoltages(PT, '1100', True)
    confRead(PT, address, '3', '0', '0x001', True)
    read(PT, True)
        
    # Rest 1 cells and read it
    confWriteVoltages(PT, '2500', '2500', True)
    confWrite(PT, address, '0', '160', True)
    write(PT, True)
    
    confReadVoltages(PT, '1100', True)
    confRead(PT, address, '3', '0', '0x001', True)
    read(PT, True)
    
def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')
          
def decode(PT, parameters):
    if   parameters[1] == 'clear'            : clear            (PT)
    elif parameters[1] == 'calibrate'        : calibrate        (PT, parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'listVRef'         : listVRef         (PT, parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'confWriteVoltages': confWriteVoltages(PT, parameters[2], parameters[3], True)
    elif parameters[1] == 'confWrite'        : confWrite        (PT, parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'write'            : write            (PT, True)
    elif parameters[1] == 'confReadVoltages' : confReadVoltages (PT, parameters[2], True)
    elif parameters[1] == 'confRead'         : confRead         (PT, parameters[2], parameters[3], parameters[4], parameters[5], True)
    elif parameters[1] == 'read'             : read             (PT, True)
    elif parameters[1] == 'confADC'          : confADC          (PT, parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'confMAC'          : confMAC          (PT, parameters[2], parameters[3], True)
    elif parameters[1] == 'checkOnOff'       : checkOnOff       (PT, parameters[2])
    elif parameters[1] == 'func1'            : sweepVRef        (PT)
    elif parameters[1] == 'func2'            : sweepOnStateCells(PT)
    else                             : unknown(parameters)