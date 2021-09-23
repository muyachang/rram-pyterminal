import CommandMap as CM

def id(PT, verbal):
    return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_PID, False)
    
def status(PT, verbal):
    return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_STATUS, verbal)

def lane(PT, action, target, verbal):
    if   action == 'set':        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_LANE + ' ' + CM.CM_RRAM_SET + ' ' + target, verbal)
    elif action == 'get': return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_LANE + ' ' + CM.CM_RRAM_GET               , verbal)
    else                : unknown(['RRAM', 'lane', action, target])
        
def group(PT, action, target, verbal):
    if   action == 'set':        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_GROUP + ' ' + CM.CM_RRAM_SET + ' ' + target, verbal)
    elif action == 'get': return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_GROUP + ' ' + CM.CM_RRAM_GET               , verbal)
    else                : unknown(['RRAM', 'group', action, target])
        
def module(PT, action, target, verbal):
    if   action == 'set':        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_MODULE + ' ' + CM.CM_RRAM_SET + ' ' + target, verbal)
    elif action == 'get': return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_MODULE + ' ' + CM.CM_RRAM_GET               , verbal)
    else                : unknown(['RRAM', 'module', action, target])
        
def mask(PT, action, target, verbal):
    if   action == 'set':        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_MASK + ' ' + CM.CM_RRAM_SET + ' ' + target, verbal)
    elif action == 'get': return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_MASK + ' ' + CM.CM_RRAM_GET               , verbal)
    else                : unknown(['RRAM', 'mask', action, target])
        
def address(PT, action, target, verbal):
    if   action == 'set':        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADDRESS + ' ' + CM.CM_RRAM_SET + ' ' + target, verbal)
    elif action == 'get': return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADDRESS + ' ' + CM.CM_RRAM_GET               , verbal)
    else                : unknown(['RRAM', 'address', action, target])
        
def read(PT, action, type, target, verbal):
    if action == 'set':
        if   type == 'enable' :        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_READ_ENABLE  + ' ' + target, verbal)
        elif type == 'cycle'  :        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_READ_CYCLE   + ' ' + target, verbal)
        elif type == 'source' :        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_READ_SOURCE  + ' ' + target, verbal)
        elif type == 'counter':        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_READ_COUNTER + ' ' + target, verbal)
        elif type == 'data'   :        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_READ_DATA    + ' ' + target, verbal)
        else                  : unknown(['RRAM', 'read', action, type, target])
    elif action == 'get':
        if   type == 'enable' : return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_READ_ENABLE                , verbal)
        elif type == 'status' : return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_READ_STATUS                , verbal)
        elif type == 'cycle'  : return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_READ_CYCLE                 , verbal)
        elif type == 'source' : return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_READ_SOURCE                , verbal)
        elif type == 'counter': return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_READ_COUNTER               , verbal)
        elif type == 'data'   : return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_READ_DATA                  , verbal)
        else                  : unknown(['RRAM', 'read', action, type, target])
    elif action == 'toggle':
        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_TOGGLE, verbal)
    else: unknown(['RRAM', 'read', action, type, target])

def mac(PT, action, type, target, verbal):
    if action == 'set':
        if   type == 'mode'      :        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_MAC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_MAC_MODE       + ' ' + target, verbal)
        elif type == 'resolution':        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_MAC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_MAC_RESOLUTION + ' ' + target, verbal)
        else                     : unknown(['RRAM', 'mac', action, type, target])
    elif action == 'get':
        if   type == 'status'    : return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_MAC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_MAC_STATUS                   , verbal)
        elif type == 'mode'      : return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_MAC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_MAC_MODE                     , verbal)
        elif type == 'resolution': return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_MAC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_MAC_RESOLUTION               , verbal)
        elif type == 'result'    : return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_MAC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_MAC_RESULT                   , verbal)
        else                     : unknown(['RRAM', 'mac', action, type, target])
    else: unknown(['RRAM', 'mac', action, type, target])

def write(PT, action, type, target, verbal):
    if action == 'set':
        if   type == 'enable':        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_WRITE_ENABLE  + ' ' + target, verbal)
        elif type == 'cycle' :        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_WRITE_CYCLE   + ' ' + target, verbal)
        elif type == 'mode'  :        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_WRITE_MODE    + ' ' + target, verbal)
        else                 : unknown(['RRAM', 'write', action, type, target])
    elif action == 'get':
        if   type == 'enable': return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_WRITE_ENABLE                , verbal)
        elif type == 'status': return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_WRITE_STATUS                , verbal)
        elif type == 'cycle' : return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_WRITE_CYCLE                 , verbal)
        elif type == 'mode'  : return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_WRITE_MODE                  , verbal)
        else                 : unknown(['RRAM', 'write', action, type, target])
    elif action == 'trigger':
        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_TRIGGER, verbal)
    else: unknown(['RRAM', 'write', action, type, target])

def adc(PT, action, type, target, verbal):
    if action == 'set':
        if   type == 'step'  :        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_ADC_STEP    + ' ' + target, verbal)
        elif type == 'offset':        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_ADC_OFFSET  + ' ' + target, verbal)
        elif type == 'comp'  :        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_ADC_COMP    + ' ' + target, verbal)
        elif type == 'hbias' :        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_ADC_HBIAS   + ' ' + target, verbal)
        elif type == 'cal'   :        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_ADC_CAL     + ' ' + target, verbal)
        else                 : unknown(['RRAM', 'adc', action, type, target])
    elif action == 'get':
        if   type == 'raw'   : return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ADC_RAW                   , verbal)
        elif type == 'step'  : return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ADC_STEP                  , verbal)
        elif type == 'offset': return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ADC_OFFSET                , verbal)
        elif type == 'comp'  : return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ADC_COMP                  , verbal)
        elif type == 'hbias' : return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ADC_HBIAS                 , verbal)
        elif type == 'cal'   : return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ADC_CAL                   , verbal)
        else                 : unknown(['RRAM', 'adc', action, type, target])
    else: unknown(['RRAM', 'adc', action, type, target])

def pg(PT, action, type, target, verbal):
    if action == 'set':
        if   type == 'disable':        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_PG + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_PG_DISABLE + ' ' + target, verbal)
        else                  : unknown(['RRAM', 'pg', action, type, target])
    elif action == 'get':
        if   type == 'disable': return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_PG + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_PG_DISABLE               , verbal)
        else                  : unknown(['RRAM', 'pg', action, type, target])
    else: unknown(['RRAM', 'pg', action, type, target])

def ecc(PT, action, type, target, verbal):
    if action == 'set':
        if   type == 'enable':        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_ECC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_ECC_ENABLE + ' ' + target, verbal)
        else                 : unknown(['RRAM', 'ecc', action, type, target])
    elif action == 'get':
        if   type == 'enable': return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_ECC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ECC_ENABLE               , verbal)
        else                 : unknown(['RRAM', 'ecc', action, type, target])
    elif action == 'clear':
        PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_ECC + ' ' + CM.CM_RRAM_CLEAR, verbal)
    elif action == 'check':
        return PT.sendCommand(CM.CM_RRAM + ' ' + CM.CM_RRAM_ECC + ' ' + CM.CM_RRAM_CHECK, verbal)
    else: unknown(['RRAM', 'ecc', action, type, target])

def unknown(parameters):
    print('Unknown Command: ' + ' '.join(parameters) + '(From PyTerminal)')
          
def decode(PT, parameters):
    if   parameters[1] == 'id'     : id     (PT, True)
    elif parameters[1] == 'status' : status (PT, True)
    elif parameters[1] == 'lane'   : lane   (PT, parameters[2], parameters[3], True)
    elif parameters[1] == 'group'  : group  (PT, parameters[2], parameters[3], True)
    elif parameters[1] == 'module' : module (PT, parameters[2], parameters[3], True)
    elif parameters[1] == 'mask'   : mask   (PT, parameters[2], parameters[3], True)
    elif parameters[1] == 'address': address(PT, parameters[2], parameters[3], True)
    elif parameters[1] == 'read'   : read   (PT, parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'mac'    : mac    (PT, parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'write'  : write  (PT, parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'adc'    : adc    (PT, parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'pg'     : pg     (PT, parameters[2], parameters[3], parameters[4], True)
    elif parameters[1] == 'ecc'    : ecc    (PT, parameters[2], parameters[3], parameters[4], True)
    else                           : unknown(parameters)