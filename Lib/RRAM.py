import CommandMap as CM
import PyTerminal as PT


def id (verbal):
    """ **[Low Level]** Get the ID of the RRAM Modules

    Args:
        verbal (bool): Whether to print the response or not.
    Returns:
        The ID of the RRAM Modules.

    """
    return PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_PID, verbal)


def lane(action, target, verbal):
    """ **[Low Level]** Set/Get the selected ADC lane

    Args:
        action (str): Could be *set* or *get*
        target (str): Target lane number, from *0*~*7*
        verbal (bool): Whether to print the response or not.
    Returns:
        The selected lane.
    """
    if   action == 'set':            PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_LANE + ' ' + CM.CM_RRAM_SET + ' ' + target, verbal)
    elif action == 'get': return int(PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_LANE + ' ' + CM.CM_RRAM_GET, verbal))
    else: PT.unknown(['RRAM', 'lane', action, target])


def group(action, target, verbal):
    """ **[Low Level]** Set/Get the selected group for the Vector module

    Args:
        action (str): Could be *set* or *get*
        target (str): Target group number, from *0*~*35*
        verbal (bool): Whether to print the response or not.
    Returns:
        The selected group.
    """
    if   action == 'set':            PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_GROUP + ' ' + CM.CM_RRAM_SET + ' ' + target, verbal)
    elif action == 'get': return int(PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_GROUP + ' ' + CM.CM_RRAM_GET, verbal))
    else: PT.unknown(['RRAM', 'group', action, target])


def module(action, target, verbal):
    """ **[Low Level]** Set/Get the selected RRAM module

    Args:
        action (str): Could be *set* or *get*
        target (str): Target RRAM module number, from *0*~*287*
        verbal (bool): Whether to print the response or not.
    Returns:
        The selected module.
    """
    if   action == 'set':            PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MODULE + ' ' + CM.CM_RRAM_SET + ' ' + target, verbal)
    elif action == 'get': return int(PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MODULE + ' ' + CM.CM_RRAM_GET, verbal))
    else: PT.unknown(['RRAM', 'module', action, target])


def mask(action, target, verbal):
    """ **[Low Level]** Set/Get the RRAM module selection mask register

    Args:
        action (str): Could be *set* or *get*
        target (str): Target RRAM module selection mask, from *0x00000001*~*0xFFFFFFFF*
        verbal (bool): Whether to print the response or not.
    Returns:
        The current mask.
    """
    if   action == 'set':        PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MASK + ' ' + CM.CM_RRAM_SET + ' ' + target, verbal)
    elif action == 'get': return PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MASK + ' ' + CM.CM_RRAM_GET, verbal)
    else: PT.unknown(['RRAM', 'mask', action, target])


def address(action, target, verbal):
    """ **[Low Level]** Set/Get the RRAM module address register

    Args:
        action (str): Could be *set* or *get*
        target (str): Target address, from *0*~*65535*
        verbal (bool): Whether to print the response or not.
    Returns:
        The current address.
    """
    if   action == 'set':            PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADDRESS + ' ' + CM.CM_RRAM_SET + ' ' + target, verbal)
    elif action == 'get': return int(PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADDRESS + ' ' + CM.CM_RRAM_GET, verbal))
    else: PT.unknown(['RRAM', 'address', action, target])


def read(action, action_type, target, verbal):
    """ **[Low Level]** Configure read related settings

    Args:
        action (str): Could be *set* or *get*
        action_type (str): Could be *status*, *enable*, *cycle*, *source*, *counter*, *data*
        target (str): Target number, *0*~*1* for *enable* *source*, *0*~*255* for *cycle*, and *0x1*~*0x1FF* for *data*
        verbal (bool): Whether to print the response or not.
    Returns:
        The current value of *action_type*.
    """
    if action == 'set':
        if   action_type == 'enable' :        PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_READ_ENABLE  + ' ' + target, verbal)
        elif action_type == 'cycle'  :        PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_READ_CYCLE   + ' ' + target, verbal)
        elif action_type == 'source' :        PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_READ_SOURCE  + ' ' + target, verbal)
        elif action_type == 'counter':        PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_READ_COUNTER + ' ' + target, verbal)
        elif action_type == 'data'   :        PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_READ_DATA    + ' ' + target, verbal)
        else: PT.unknown(['RRAM', 'read', action, action_type, target])
    elif action == 'get':
        if   action_type == 'enable' : return int(PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_READ_ENABLE , verbal))
        elif action_type == 'status' : return int(PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_READ_STATUS , verbal))
        elif action_type == 'cycle'  : return int(PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_READ_CYCLE  , verbal))
        elif action_type == 'source' : return int(PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_READ_SOURCE , verbal))
        elif action_type == 'counter': return int(PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_READ_COUNTER, verbal))
        elif action_type == 'data'   : return     PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_READ_DATA   , verbal)
        else: PT.unknown(['RRAM', 'read', action, action_type, target])
    elif action == 'toggle':
        PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_READ + ' ' + CM.CM_RRAM_TOGGLE, verbal)
    else: PT.unknown(['RRAM', 'read', action, action_type, target])


def mac(action, action_type, target, verbal):
    """ **[Low Level]** Configure mac related settings

    Args:
        action (str): Could be *set* or *get*
        action_type (str): Could be *status*, *result*, *mode*, *resolution*
        target (str): Target number, *0*~*1* for *mode*, *0*~*3* for *resolution*
        verbal (bool): Whether to print the response or not.
    Returns:
        The current value of *action_type*.
    """
    if action == 'set':
        if   action_type == 'mode'      :            PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MAC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_MAC_MODE       + ' ' + target, verbal)
        elif action_type == 'resolution':            PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MAC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_MAC_RESOLUTION + ' ' + target, verbal)
        else: PT.unknown(['RRAM', 'mac', action, action_type, target])
    elif action == 'get':
        if   action_type == 'status'    : return int(PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MAC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_MAC_STATUS    , verbal))
        elif action_type == 'mode'      : return int(PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MAC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_MAC_MODE      , verbal))
        elif action_type == 'resolution': return int(PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MAC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_MAC_RESOLUTION, verbal))
        elif action_type == 'result'    : return int(PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_MAC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_MAC_RESULT    , verbal))
        else: PT.unknown(['RRAM', 'mac', action, action_type, target])
    else: PT.unknown(['RRAM', 'mac', action, action_type, target])


def write(action, action_type, target, verbal):
    """ **[Low Level]** Configure read related settings

    Args:
        action (str): Could be *set* or *get*
        action_type (str): Could be *status*, *enable*, *cycle*, *mode*
        target (str): Target number, *0*~*1* for *enable* *mode*, *0*~*65535* for *cycle*
        verbal (bool): Whether to print the response or not.
    Returns:
        The current value of *action_type*.
    """
    if action == 'set':
        if   action_type == 'enable':            PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_WRITE_ENABLE + ' ' + target, verbal)
        elif action_type == 'cycle' :            PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_WRITE_CYCLE  + ' ' + target, verbal)
        elif action_type == 'mode'  :            PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_WRITE_MODE   + ' ' + target, verbal)
        else: PT.unknown(['RRAM', 'write', action, action_type, target])
    elif action == 'get':
        if   action_type == 'enable': return int(PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_WRITE_ENABLE, verbal))
        elif action_type == 'status': return int(PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_WRITE_STATUS, verbal))
        elif action_type == 'cycle' : return int(PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_WRITE_CYCLE , verbal))
        elif action_type == 'mode'  : return int(PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_WRITE_MODE  , verbal))
        else: PT.unknown(['RRAM', 'write', action, action_type, target])
    elif action == 'trigger':
        PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_WRITE + ' ' + CM.CM_RRAM_TRIGGER, verbal)
    else: PT.unknown(['RRAM', 'write', action, action_type, target])


def adc(action, action_type, target, verbal):
    """ **[Low Level]** Configure ADC related settings

    Args:
        action (str): Could be *set* or *get*
        action_type (str): Could be *raw*, *step*, *offset*, *comp*, *hbias*, *cal*
        target (str): Target number, *0*~*1* for *hbias* *cal*, *0*~*63* for *step* *offset*, *0x0000*~*0x7FFF* for *comp*
        verbal (bool): Whether to print the response or not.
    Returns:
        The current value of *action_type*.
    """
    if action == 'set':
        if   action_type == 'step'  :            PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_ADC_STEP   + ' ' + target, verbal)
        elif action_type == 'offset':            PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_ADC_OFFSET + ' ' + target, verbal)
        elif action_type == 'comp'  :            PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_ADC_COMP   + ' ' + target, verbal)
        elif action_type == 'hbias' :            PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_ADC_HBIAS  + ' ' + target, verbal)
        elif action_type == 'cal'   :            PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_ADC_CAL    + ' ' + target, verbal)
        else: PT.unknown(['RRAM', 'adc', action, action_type, target])
    elif action == 'get':
        if   action_type == 'raw'   : return     PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ADC_RAW   , verbal)
        elif action_type == 'step'  : return int(PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ADC_STEP  , verbal))
        elif action_type == 'offset': return int(PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ADC_OFFSET, verbal))
        elif action_type == 'comp'  : return     PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ADC_COMP  , verbal)
        elif action_type == 'hbias' : return int(PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ADC_HBIAS , verbal))
        elif action_type == 'cal'   : return int(PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ADC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ADC_CAL   , verbal))
        else:
            PT.unknown(['RRAM', 'adc', action, action_type, target])
    else: PT.unknown(['RRAM', 'adc', action, action_type, target])


def pg(action, action_type, target, verbal):
    """ **[Low Level]** Configure power gating related settings

    Args:
        action (str): Could be *set* or *get*
        action_type (str): Could be *disable*
        target (str): Target number, *0*~*1* for *disable*
        verbal (bool): Whether to print the response or not.
    Returns:
        The current value of *action_type*.
    """
    if action == 'set':
        if   action_type == 'disable':            PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_PG + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_PG_DISABLE + ' ' + target, verbal)
        else:
            PT.unknown(['RRAM', 'pg', action, action_type, target])
    elif action == 'get':
        if   action_type == 'disable': return int(PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_PG + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_PG_DISABLE, verbal))
        else:
            PT.unknown(['RRAM', 'pg', action, action_type, target])
    else: PT.unknown(['RRAM', 'pg', action, action_type, target])


def ecc(action, action_type, target, verbal):
    """ **[Low Level]** Configure power gating related settings

    Args:
        action (str): Could be *set*, *get*, *clear*, or *check*
        action_type (str): Could be *enable*
        target (str): Target number, *0*~*1* for *enable*
        verbal (bool): Whether to print the response or not.
    Returns:
        The current value of *action_type*.
    """
    if action == 'set':
        if   action_type == 'enable':            PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ECC + ' ' + CM.CM_RRAM_SET + ' ' + CM.CM_RRAM_ECC_ENABLE + ' ' + target, verbal)
        else:
            PT.unknown(['RRAM', 'ecc', action, action_type, target])
    elif action == 'get':
        if   action_type == 'enable': return int(PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ECC + ' ' + CM.CM_RRAM_GET + ' ' + CM.CM_RRAM_ECC_ENABLE, verbal))
        else:
            PT.unknown(['RRAM', 'ecc', action, action_type, target])
    elif action == 'clear':
               PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ECC + ' ' + CM.CM_RRAM_CLEAR, verbal)
    elif action == 'check':
        return PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_ECC + ' ' + CM.CM_RRAM_CHECK, verbal)
    else: PT.unknown(['RRAM', 'ecc', action, action_type, target])


def reg_status(verbal):
    """ **[High Level]** Print the register status of the RRAM accelerator

    Args:
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_REG_STATUS, verbal)


def env_init(verbal):
    """ **[High Level]** Initialize the environment configurations of the RRAM accelerator and the currently selected RRAM modules

    Args:
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_ENV_INIT, verbal)


def env_status(verbal):
    """ **[High Level]** Print the environment configurations of the RRAM accelerator and the currently selected RRAM modules

    Args:
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_ENV_STATUS, verbal)


def mod_init(verbal):
    """ **[High Level]** Initialize the module floorplan status

    Args:
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_MOD_INIT, verbal)


def mod_status(verbal):
    """ **[High Level]** Print the module floorplan status

    Args:
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_MOD_STATUS, verbal)


def mod_conf(status, verbal):
    """ **[High Level]** Configure the current module floorplan status

    Args:
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_MOD_CONF + ' ' + status, verbal)


def switch(index, verbal):
    """ **[High Level]** Switch to module *index* and configure related things. (ex. ADC, VTGT_BL ... etc)

    Args:
        index (str): Target RRAM Module, from *0* ~ *287*
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_SWITCH + ' ' + index, verbal)


def conf_form(AVDD_WR, AVDD_WL, cycle, times, verbal):
    """ **[High Level]** Configure FORM operation

    Args:
        AVDD_WR (str): AVDD_WR voltage for FORM
        AVDD_WL (str): AVDD_WL voltage for FORM
        cycle (str): number of clock cycles per pulse for FORM
        times (str): number of pulses for FORM
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CONF_FORM + ' ' + AVDD_WR + ' ' + AVDD_WL + ' ' + cycle + ' ' + times, verbal)


def form(level, number, verbal):
    """ **[High Level]** FORM the cells

    Args:
        level (str): Hierarchy level, could be *cell*, *row*, *col*, *module*
        number (str): Target number, could be *0*~*65535* for *cell*, *0*~*255* for *row* and *col*, *0* for *module*
        verbal (bool): Whether to print the response or not.
    """
    if level == 'cell':
        PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_FORM + ' ' + CM.CM_RRAM_API_LEVEL_CELL + ' ' + number, verbal)
    elif level == 'row':
        PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_FORM + ' ' + CM.CM_RRAM_API_LEVEL_ROW + ' ' + number, verbal)
    elif level == 'col':
        PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_FORM + ' ' + CM.CM_RRAM_API_LEVEL_COL + ' ' + number, verbal)
    elif level == 'module':
        PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_FORM + ' ' + CM.CM_RRAM_API_LEVEL_MODULE + ' ' + number, verbal)


def conf_set(AVDD_WR, AVDD_WL, cycle, times, verbal):
    """ **[High Level]** Configure SET operation

    Args:
        AVDD_WR (str): AVDD_WR voltage for SET
        AVDD_WL (str): AVDD_WL voltage for SET
        cycle (str): number of clock cycles per pulse for SET
        times (str): number of pulses for SET
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CONF_SET + ' ' + AVDD_WR + ' ' + AVDD_WL + ' ' + cycle + ' ' + times, verbal)


def set(level, number, verbal):
    """ **[High Level]** SET the cells

    Args:
        level (str): Hierarchy level, could be *cell*, *row*, *col*, *module*
        number (str): Target number, could be *0*~*65535* for *cell*, *0*~*255* for *row* and *col*, *0* for *module*
        verbal (bool): Whether to print the response or not.
    """
    if level == 'cell':
        PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_SET + ' ' + CM.CM_RRAM_API_LEVEL_CELL + ' ' + number, verbal)
    elif level == 'row':
        PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_SET + ' ' + CM.CM_RRAM_API_LEVEL_ROW + ' ' + number, verbal)
    elif level == 'col':
        PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_SET + ' ' + CM.CM_RRAM_API_LEVEL_COL + ' ' + number, verbal)
    elif level == 'module':
        PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_SET + ' ' + CM.CM_RRAM_API_LEVEL_MODULE + ' ' + number, verbal)


def conf_reset(AVDD_WR, AVDD_WL, cycle, times, verbal):
    """ **[High Level]** Configure RESET operation

    Args:
        AVDD_WR (str): AVDD_WR voltage for RESET
        AVDD_WL (str): AVDD_WL voltage for RESET
        cycle (str): number of clock cycles per pulse for RESET
        times (str): number of pulses for RESET
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CONF_RESET + ' ' + AVDD_WR + ' ' + AVDD_WL + ' ' + cycle + ' ' + times, verbal)


def reset(level, number, verbal):
    """ **[High Level]** RESET the cells

    Args:
        level (str): Hierarchy level, could be *cell*, *row*, *col*, *module*
        number (str): Target number, could be *0*~*65535* for *cell*, *0*~*255* for *row* and *col*, *0* for *module*
        verbal (bool): Whether to print the response or not.
    """
    if level == 'cell':
        PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_RESET + ' ' + CM.CM_RRAM_API_LEVEL_CELL + ' ' + number, verbal)
    elif level == 'row':
        PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_RESET + ' ' + CM.CM_RRAM_API_LEVEL_ROW + ' ' + number, verbal)
    elif level == 'col':
        PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_RESET + ' ' + CM.CM_RRAM_API_LEVEL_COL + ' ' + number, verbal)
    elif level == 'module':
        PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_RESET + ' ' + CM.CM_RRAM_API_LEVEL_MODULE + ' ' + number, verbal)


def set_reset(level, number, times, verbal):
    """ **[High Level]** SET and RESET the cells

    Args:
        level (str): Hierarchy level, could be *cell*, *row*, *col*, *module*
        number (str): Target number, could be *0*~*65535* for *cell*, *0*~*255* for *row* and *col*, *0* for *module*
        times (str): How many loops per set&reset
        verbal (bool): Whether to print the response or not.
    """
    if level == 'cell':
        PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_SET_RESET + ' ' + CM.CM_RRAM_API_LEVEL_CELL + ' ' + number + ' ' + times, verbal)
    elif level == 'row':
        PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_SET_RESET + ' ' + CM.CM_RRAM_API_LEVEL_ROW + ' ' + number + ' ' + times, verbal)
    elif level == 'col':
        PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_SET_RESET + ' ' + CM.CM_RRAM_API_LEVEL_COL + ' ' + number + ' ' + times, verbal)
    elif level == 'module':
        PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_SET_RESET + ' ' + CM.CM_RRAM_API_LEVEL_MODULE + ' ' + number + ' ' + times, verbal)


def write_byte(address, value, verbal):
    """ **[High Level]** Write *value* to *address*

    Args:
        address (str): Address to be written to
        value (str): Value to be written to
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_WRITE_BYTE + ' ' + address + ' ' + value, verbal)


def write_byte_iter(address, value, verbal):
    """ **[High Level]** Write *value* to *address* iteratively, this function is more robust than `write_byte` but takes longer

    Args:
        address (str): Address to be written to
        value (str): Value to be written to
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_WRITE_BYTE_ITER + ' ' + address + ' ' + value, verbal)


def conf_read(cycle, verbal):
    """ **[High Level]** Configure READ operation

    Args:
        cycle (str): Number of clock cycles per pulse for READ
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CONF_READ + ' ' + cycle, verbal)


def read_lane(address, data, verbal):
    """ **[High Level]** Read the *address* cell with *data* fed to the WLs

    Args:
        address (str): Address to be read from
        data (str): Value to be fed to the WLs
        verbal (bool): Whether to print the response or not.
    Returns:
        The readout value of one lane.
    """
    return PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_READ_LANE + ' ' + address + ' ' + data, verbal)


def read_byte(address, counter, data, verbal):
    """ **[High Level]** Read the whole byte from *address* with *data* fed to the WLs and *counter* for the MAC unit

    Args:
        address (str): Address to be read from
        counter (str): so the MAC unit knows which bit the *data* is currently at
        data (str): Value to be fed to the WLs
        verbal (bool): Whether to print the response or not.
    Returns:
        The readout value of one byte (8 lanes).
    """
    return PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_READ_BYTE + ' ' + address + ' ' + counter + ' ' + data, verbal)


def conf_ADC(offset, step, comp, verbal):
    """ **[High Level]** Configure ADC settings

    Args:
        offset (str): ADC offset, from *0*~*63*, *0* for minimum offset and *63* for maximum offset
        step (str): ADC step size, from *0*~*63*, *0* for minimum step and *63* for maximum step
        comp (str): Comparator enables, from *0x0001*~*0x7FFF*, each bit controls a comparator
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CONF_ADC + ' ' + offset + ' ' + step + ' ' + comp, verbal)


def conf_MAC(mode, resolution, verbal):
    """ **[High Level]** Configure MAC settings

    Args:
        mode (str): MAC mode, *0* for unsigned and *1* for *signed*
        resolution (str): MAC resolution *0* for 1 bit, *1* for 2 bits, *2* for 4 bits, and *3* for 8 bits
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CONF_MAC + ' ' + mode + ' ' + resolution, verbal)


def calibrate_VRef(low, high, tolerance, verbal):
    """ **[High Level]** Calibrate the internally generated reference voltages so the range would be approx. (*low*, *high*) for the current module

    Args:
        low (str): Target lower bound of the reference voltages
        high (str): Target upper bound of the reference voltages
        tolerance (str): Target tolerance from either *low* or *high*
        verbal (bool): Whether to print the response or not.
    Returns:
        (offset, step) which makes ADC fit the desired range.
    """
    return PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CAL_VREF + ' ' + low + ' ' + high + ' ' + tolerance, verbal)


def sweep_VRef(low, high, step, verbal):
    """ **[High Level]** Sweep the ADC_CAL and look for all 15 internally generated reference voltages for the current module

    Args:
        low (str): Starting voltage for ADC_CAL
        high (str): Ending voltage for ADC_CAL
        step (str): Step for ADC_CAL
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_SWEEP_VREF + ' ' + low + ' ' + high + ' ' + step, verbal)


def list_VRef(verbal):
    """ **[High Level]** List 15 internally generated reference voltages of the current module, sweep_VRef needs to be done in advance

    Args:
        verbal (bool): Whether to print the response or not.
    Returns:
        15 internally generated reference voltages of the selected RRAM Module.
    """
    return PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_LIST_VREF, verbal)


def clear_VRef(verbal):
    """ **[High Level]** Clear 15 internally generated reference voltages of the current module

    Args:
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CLEAR_VREF, verbal)


def calibrate_VTGT_BL(verbal):
    """ **[High Level]** Calibrate VTGT_BL for the current module

        **[Note]** This function destroys the values inside some cells

    Args:
        verbal (bool): Whether to print the response or not.
    Returns:
        VTGT_BL which makes readout from 9 parallel HRS cells to be 0x4000.
    """
    return PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CAL_VTGT_BL, verbal)


def conf_VTGT_BL(vtgt_bl, verbal):
    """ **[High Level]** Save the VTGT_BL for the current module

    Args:
        vtgt_bl (str): Voltage value for VTGT_BL.
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CONF_VTGT_BL + ' ' + vtgt_bl, verbal)


def list_VTGT_BL(verbal):
    """ **[High Level]** List saved VTGT_BL of the current module

    Args:
        verbal (bool): Whether to print the response or not.
    Returns:
        The current VTGT_BL of the selected RRAM Module.
    """
    return PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_LIST_VTGT_BL, verbal)


def clear_VTGT_BL(verbal):
    """ **[High Level]** Clear saved VTGT_BL of the current module

    Args:
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CLEAR_VTGT_BL, verbal)


def sweep_DRef(ones, verbal):
    """ **[High Level]** Calibrate decoder reference levels.

        **[Note]** This function destroys the values inside some cells

    Args:
        ones (str): Could be omit or *1*~*9*, omit means do the calibration for all *1*~*9*
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_SWEEP_DREF + ' ' + ones, verbal)


def list_DRef(verbal):
    """ **[High Level]** List decoder reference levels of the current module

    Args:
        verbal (bool): Whether to print the response or not.
    Returns:
        The current decoder reference of the selected RRAM Module.
    """
    return PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_LIST_DREF, verbal)


def clear_DRef(ones, verbal):
    """ **[High Level]** Clear decoder reference levels.

    Args:
        ones (str): Could be omit or *1*~*9*, omit means do the calibration for all *1*~*9*
        verbal (bool): Whether to print the response or not.
    """
    PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CLEAR_DREF + ' ' + ones, verbal)


def check(level, number, verbal):
    """ **[High Level]** Check the health of RRAM cells, this function essentially consists of SET->READ->RESET->READ.
        If the cell is healthy, the ADC raw value after SET should be smaller than the value after RESET.

        **[Note]** This function destroys the values inside some cells

    Args:
        level (str): Hierarchy level, could be *cell*, *row*, *col*, *module*
        number (str): Target number, could be *0*~*65535* for *cell*, *0*~*255* for *row* and *col*, *0* for *module*
        verbal (bool): Whether to print the response or not.
    """
    if level == 'cell':
        address = int(number)
        response = PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CHECK_CELL + ' ' + str(address), False)
        print(f'{address:>6} : {response:>10}')
    elif level == 'row':
        for col in range(0, 256):
            address = int(number)*256 + col
            response = PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CHECK_CELL + ' ' + str(address), False)
            print(f'{address:>6} : {response:>10}')
    elif level == 'col':
        for row in range(0, 256):
            address = row*256 + int(number)
            response = PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CHECK_CELL + ' ' + str(address), False)
            print(f'{address:>6} : {response:>10}')
    elif level == 'module':
        for row in range(0, 256):
            for col in range(0, 256):
                address = row*256 + col
                response = PT.send_command(CM.CM_RRAM + ' ' + CM.CM_RRAM_API_CHECK_CELL + ' ' + str(address), False)
                print(f'{address:>6} : {response:>10}')


def decode(parameters):
    """ Decode the command

    Args:
        parameters (list): Command in List form.
    """
    # Driver functions
    if   parameters[1] == 'id'               : id               (                                                            True)
    elif parameters[1] == 'lane'             : lane             (parameters[2], parameters[3],                               True)
    elif parameters[1] == 'group'            : group            (parameters[2], parameters[3],                               True)
    elif parameters[1] == 'module'           : module           (parameters[2], parameters[3],                               True)
    elif parameters[1] == 'mask'             : mask             (parameters[2], parameters[3],                               True)
    elif parameters[1] == 'address'          : address          (parameters[2], parameters[3],                               True)
    elif parameters[1] == 'read'             : read             (parameters[2], parameters[3], parameters[4],                True)
    elif parameters[1] == 'mac'              : mac              (parameters[2], parameters[3], parameters[4],                True)
    elif parameters[1] == 'write'            : write            (parameters[2], parameters[3], parameters[4],                True)
    elif parameters[1] == 'adc'              : adc              (parameters[2], parameters[3], parameters[4],                True)
    elif parameters[1] == 'pg'               : pg               (parameters[2], parameters[3], parameters[4],                True)
    elif parameters[1] == 'ecc'              : ecc              (parameters[2], parameters[3], parameters[4],                True)
    # API functions
    elif parameters[1] == 'reg_status'       : reg_status       (                                                            True)
    elif parameters[1] == 'env_init'         : env_init         (                                                            True)
    elif parameters[1] == 'env_status'       : env_status       (                                                            True)
    elif parameters[1] == 'mod_init'         : mod_init         (                                                            True)
    elif parameters[1] == 'mod_status'       : mod_status       (                                                            True)
    elif parameters[1] == 'mod_conf'         : mod_conf         (parameters[2],                                              True)
    elif parameters[1] == 'switch'           : switch           (parameters[2],                                              True)
    elif parameters[1] == 'conf_form'        : conf_form        (parameters[2], parameters[3], parameters[4], parameters[5], True)
    elif parameters[1] == 'form'             : form             (parameters[2], parameters[3],                               True)
    elif parameters[1] == 'conf_set'         : conf_set         (parameters[2], parameters[3], parameters[4], parameters[5], True)
    elif parameters[1] == 'set'              : set              (parameters[2], parameters[3],                               True)
    elif parameters[1] == 'set_reset'        : set_reset        (parameters[2], parameters[3], parameters[4],                True)
    elif parameters[1] == 'conf_reset'       : conf_reset       (parameters[2], parameters[3], parameters[4], parameters[5], True)
    elif parameters[1] == 'reset'            : reset            (parameters[2], parameters[3],                               True)
    elif parameters[1] == 'write_byte'       : write_byte       (parameters[2], parameters[3],                               True)
    elif parameters[1] == 'write_byte_iter'  : write_byte_iter  (parameters[2], parameters[3],                               True)
    elif parameters[1] == 'conf_read'        : conf_read        (parameters[2],                                              True)
    elif parameters[1] == 'read_lane'        : read_lane        (parameters[2], parameters[3],                               True)
    elif parameters[1] == 'read_byte'        : read_byte        (parameters[2], parameters[3], parameters[4],                True)
    elif parameters[1] == 'conf_ADC'         : conf_ADC         (parameters[2], parameters[3], parameters[4],                True)
    elif parameters[1] == 'conf_MAC'         : conf_MAC         (parameters[2], parameters[3],                               True)
    elif parameters[1] == 'calibrate_VRef'   : calibrate_VRef   (parameters[2], parameters[3], parameters[4],                True)
    elif parameters[1] == 'sweep_VRef'       : sweep_VRef       (parameters[2], parameters[3], parameters[4],                True)
    elif parameters[1] == 'list_VRef'        : list_VRef        (                                                            True)
    elif parameters[1] == 'clear_VRef'       : clear_VRef       (                                                            True)
    elif parameters[1] == 'calibrate_VTGT_BL': calibrate_VTGT_BL(                                                            True)
    elif parameters[1] == 'conf_VTGT_BL'     : conf_VTGT_BL     (parameters[2],                                              True)
    elif parameters[1] == 'list_VTGT_BL'     : list_VTGT_BL     (                                                            True)
    elif parameters[1] == 'clear_VTGT_BL'    : clear_VTGT_BL    (                                                            True)
    elif parameters[1] == 'sweep_DRef'       : sweep_DRef       (parameters[2],                                              True)
    elif parameters[1] == 'list_DRef'        : list_DRef        (                                                            True)
    elif parameters[1] == 'clear_DRef'       : clear_DRef       (parameters[2],                                              True)
    elif parameters[1] == 'check'            : check            (parameters[2], parameters[3],                               True)
    else: PT.unknown(parameters)
