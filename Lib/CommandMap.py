##############
# Atmel Part #
##############
# argv[0]
CM_PM                 = b'\x41'.decode('utf-8')
CM_DAC                = b'\x42'.decode('utf-8')
CM_DF                 = b'\x43'.decode('utf-8')
CM_EEPROM             = b'\x44'.decode('utf-8')
CM_LED                = b'\x45'.decode('utf-8')
CM_TC                 = b'\x46'.decode('utf-8')
CM_DEMO               = b'\x47'.decode('utf-8')
CM_RRAM               = b'\x48'.decode('utf-8')
CM_VECTOR             = b'\x49'.decode('utf-8')
                      
# argv[1]             
CM_PM_CLEAR           = b'\x41'.decode('utf-8')
CM_PM_STATUS          = b'\x42'.decode('utf-8')
CM_PM_SAVE            = b'\x43'.decode('utf-8')
CM_PM_LOAD            = b'\x44'.decode('utf-8')
CM_PM_RESET           = b'\x45'.decode('utf-8')
CM_PM_ENABLE          = b'\x46'.decode('utf-8')
CM_PM_DISABLE         = b'\x47'.decode('utf-8')
CM_PM_INCR            = b'\x48'.decode('utf-8')
CM_PM_DECR            = b'\x49'.decode('utf-8')
CM_PM_PLUS            = b'\x4A'.decode('utf-8')
CM_PM_MINUS           = b'\x4B'.decode('utf-8')
CM_PM_SET             = b'\x4C'.decode('utf-8')
CM_PM_GET             = b'\x4D'.decode('utf-8')
                      
CM_DAC_INCR           = b'\x41'.decode('utf-8')
CM_DAC_DECR           = b'\x42'.decode('utf-8')
CM_DAC_PLUS           = b'\x43'.decode('utf-8')
CM_DAC_MINUS          = b'\x44'.decode('utf-8')
CM_DAC_SET            = b'\x45'.decode('utf-8')
CM_DAC_GET            = b'\x46'.decode('utf-8')
                      
CM_DF_STATUS          = b'\x41'.decode('utf-8')
CM_DF_ID              = b'\x42'.decode('utf-8')
CM_DF_RESET           = b'\x43'.decode('utf-8')
CM_DF_READ            = b'\x44'.decode('utf-8')
CM_DF_WRITE           = b'\x45'.decode('utf-8')
CM_DF_ERASE           = b'\x46'.decode('utf-8')
CM_DF_PROTECT         = b'\x47'.decode('utf-8')
CM_DF_BLANKCHECK      = b'\x48'.decode('utf-8')

CM_DF_PROTECT_ENABLE  = b'\x41'.decode('utf-8')
CM_DF_PROTECT_DISABLE = b'\x42'.decode('utf-8')
CM_DF_PROTECT_STATUS  = b'\x43'.decode('utf-8')
CM_DF_PROTECT_ADD     = b'\x44'.decode('utf-8')
CM_DF_PROTECT_REMOVE  = b'\x45'.decode('utf-8')

CM_EEPROM_READ        = b'\x41'.decode('utf-8')
CM_EEPROM_WRITE       = b'\x42'.decode('utf-8')
                      
CM_LED_ENABLE         = b'\x41'.decode('utf-8')
CM_LED_DISABLE        = b'\x42'.decode('utf-8')
CM_LED_TOGGLE         = b'\x43'.decode('utf-8')
                      
CM_TC_CONNECT         = b'\x41'.decode('utf-8')
CM_TC_READ            = b'\x42'.decode('utf-8')
CM_TC_WRITE           = b'\x43'.decode('utf-8')
                      
CM_DEMO_LIST          = b'\x41'.decode('utf-8')
CM_DEMO_LOAD          = b'\x42'.decode('utf-8')
CM_DEMO_RUN           = b'\x43'.decode('utf-8')
CM_DEMO_ANALYZE       = b'\x44'.decode('utf-8')    


######################
# RRAM Testchip Part #
######################
# argv[0]
#define CM_RRAM     0x48 // Need to match with Atmel
#define CM_VECTOR   0x49 // Need to match with Atmel

# argv[1]
CM_RRAM_PID            = b'\x41'.decode('utf-8')
CM_RRAM_STATUS         = b'\x42'.decode('utf-8')
CM_RRAM_LANE           = b'\x43'.decode('utf-8')
CM_RRAM_GROUP          = b'\x44'.decode('utf-8')
CM_RRAM_MODULE         = b'\x45'.decode('utf-8')
CM_RRAM_MASK           = b'\x46'.decode('utf-8')
CM_RRAM_ADDRESS        = b'\x49'.decode('utf-8')
CM_RRAM_READ           = b'\x4A'.decode('utf-8')
CM_RRAM_MAC            = b'\x4B'.decode('utf-8')
CM_RRAM_WRITE          = b'\x4C'.decode('utf-8')
CM_RRAM_ADC            = b'\x4F'.decode('utf-8')
CM_RRAM_PG             = b'\x50'.decode('utf-8')
CM_RRAM_ECC            = b'\x51'.decode('utf-8')
                      
# argv[2]             
CM_RRAM_SET            = b'\x41'.decode('utf-8')
CM_RRAM_GET            = b'\x42'.decode('utf-8')
CM_RRAM_TOGGLE         = b'\x43'.decode('utf-8')
CM_RRAM_TRIGGER        = b'\x44'.decode('utf-8')
CM_RRAM_CLEAR          = b'\x45'.decode('utf-8')
CM_RRAM_CHECK          = b'\x46'.decode('utf-8')

# argv[3]
CM_RRAM_READ_ENABLE    = b'\x41'.decode('utf-8')
CM_RRAM_READ_STATUS    = b'\x42'.decode('utf-8')
CM_RRAM_READ_CYCLE     = b'\x43'.decode('utf-8')
CM_RRAM_READ_SOURCE    = b'\x44'.decode('utf-8')
CM_RRAM_READ_COUNTER   = b'\x45'.decode('utf-8')
CM_RRAM_READ_DATA      = b'\x46'.decode('utf-8')

CM_RRAM_MAC_STATUS     = b'\x41'.decode('utf-8')
CM_RRAM_MAC_MODE       = b'\x42'.decode('utf-8')
CM_RRAM_MAC_RESOLUTION = b'\x43'.decode('utf-8')
CM_RRAM_MAC_RESULT     = b'\x44'.decode('utf-8')

CM_RRAM_WRITE_ENABLE   = b'\x41'.decode('utf-8')
CM_RRAM_WRITE_STATUS   = b'\x42'.decode('utf-8')
CM_RRAM_WRITE_CYCLE    = b'\x43'.decode('utf-8')
CM_RRAM_WRITE_MODE     = b'\x44'.decode('utf-8')

CM_RRAM_ADC_RAW        = b'\x41'.decode('utf-8')
CM_RRAM_ADC_STEP       = b'\x42'.decode('utf-8')
CM_RRAM_ADC_OFFSET     = b'\x43'.decode('utf-8')
CM_RRAM_ADC_COMP       = b'\x44'.decode('utf-8')
CM_RRAM_ADC_HBIAS      = b'\x45'.decode('utf-8')
CM_RRAM_ADC_CAL        = b'\x46'.decode('utf-8')

CM_RRAM_PG_DISABLE     = b'\x41'.decode('utf-8')

CM_RRAM_ECC_ENABLE     = b'\x41'.decode('utf-8')