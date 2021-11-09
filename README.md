# rram-pyterminal

This program was developed in PyCharm with Python 3.10.0rc2, the purpose of this program is provide an interactive and simple platform for end users to get hands on the RRAM test chip.

### Required Python Packages
- pyserial

### Evaluation Board
#### Structure
![Structure](https://user-images.githubusercontent.com/4018299/140850588-7cd2da58-717a-46f9-90fd-8df5c18abf03.png)
#### Block Diagram
![Block Diagram](https://user-images.githubusercontent.com/4018299/140850607-568fab2c-8d2b-47f8-9299-e08c622d739e.png)
#### Mother Board
![Mother Board](https://user-images.githubusercontent.com/4018299/140850611-f4fd9769-1034-425f-a181-0ed47ddad647.png)
#### Daughter Board
![Daughter Board](https://user-images.githubusercontent.com/4018299/140850609-052c539d-31b6-4576-bfc6-f63140e24af5.png)


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
The detail description of the functions below are inside each .py files
| argv[0] | argv[1]        | argv[2]   | argv[3]      | argv[4]  | argv[5]    
| :----:  | :----:         | :----:    | :----:       | :----:   | :----:     
| BOARD   | version        |           |              |          |            
| PM      | list           |           |              |          |            
| PM      | clear          |           |              |          |            
| PM      | status         |           |              |          |            
| PM      | save           |           |              |          |            
| PM      | load           |           |              |          |            
| PM      | allon          |           |              |          |            
| PM      | alloff         |           |              |          |            
| PM      | reset          |           |              |          |            
| PM      | enable         | [target]  |              |          |            
| PM      | disable        | [target]  |              |          |            
| PM      | ++             | [target]  |              |          |            
| PM      | --             | [target]  |              |          |            
| PM      | +              | [value]   | [target]     |          |            
| PM      | -              | [value]   | [target]     |          |            
| PM      | set            | [value]   | [target]     |          |            
| PM      | get            | [target]  |              |          |            
| DAC     | list           |           |              |          |            
| DAC     | ++             | [target]  |              |          |            
| DAC     | --             | [target]  |              |          |            
| DAC     | +              | [value]   | [target]     |          |            
| DAC     | -              | [value]   | [target]     |          |            
| DAC     | set            | [value]   | [target]     |          |            
| DAC     | get            | [target]  |              |          |            
| DF      | status         |           |              |          |            
| DF      | id             |           |              |          |            
| DF      | reset          |           |              |          |            
| DF      | read           | sector    | [number]     |          |            
| DF      | read           | block     | [number]     |          |            
| DF      | read           | page      | [number]     |          |            
| DF      | read           | byte      | [number]     |          |            
| DF      | write          | [address] | [value]      |          |            
| DF      | erase          | chip      |              |          |            
| DF      | erase          | sector    | [number]     |          |            
| DF      | erase          | block     | [number]     |          |            
| DF      | erase          | page      | [number]     |          |            
| DF      | protect        | enable    |              |          |            
| DF      | protect        | disable   |              |          |            
| DF      | protect        | status    |              |          |            
| DF      | protect        | all       |              |          |            
| DF      | protect        | none      |              |          |            
| DF      | protect        | add       | [sector]     |          |            
| DF      | protect        | remove    | [sector]     |          |            
| DF      | blankcheck     |           |              |          |            
| EEPROM  | read           | [address] |              |          |            
| EEPROM  | write          | [address] | [value]      |          |            
| LED     | enable         | [target]  |              |          |            
| LED     | disable        | [target]  |              |          |            
| LED     | toggle         | [target]  |              |          |            
| TC      | connect        |           |              |          |            
| TC      | disconnect     |           |              |          |            
| TC      | read           | [address] |              |          |            
| TC      | write          | [address] | [value]      |          |            
| TC      | list           |           |              |          |            
| TC      | save           | [number]  |              |          |            
| TC      | load           | [number]  |              |          |            
| DEMO    | list           |           |              |          |            
| DEMO    | load           | [number]  |              |          |            
| DEMO    | run            |           |              |          |            
| DEMO    | analyze        |           |              |          |            
| RRAM    | id             |           |              |          |            
| RRAM    | status         |           |              |          |            
| RRAM    | lane           | set       | [number]     |          |            
| RRAM    | lane           | get       |              |          |            
| RRAM    | group          | set       | [number]     |          |            
| RRAM    | group          | get       |              |          |            
| RRAM    | module         | set       | [number]     |          |            
| RRAM    | module         | get       |              |          |            
| RRAM    | mask           | set       | [hex]        |          |            
| RRAM    | mask           | get       |              |          |            
| RRAM    | address        | set       | [number]     |          |            
| RRAM    | address        | get       |              |          |            
| RRAM    | read           | set       | enable       | [number] |            
| RRAM    | read           | get       | enable       |          |            
| RRAM    | read           | get       | status       |          |            
| RRAM    | read           | get       |              |          |            
| RRAM    | read           | set       | cycle        | [number] |            
| RRAM    | read           | get       | cycle        |          |            
| RRAM    | read           | set       | source       | [number] |            
| RRAM    | read           | get       | source       |          |            
| RRAM    | read           | set       | counter      | [number] |            
| RRAM    | read           | get       | counter      |          |            
| RRAM    | read           | set       | data         | [hex]    |            
| RRAM    | read           | get       | data         |          |            
| RRAM    | mac            | get       | status       |          |            
| RRAM    | mac            | set       | mode         | [number] |            
| RRAM    | mac            | get       | mode         |          |            
| RRAM    | mac            | set       | resolution   | [number] |            
| RRAM    | mac            | get       | resolution   |          |            
| RRAM    | mac            | get       | result       |          |            
| RRAM    | write          | set       | enable       | [number] |            
| RRAM    | write          | get       | enable       |          |            
| RRAM    | write          | get       | status       |          |            
| RRAM    | write          | trigger   |              |          |            
| RRAM    | write          | set       | cycle        | [number] |            
| RRAM    | write          | get       | cycle        |          |            
| RRAM    | write          | set       | mode         | [number] |            
| RRAM    | write          | get       | mode         |          |            
| RRAM    | adc            | get       | raw          |          |            
| RRAM    | adc            | set       | step         | [number] |            
| RRAM    | adc            | get       | step         |          |            
| RRAM    | adc            | set       | offset       | [number] |            
| RRAM    | adc            | get       | offset       |          |            
| RRAM    | adc            | set       | comp         | [hex]    |            
| RRAM    | adc            | get       | comp         |          |            
| RRAM    | adc            | set       | hbias        | [number] |            
| RRAM    | adc            | get       | hbias        |          |            
| RRAM    | adc            | set       | cal          | [number] |            
| RRAM    | adc            | get       | cal          |          |            
| RRAM    | pg             | set       | disable      | [number] |            
| RRAM    | pg             | get       | disable      |          |            
| RRAM    | ecc            | set       | enable       | [number] |            
| RRAM    | ecc            | get       | enable       |          |            
| RRAM    | ecc            | clear     |              |          |            
| RRAM    | ecc            | check     |              |          |            
| RRAM    | conf_form      | [AVDD_WR] | [AVDD_WL]    | [cycle]  | [times]    
| RRAM    | form           | [level]   | [number]     |          |            
| RRAM    | conf_set       | [AVDD_WR] | [AVDD_WL]    | [cycle]  | [times]    
| RRAM    | set            | [level]   | [number]     |          |            
| RRAM    | conf_reset     | [AVDD_WR] | [AVDD_WL]    | [cycle]  | [times]    
| RRAM    | reset          | [level]   | [number]     |          |            
| RRAM    | write_byte     | [address] | [value]      |          |            
| RRAM    | write_byte_iter| [address] | [value]      |          |            
| RRAM    | conf_read      | [AVDD_WL] | [cycle]      |          |            
| RRAM    | read_lane      | [address] | [data]       |          |            
| RRAM    | read_byte      | [address] | [counter]    | [data]   |            
| RRAM    | conf_ADC       | [offset]  | [step]       | [comp]   |            
| RRAM    | conf_MAC       | [mode]    | [resolution] |          |            
| RRAM    | calibrate_VRef | [index]   | [low]        | [high]   | [tolerance]
| RRAM    | sweep_VRef     | [index]   | [low]        | [high]   | [step]     
| RRAM    | list_VRef      | [index]   |              |          |            
| RRAM    | sweep_DRef     | [index]   | [ones]       |          |            
| RRAM    | list_DRef      | [index]   |              |          |            
| RRAM    | check          | [level]   | [number]     |          |            

### Suggested Form/Set/Reset/Read Parameters
| Type   | AVDD_WR(mV) | AVDD_WL(mV) | Cycles | Times
| :----: | :----:      | :----:      | :----: | :----:      
| Form   | 3200        | 1600        | 20     | 4        
| Set    | 2200        | 2200        | 100    | 20        
| Reset  | 2800        | 2800        | 200    | 80        
| Read   | N/A         | 1100        | 5      | N/A         
