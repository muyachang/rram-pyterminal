# rram-pyterminal

This program was developed in PyCharm with Python 3.10.0rc2, the purpose of this program is provide an interactive and simple platform for end users to get hands on the RRAM test chip.

### Required Python Packages
- pyserial

### PCB Block Diagram
Figure below shows a overall component markings of the evaluation board.
![PCB](https://user-images.githubusercontent.com/4018299/134605757-104c7f77-8836-4417-b8e7-61fecc7c144b.png)


### Voltage Sources
| Voltage Source | Regulator Type | Power/Value Control Method | Voltage Range (V) | Step Resolution (mV) | Max Supported Current |                
| :----:         | :----:         | :----:                     | :----:            | :----:               | :----:                |
| 3V3 Always On  | LDO            | -  /Potentiometer          | 0.73 ~ VCC        | -                    | 25 mA                 |
| VDD            | LDO            | I2C/Potentiometer          | 0.73 ~ VCC        | -                    | 300 mA                |
| AVDD_SRAM      | LDO            | I2C/Potentiometer          | 0.73 ~ VCC        | -                    | 300 mA                |
| 3V3            | DC/DC          | I2C/I2C                    | 2.06 ~ 4.00       | 62.50                | 1.5 A                 |
| AVDD_WR        | DC/DC          | I2C/I2C                    | 1.08 ~ 4.00       | 32.63 & 62.50        | 1.5 A                 |
| AVDD_WL        | DC/DC          | I2C/I2C                    | 0.83 ~ 3.08       | 25.00 & 48.13        | 2.5 A                 |
| AVDD_RRAM      | DC/DC          | I2C/I2C                    | 0.83 ~ 1.60       | 25.00                | 2.5 A                 |
    
### DAC Sources
There're two DAC sources: "**VTGT_BL**" and "**ADC_CAL**", where each of them can be 0 ~ 3V3 with 12 bit resolution.
- **VTGT_BL**: Target voltage for the bit lines. (Nominal range: 80 ~ 120 mV)
- **ADC_CAL**: Used for ADC calibration mode, where the input of ADC would be this voltage source instead of bit lines.

### Command List
| argv[0] | argv[1]        | argv[2]   | argv[3]      | argv[4]  | argv[5]     | Explanation                                                     
| :----:  | :----:         | :----:    | :----:       | :----:   | :----:      | :---                                                           
| BOARD   | version        |           |              |          |             | List current Atmel firmware version
| PM      | list           |           |              |          |             | List current status for each voltage sources                    
| PM      | clear          |           |              |          |             | Clear the IRQ register (Might not be used often)                
| PM      | status         |           |              |          |             | Print out the IRQ register value                                
| PM      | save           |           |              |          |             | Save current configuration into EEPROM                          
| PM      | load           |           |              |          |             | Load previous configuration from EEPROM                         
| PM      | allon          |           |              |          |             | Turn all the voltage sources on                                 
| PM      | alloff         |           |              |          |             | Turn all the voltage sources off                                
| PM      | reset          |           |              |          |             | Reset the voltage regulator                                     
| PM      | enable         | [target]  |              |          |             | Turn on the specified voltage source                            
| PM      | disable        | [target]  |              |          |             | Turn off the specified voltage source                           
| PM      | ++             | [target]  |              |          |             | Increase a step of the specified voltage source                 
| PM      | --             | [target]  |              |          |             | Decrease a step of the specified voltage source                 
| PM      | +              | [value]   | [target]     |          |             | Increase [value] mV of the specified voltage source             
| PM      | -              | [value]   | [target]     |          |             | Decrease [value] mV of the specified voltage source             
| PM      | set            | [value]   | [target]     |          |             | Set the specified voltage source to [value] mV                  
| PM      | get            | [target]  |              |          |             | Get the value of the specified voltage source (Supposely)       
| DAC     | list           |           |              |          |             | List current status for each DAC ouptut                         
| DAC     | ++             | [target]  |              |          |             | Increase a step of the specified DAC output                     
| DAC     | --             | [target]  |              |          |             | Decrease a step of the specified DAC output                     
| DAC     | +              | [value]   | [target]     |          |             | Increase [value] mV of the specified DAC output                 
| DAC     | -              | [value]   | [target]     |          |             | Decrease [value] mV of the specified DAC output                 
| DAC     | set            | [value]   | [target]     |          |             | Set the specified DAC output to [value] mV                      
| DAC     | get            | [target]  |              |          |             | Print out the value of the specified DAC output (Supposely)     
| DF      | status         |           |              |          |             | Print out 2 bytes value of the status register                  
| DF      | id             |           |              |          |             | Print out 3 bytes ID (1 byte Manufacturer ID + 2 bytes ID Bytes)
| DF      | reset          |           |              |          |             | Software reset the data flash                                   
| DF      | read           | sector    | [number]     |          |             | Print out the value of sector [number] ("0a", "0b", or 1~63)                         
| DF      | read           | block     | [number]     |          |             | Print out the value of block [number]                           
| DF      | read           | page      | [number]     |          |             | Print out the value of page [number]                            
| DF      | read           | byte      | [number]     |          |             | Print out the value at [address]                                
| DF      | write          | [address] | [value]      |          |             | Write [value] to [address]                                      
| DF      | erase          | chip      |              |          |             | Erase the whole chip                                            
| DF      | erase          | sector    | [number]     |          |             | Erase sector [number] ("0a", "0b", or 1~63)     
| DF      | erase          | block     | [number]     |          |             | Erase block [number]                                            
| DF      | erase          | page      | [number]     |          |             | Erase page [number]                                             
| DF      | protect        | enable    |              |          |             | Enable sector protection                                        
| DF      | protect        | disable   |              |          |             | Disable sector protection                                       
| DF      | protect        | status    |              |          |             | Print out the sector protection status                          
| DF      | protect        | all       |              |          |             | Protect all the sectors                                         
| DF      | protect        | none      |              |          |             | Protect none of the sectors                                     
| DF      | protect        | add       | [sector]     |          |             | Add protection for [sector] ("0a", "0b", or 1~63)                                    
| DF      | protect        | remove    | [sector]     |          |             | Remove protection for [sector] ("0a", "0b", or 1~63)                                 
| DF      | blankcheck     |           |              |          |             | Check whether the chip is empty                                 
| EEPROM  | read           | [address] |              |          |             | Print out the value at [address]                                
| EEPROM  | write          | [address] | [value]      |          |             | Write [value] to  [address]                                     
| LED     | enable         | [target]  |              |          |             | Enable the specified LED ([target] can be "TX" or "RX")         
| LED     | disable        | [target]  |              |          |             | Disable the specified LED ([target] can be "TX" or "RX")        
| LED     | toggle         | [target]  |              |          |             | Toggle the specified LED ([target] can be "TX" or "RX")         
| TC      | connect        |           |              |          |             | Connect with the testchip and print out the Device ID         
| TC      | disconnect     |           |              |          |             |
| TC      | read           | [address] |              |          |             | Read the value of [address]                                     
| TC      | write          | [address] | [value]      |          |             | Write [value] to  [address]         
| TC      | list           |           |              |          |             |         
| TC      | save           | [number]  |              |          |             |         
| TC      | load           | [number]  |              |          |             |                                     
| DEMO    | list           |           |              |          |             | List available demos                                            
| DEMO    | load           | [number]  |              |          |             | Load demo [number] to the RRAM testchip                         
| DEMO    | run            |           |              |          |             | Move master role to RRAM testchip and reset the testchip        
| DEMO    | analyze        |           |              |          |             | Analyze the size of each demo to speedup the load process       
| RRAM    | id             |           |              |          |             | Return PID of the RRAM Modules (Should be 0x01314520)           
| RRAM    | status         |           |              |          |             | Print out a lot of information about current status             
| RRAM    | lane           | set       | [number]     |          |             | Set the ADC lane to [number] (0~7)                              
| RRAM    | lane           | get       |              |          |             | Get the ADC lane                                                
| RRAM    | group          | set       | [number]     |          |             | Set the vector group to [number] (0~35)                         
| RRAM    | group          | get       |              |          |             | Get the vector group                                            
| RRAM    | module         | set       | [number]     |          |             | Set the RRAM module [number] (0~287)                            
| RRAM    | module         | get       |              |          |             | Get the RRAM module                                             
| RRAM    | mask           | set       | [hex]        |          |             | Set mask to [hex] (0x000 ~ 0x1FF)                               
| RRAM    | mask           | get       |              |          |             | Get mask                                                        
| RRAM    | address        | set       | [number]     |          |             | Set the address to [number] (0~65535)                           
| RRAM    | address        | get       |              |          |             | Get the address                                                 
| RRAM    | read           | set       | enable       | [number] |             | Set read enable (1: Enabled, 0: Disabled)                       
| RRAM    | read           | get       | enable       |          |             | Get read enable (1: Enabled, 0: Disabled)                       
| RRAM    | read           | get       | status       |          |             | Get read status (1: Done, 0: In Progess)                        
| RRAM    | read           | get       |              |          |             | Toggle read strobe                                              
| RRAM    | read           | set       | cycle        | [number] |             | Set read cycles (0~255)                                         
| RRAM    | read           | get       | cycle        |          |             | Get read cycles                                                 
| RRAM    | read           | set       | source       | [number] |             | Set read source (1: vector, 0: M3)                              
| RRAM    | read           | get       | source       |          |             | Get read source (1: vector, 0: M3)                              
| RRAM    | read           | set       | counter      | [number] |             | Set read counter (0~7)                                          
| RRAM    | read           | get       | counter      |          |             | Get read counter                                                
| RRAM    | read           | set       | data         | [hex]    |             | Set read data_in (0x000 ~ 0x1FF)                                
| RRAM    | read           | get       | data         |          |             | Get read data_in                                                
| RRAM    | mac            | get       | status       |          |             | Get MAC status (1: Done, 0: In Progess)                         
| RRAM    | mac            | set       | mode         | [number] |             | Set MAC mode (0: unsigned, 1: signed)                           
| RRAM    | mac            | get       | mode         |          |             | Get MAC mode (0: unsigned, 1: signed)                           
| RRAM    | mac            | set       | resolution   | [number] |             | Set MAC resolution (0: 1 bit, 1: 2 bits, 2: 4 bits, 3: 8 bits)  
| RRAM    | mac            | get       | resolution   |          |             | Get MAC resolution (0: 1 bit, 1: 2 bits, 2: 4 bits, 3: 8 bits)  
| RRAM    | mac            | get       | result       |          |             | Get the MAC result                                              
| RRAM    | write          | set       | enable       | [number] |             | Set write enable (1: Enabled, 0: Disabled)                      
| RRAM    | write          | get       | enable       |          |             | Get write enable (1: Enabled, 0: Disabled)                      
| RRAM    | write          | get       | status       |          |             | Get write status (1: Done, 0: In Progess)                       
| RRAM    | write          | trigger   |              |          |             | Trigger write operation                                         
| RRAM    | write          | set       | cycle        | [number] |             | Set write cycles (0~65535)                                      
| RRAM    | write          | get       | cycle        |          |             | Get write cycles                                                
| RRAM    | write          | set       | mode         | [number] |             | Set write mode (0: SET?, 1: RST?)                               
| RRAM    | write          | get       | mode         |          |             | Get write mode (0: SET?, 1: RST?)                               
| RRAM    | adc            | get       | raw          |          |             | Print out raw ADC output                                        
| RRAM    | adc            | set       | step         | [number] |             | Set CTRL_STEP to [number] (0~63)   0: Widest, 1: Narrowest      
| RRAM    | adc            | get       | step         |          |             | Get CTRL_STEP                                                   
| RRAM    | adc            | set       | offset       | [number] |             | Set CTRL_OFFSET [number] (0~63)   0: Min offset, 1: Max offset  
| RRAM    | adc            | get       | offset       |          |             | Get CTRL_OFFSET                                                 
| RRAM    | adc            | set       | comp         | [hex]    |             | Set Comparator Enables to [hex] (0x0000 ~ 0x7FFF)               
| RRAM    | adc            | get       | comp         |          |             | Get Comparator Enables                                          
| RRAM    | adc            | set       | hbias        | [number] |             | Set hbias mode (1: Enabled, 0: Disabled)                        
| RRAM    | adc            | get       | hbias        |          |             | Get hbias mode (1: Enabled, 0: Disabled)                        
| RRAM    | adc            | set       | cal          | [number] |             | Set cal mode (1: Enabled, 0: Disabled)                          
| RRAM    | adc            | get       | cal          |          |             | Get cal mode (1: Enabled, 0: Disabled)                          
| RRAM    | pg             | set       | disable      | [number] |             | Set power gating mode (0: Enabled, 1: Disabled)                 
| RRAM    | pg             | get       | disable      |          |             | Get power gating mode (0: Enabled, 1: Disabled)                 
| RRAM    | ecc            | set       | enable       | [number] |             | Set ECC mode (1: Enabled, 0: Disabled)                          
| RRAM    | ecc            | get       | enable       |          |             | Get ECC mode (1: Enabled, 0: Disabled)                          
| RRAM    | ecc            | clear     |              |          |             | Clear ECC flag                                                  
| RRAM    | ecc            | check     |              |          |             | Check ECC flag
| RRAM    | conf_form      | [AVDD_WR] | [AVDD_WL]    | [cycle]  | [times]     | Configure (AVDD_WR, AVDD_WL, cycle, times) for FORM operations                                                  
| RRAM    | form           | [type]    | [number]     |          |             | Perform FORM operations. (ex. "form cell 2", "form row 3", "form col 4", "form module")                                                 
| RRAM    | conf_set       | [AVDD_WR] | [AVDD_WL]    | [cycle]  | [times]     | Configure (AVDD_WR, AVDD_WL, cycle, times) for SET operations                                                  
| RRAM    | set            | [type]    | [number]     |          |             | Perform SET operations. (ex. "set cell 2", "set row 3", "set col 4", "set module")                                                      
| RRAM    | conf_reset     | [AVDD_WR] | [AVDD_WL]    | [cycle]  | [times]     | Configure (AVDD_WR, AVDD_WL, cycle, times) for RESET operations                                                  
| RRAM    | reset          | [type]    | [number]     |          |             | Perform RESET operations. (ex. "reset cell 2", "reset row 3", "reset col 4", "reset module")                                                       
| RRAM    | write_byte     | [addr]    | [value]      |          |             | Write [value] to [addr], simpler version of write.                                                  
| RRAM    | write_byte_iter| [addr]    | [value]      |          |             | Write [value] to [addr] with iterative verification, more complex version of write.
| RRAM    | conf_read      | [AVDD_WL] | [cycle]      |          |             | Configure (AVDD_WL, cycle) for READ operations
| RRAM    | read_lane      | [addr]    | [data]       |          |             | Read [addr] with [data] WLs turned on (Only that lane is being read)
| RRAM    | read_byte      | [addr]    | [counter]    | [data]   |             | Read the whole byte at [addr] with [data] WLs turned on (8 lanes are being read)
| RRAM    | conf_ADC       | [offset]  | [step]       | [comp]   |             | Configure (Offset, Step, Comparator) for ADCs                                                  
| RRAM    | conf_MAC       | [mode]    | [resolution] |          |             | Configure (Mode, Resolution) for MACs                                                  
| RRAM    | calibrate_VRef | [index]   | [low]        | [high]   | [tolerance] | Calibrate reference voltages for module [index] so the range is between [low]~[high] with tolerance [tolerance]
| RRAM    | sweep_VRef     | [index]   | [low]        | [high]   | [step]      | Sweep ADC_CAL from [low]~[high] with step [step] to get 15 reference voltages for module [index]
| RRAM    | list_VRef      | [index]   |              |          |             | List reference voltages of module [index]
| RRAM    | calibrate_DRef | [index]   | [ones]       |          |             | Calibrate decoder reference levels for [ones] WLs turned on simultaneously. (Omitting [ones] parameter to perform calibration for [ones] = 1~9)  
| RRAM    | list_DRef      | [index]   |              |          |             | List decoder reference levels of module [index]
| RRAM    | check          | [type]    | [number]     |          |             | Check the status of cells, i.e. perform set and reset one after another to make sure the cells are responsive.

### Suggested Form/Set/Reset/Read Parameters
| Type   | AVDD_WR(mV) | AVDD_WL(mV) | Cycles | Times
| :----: | :----:      | :----:      | :----: | :----:      
| Form   | 3200        | 1600        | 20     | 4        
| Set    | 2200        | 2200        | 100    | 20        
| Reset  | 2800        | 2800        | 200    | 80        
| Read   | N/A         | 1100        | 5      | N/A         
