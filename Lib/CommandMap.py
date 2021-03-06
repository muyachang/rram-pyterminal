##############
# Atmel Part #
##############
# argv[0]
CM_BOARD                    = b'\x40'.decode('utf-8')
CM_PM                       = b'\x41'.decode('utf-8')
CM_DAC                      = b'\x42'.decode('utf-8')
CM_DF                       = b'\x43'.decode('utf-8')
CM_EEPROM                   = b'\x44'.decode('utf-8')
CM_LED                      = b'\x45'.decode('utf-8')
CM_TC                       = b'\x46'.decode('utf-8')
CM_DEMO                     = b'\x47'.decode('utf-8')
CM_RRAM                     = b'\x48'.decode('utf-8')
CM_VECTOR                   = b'\x49'.decode('utf-8')
CM_DNN                      = b'\x4A'.decode('utf-8')
                      
# argv[1]
CM_BOARD_VERSION            = b'\x41'.decode('utf-8')

CM_PM_CLEAR                 = b'\x41'.decode('utf-8')
CM_PM_STATUS                = b'\x42'.decode('utf-8')
CM_PM_SAVE                  = b'\x43'.decode('utf-8')
CM_PM_LOAD                  = b'\x44'.decode('utf-8')
CM_PM_RESET                 = b'\x45'.decode('utf-8')
CM_PM_ENABLE                = b'\x46'.decode('utf-8')
CM_PM_DISABLE               = b'\x47'.decode('utf-8')
CM_PM_INCR                  = b'\x48'.decode('utf-8')
CM_PM_DECR                  = b'\x49'.decode('utf-8')
CM_PM_PLUS                  = b'\x4A'.decode('utf-8')
CM_PM_MINUS                 = b'\x4B'.decode('utf-8')
CM_PM_SET                   = b'\x4C'.decode('utf-8')
CM_PM_SET_SAFE              = b'\x4D'.decode('utf-8')
CM_PM_GET                   = b'\x4E'.decode('utf-8')

CM_DAC_SAVE                 = b'\x41'.decode('utf-8')
CM_DAC_LOAD                 = b'\x42'.decode('utf-8')
CM_DAC_INCR                 = b'\x43'.decode('utf-8')
CM_DAC_DECR                 = b'\x44'.decode('utf-8')
CM_DAC_PLUS                 = b'\x45'.decode('utf-8')
CM_DAC_MINUS                = b'\x46'.decode('utf-8')
CM_DAC_SET                  = b'\x47'.decode('utf-8')
CM_DAC_GET                  = b'\x48'.decode('utf-8')
                      
CM_DF_STATUS                = b'\x41'.decode('utf-8')
CM_DF_ID                    = b'\x42'.decode('utf-8')
CM_DF_RESET                 = b'\x43'.decode('utf-8')
CM_DF_READ                  = b'\x44'.decode('utf-8')
CM_DF_WRITE                 = b'\x45'.decode('utf-8')
CM_DF_ERASE                 = b'\x46'.decode('utf-8')
CM_DF_PROTECT               = b'\x47'.decode('utf-8')
CM_DF_BLANKCHECK            = b'\x48'.decode('utf-8')

CM_DF_PROTECT_ENABLE        = b'\x41'.decode('utf-8')
CM_DF_PROTECT_DISABLE       = b'\x42'.decode('utf-8')
CM_DF_PROTECT_STATUS        = b'\x43'.decode('utf-8')
CM_DF_PROTECT_ADD           = b'\x44'.decode('utf-8')
CM_DF_PROTECT_REMOVE        = b'\x45'.decode('utf-8')

CM_EEPROM_READ              = b'\x41'.decode('utf-8')
CM_EEPROM_WRITE             = b'\x42'.decode('utf-8')
                      
CM_LED_ENABLE               = b'\x41'.decode('utf-8')
CM_LED_DISABLE              = b'\x42'.decode('utf-8')
CM_LED_TOGGLE               = b'\x43'.decode('utf-8')
                      
CM_TC_CONNECT               = b'\x41'.decode('utf-8')
CM_TC_DISCONNECT            = b'\x42'.decode('utf-8')
CM_TC_READ                  = b'\x43'.decode('utf-8')
CM_TC_WRITE                 = b'\x44'.decode('utf-8')
CM_TC_LIST                  = b'\x45'.decode('utf-8')
CM_TC_SAVE                  = b'\x46'.decode('utf-8')
CM_TC_LOAD                  = b'\x47'.decode('utf-8')
CM_TC_REMOVE                = b'\x48'.decode('utf-8')
                      
CM_DEMO_LIST                = b'\x41'.decode('utf-8')
CM_DEMO_LOAD                = b'\x42'.decode('utf-8')
CM_DEMO_RUN                 = b'\x43'.decode('utf-8')
CM_DEMO_ANALYZE             = b'\x44'.decode('utf-8')

CM_RRAM_PID                 = b'\x41'.decode('utf-8')
CM_RRAM_LANE                = b'\x42'.decode('utf-8')
CM_RRAM_GROUP               = b'\x43'.decode('utf-8')
CM_RRAM_MODULE              = b'\x44'.decode('utf-8')
CM_RRAM_MASK                = b'\x45'.decode('utf-8')
CM_RRAM_ADDRESS             = b'\x46'.decode('utf-8')
CM_RRAM_READ                = b'\x49'.decode('utf-8')
CM_RRAM_MAC                 = b'\x4A'.decode('utf-8')
CM_RRAM_WRITE               = b'\x4B'.decode('utf-8')
CM_RRAM_ADC                 = b'\x4C'.decode('utf-8')
CM_RRAM_PG                  = b'\x4F'.decode('utf-8')
CM_RRAM_ECC                 = b'\x50'.decode('utf-8')

CM_RRAM_API_REG_STATUS      = b'\x51'.decode('utf-8')
CM_RRAM_API_ENV_INIT        = b'\x52'.decode('utf-8')
CM_RRAM_API_ENV_STATUS      = b'\x53'.decode('utf-8')
CM_RRAM_API_MOD_INIT        = b'\x54'.decode('utf-8')
CM_RRAM_API_MOD_STATUS      = b'\x55'.decode('utf-8')
CM_RRAM_API_MOD_CONF        = b'\x56'.decode('utf-8')
CM_RRAM_API_SWITCH          = b'\x57'.decode('utf-8')
CM_RRAM_API_CONF_FORM       = b'\x58'.decode('utf-8')
CM_RRAM_API_FORM            = b'\x59'.decode('utf-8')
CM_RRAM_API_CONF_SET        = b'\x5A'.decode('utf-8')
CM_RRAM_API_SET             = b'\x5B'.decode('utf-8')
CM_RRAM_API_CONF_RESET      = b'\x5C'.decode('utf-8')
CM_RRAM_API_RESET           = b'\x5D'.decode('utf-8')
CM_RRAM_API_SET_RESET       = b'\x5E'.decode('utf-8')
CM_RRAM_API_WRITE_BYTE      = b'\x5F'.decode('utf-8')
CM_RRAM_API_WRITE_BYTE_ITER = b'\x60'.decode('utf-8')
CM_RRAM_API_CONF_READ       = b'\x61'.decode('utf-8')
CM_RRAM_API_READ_LANE       = b'\x62'.decode('utf-8')
CM_RRAM_API_READ_BYTE       = b'\x63'.decode('utf-8')
CM_RRAM_API_CONF_ADC        = b'\x64'.decode('utf-8')
CM_RRAM_API_CONF_MAC        = b'\x65'.decode('utf-8')
CM_RRAM_API_CAL_VREF        = b'\x66'.decode('utf-8')
CM_RRAM_API_SWEEP_VREF      = b'\x67'.decode('utf-8')
CM_RRAM_API_LIST_VREF       = b'\x68'.decode('utf-8')
CM_RRAM_API_CLEAR_VREF      = b'\x69'.decode('utf-8')
CM_RRAM_API_CAL_VTGT_BL     = b'\x70'.decode('utf-8')
CM_RRAM_API_CONF_VTGT_BL    = b'\x71'.decode('utf-8')
CM_RRAM_API_LIST_VTGT_BL    = b'\x72'.decode('utf-8')
CM_RRAM_API_CLEAR_VTGT_BL   = b'\x73'.decode('utf-8')
CM_RRAM_API_SWEEP_DREF      = b'\x74'.decode('utf-8')
CM_RRAM_API_LIST_DREF       = b'\x75'.decode('utf-8')
CM_RRAM_API_CLEAR_DREF      = b'\x76'.decode('utf-8')
CM_RRAM_API_CHECK_CELL      = b'\x77'.decode('utf-8')

CM_RRAM_API_LEVEL_CELL      = b'\x41'.decode('utf-8')
CM_RRAM_API_LEVEL_ROW       = b'\x42'.decode('utf-8')
CM_RRAM_API_LEVEL_COL       = b'\x43'.decode('utf-8')
CM_RRAM_API_LEVEL_MODULE    = b'\x44'.decode('utf-8')

CM_RRAM_API_MOD_STATUS_CLEAN            = 0
CM_RRAM_API_MOD_STATUS_FORMED           = 1
CM_RRAM_API_MOD_STATUS_PARTIALLY_FORMED = 2
CM_RRAM_API_MOD_STATUS_USED             = 3
CM_RRAM_API_MOD_STATUS_BROKEN           = 4
CM_RRAM_API_MOD_STATUS_ADC_FATAL        = 5
CM_RRAM_API_MOD_STATUS_UNKNOWN          = 6

CM_VECTOR_PID               = b'\x41'.decode('utf-8')

CM_DNN_IN_CONF_LEN          = b'\x41'.decode('utf-8')
CM_DNN_IN_CLEAR             = b'\x42'.decode('utf-8')
CM_DNN_IN_FILL              = b'\x43'.decode('utf-8')
CM_DNN_IN_PRINT             = b'\x44'.decode('utf-8')
CM_DNN_NN_CLEAR             = b'\x45'.decode('utf-8')
CM_DNN_NN_CONF_TYPE         = b'\x46'.decode('utf-8')
CM_DNN_NN_CONF_RRAMS        = b'\x47'.decode('utf-8')
CM_DNN_NN_CONF_INPUT        = b'\x48'.decode('utf-8')
CM_DNN_NN_CONF_KERNEL       = b'\x49'.decode('utf-8')
CM_DNN_NN_CONF_OUTPUT       = b'\x50'.decode('utf-8')
CM_DNN_NN_CONF_OUTPUT_Q     = b'\x51'.decode('utf-8')
CM_DNN_NN_CONF_ECC          = b'\x52'.decode('utf-8')
CM_DNN_NN_PRINT             = b'\x53'.decode('utf-8')
CM_DNN_FORWARD              = b'\x54'.decode('utf-8')

CM_DNN_TYPE_LINEAR          = 0
CM_DNN_TYPE_CONV            = 1
CM_DNN_TYPE_MAXPOOL         = 2
CM_DNN_TYPE_RELU            = 3
CM_DNN_TYPE_ARGMAX          = 4
CM_DNN_TYPE_EON             = 5

# argv[2]
CM_RRAM_SET                 = b'\x41'.decode('utf-8')
CM_RRAM_GET                 = b'\x42'.decode('utf-8')
CM_RRAM_TOGGLE              = b'\x43'.decode('utf-8')
CM_RRAM_TRIGGER             = b'\x44'.decode('utf-8')
CM_RRAM_CLEAR               = b'\x45'.decode('utf-8')
CM_RRAM_CHECK               = b'\x46'.decode('utf-8')

# argv[3]
CM_RRAM_READ_ENABLE         = b'\x41'.decode('utf-8')
CM_RRAM_READ_STATUS         = b'\x42'.decode('utf-8')
CM_RRAM_READ_CYCLE          = b'\x43'.decode('utf-8')
CM_RRAM_READ_SOURCE         = b'\x44'.decode('utf-8')
CM_RRAM_READ_COUNTER        = b'\x45'.decode('utf-8')
CM_RRAM_READ_DATA           = b'\x46'.decode('utf-8')

CM_RRAM_MAC_STATUS          = b'\x41'.decode('utf-8')
CM_RRAM_MAC_MODE            = b'\x42'.decode('utf-8')
CM_RRAM_MAC_RESOLUTION      = b'\x43'.decode('utf-8')
CM_RRAM_MAC_RESULT          = b'\x44'.decode('utf-8')

CM_RRAM_WRITE_ENABLE        = b'\x41'.decode('utf-8')
CM_RRAM_WRITE_STATUS        = b'\x42'.decode('utf-8')
CM_RRAM_WRITE_CYCLE         = b'\x43'.decode('utf-8')
CM_RRAM_WRITE_MODE          = b'\x44'.decode('utf-8')

CM_RRAM_ADC_RAW             = b'\x41'.decode('utf-8')
CM_RRAM_ADC_STEP            = b'\x42'.decode('utf-8')
CM_RRAM_ADC_OFFSET          = b'\x43'.decode('utf-8')
CM_RRAM_ADC_COMP            = b'\x44'.decode('utf-8')
CM_RRAM_ADC_HBIAS           = b'\x45'.decode('utf-8')
CM_RRAM_ADC_CAL             = b'\x46'.decode('utf-8')

CM_RRAM_PG_DISABLE          = b'\x41'.decode('utf-8')

CM_RRAM_ECC_ENABLE          = b'\x41'.decode('utf-8')