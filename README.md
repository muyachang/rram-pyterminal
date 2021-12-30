# rram-pyterminal

PyTerminal was developed in PyCharm with Python 3.6.7, the purpose of this is to provide an interactive and simple 
platform for end users to get hands on our RRAM test chip.

- ## Required Python Packages
  - pyserial

- ## Evaluation Board
  - ### Structure
      ![Structure](https://user-images.githubusercontent.com/4018299/140850588-7cd2da58-717a-46f9-90fd-8df5c18abf03.png)
  - ### Block Diagram
      ![Block Diagram](https://user-images.githubusercontent.com/4018299/140850607-568fab2c-8d2b-47f8-9299-e08c622d739e.png)
  - ### Mother Board
      ![Mother Board](https://user-images.githubusercontent.com/4018299/140850611-f4fd9769-1034-425f-a181-0ed47ddad647.png)
  - ### Daughter Board
      ![Daughter Board](https://user-images.githubusercontent.com/4018299/140850609-052c539d-31b6-4576-bfc6-f63140e24af5.png)

- ## Voltage Sources

    | Voltage Source | Regulator Type | Power/Value<br/>Control | Voltage Range (V) | Resolution (mV) | Max Supported Current |                
    | :----:         | :----:         | :----:                  | :----:            | :----:          | :----:                |
    | `3V3 AO`       | LDO            | -  /Pot                 | 0.73 ~ VCC        | -               | 25 mA                 |
    | `VDD`          | LDO            | I2C/Pot                 | 0.73 ~ VCC        | -               | 300 mA                |
    | `AVDD_SRAM`    | LDO            | I2C/Pot                 | 0.73 ~ VCC        | -               | 300 mA                |
    | `3V3`          | DC/DC          | I2C/I2C                 | 2.06 ~ 4.00       | 62.50           | 1.5 A                 |
    | `AVDD_WR`      | DC/DC          | I2C/I2C                 | 1.08 ~ 4.00       | 32.63/62.50     | 1.5 A                 |
    | `AVDD_WL`      | DC/DC          | I2C/I2C                 | 0.83 ~ 3.08       | 25.00/48.13     | 2.5 A                 |
    | `AVDD_RRAM`    | DC/DC          | I2C/I2C                 | 0.83 ~ 1.60       | 25.00           | 2.5 A                 |

- ## DAC Sources
    There are two DAC sources: `VTGT_BL` and `ADC_CAL`, where each of them can be *0* ~ *3.3* V with *12* bit resolution.
  - `VTGT_BL`: Target voltage for the bit lines. (Nominal range: *20* ~ *200* mV)
  - `ADC_CAL`: Used for ADC calibration mode, where the input of ADC would be connected to this voltage source instead of bit lines.

- ## Command List
  - ### Board component driver
    - [BOARD](https://muyachang.github.io/rram-pyterminal/docs/Board/BOARD.html)
    - [DAC](https://muyachang.github.io/rram-pyterminal/docs/Board/DAC.html)
    - [DF (Data Flash)](https://muyachang.github.io/rram-pyterminal/docs/Board/DF.html)
    - [EEPROM](https://muyachang.github.io/rram-pyterminal/docs/Board/EEPROM.html)
    - [LED](https://muyachang.github.io/rram-pyterminal/docs/Board/LED.html)
    - [PM (Power Management)](https://muyachang.github.io/rram-pyterminal/docs/Board/PM.html)
    - [TC (Testchip)](https://muyachang.github.io/rram-pyterminal/docs/Board/TC.html)
  - ### Library API
    - [DEMO](https://muyachang.github.io/rram-pyterminal/docs/Lib/DEMO.html)
    - [RRAM](https://muyachang.github.io/rram-pyterminal/docs/Lib/RRAM.html)
    - [VECTOR](https://muyachang.github.io/rram-pyterminal/docs/Lib/VECTOR.html)
    - [DNN](https://muyachang.github.io/rram-pyterminal/docs/Lib/DNN.html)

- ## Suggested Parameters

    | Type   | AVDD_WR (mV) | AVDD_WL (mV) | Cycles | Times
    | :----: | :----:       | :----:       | :----: | :----:      
    | FORM   | 3200         | 1600         | 20     | 2     
    | SET    | 2200         | 2200         | 100    | 2        
    | RESET  | 2800         | 2800         | 200    | 8        
    | READ   | N/A          | N/A          | 5      | N/A

- ## Firmware Update
    To update the firmwares, please refer to [rram-programmer](https://muyachang.github.io/rram-programmer/) repo.
