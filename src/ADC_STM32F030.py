# Author:       Lukas Kretschmar (lukas.kretschmar@ost.ch)
# License:      MIT

from grove.i2c import Bus
from .ISensor import ISensor

ADC_DEFAULT_IIC_ADDR = 0X04
ADC_CHAN_NUM = 8
 
REG_RAW_DATA_START = 0X10
REG_VOL_START = 0X20

# Based on the code provided by https://wiki.seeedstudio.com/8-Channel_12-Bit_ADC_for_Raspberry_Pi-STM32F030/
"""
ADC Data Reader for the STM32F030
"""
class ADC_STM32F030(ISensor):

    def __init__(self, name, bus_num=1, addr=ADC_DEFAULT_IIC_ADDR, channels=ADC_CHAN_NUM):
        self._name = name                    # Setting the name
        self._bus = Bus(bus_num)             # Creating the Bus object
        self._addr = addr                    # Assigning the address
        self._channels = channels            # Assigning the number of channels

    def getName(self):
        """
        Returns the name of the sensor.
        """
        return self._name

    def getHeaders(self):
        """
        Returns the list of headers of the data.
        First, the raw data for channels 1-8 is listed,
        then the voltage on the channel 1-8 is exported.
        """
        headers = [f"RawData_{ch}" for ch in range(1,9)]         # Generating the column headers for the channels raw data
        headers.extend([f"Voltage_{ch}" for ch in range(1,9)])   # Generating the column headesr for the channels voltages
        return headers

    def getValues(self):
        """
        Exporting the raw data on channels 1-8,
        then the voltages on channels 1-8.
        """
        values = self._getRawValues(REG_RAW_DATA_START)
        values.extend(self._getRawValues(REG_VOL_START))
        return values

    def _getRawValues(self, reg_start):
        values = []
        for ch in range(self._channels):  
            data=self._bus.read_i2c_block_data(self._addr, reg_start + ch,2)
            val=data[1]<<8|data[0]
            values.append(val)
        return values

    def printValues(self):
        """
        Prints the current values of the ADC component.
        """
        headers = self.getHeaders()
        values = self.getValues()
        for i in range(len(values)):
            print(f"{headers[i]}: {values[i]}")
    