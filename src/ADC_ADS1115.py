from ADS1x15 import ADS1115
from .ISensor import ISensor

GAIN = 1
ADC_CHAN_NUM = 4

class ADC_ADS1115(ISensor):

    def __init__(self, name, addr, channels=ADC_CHAN_NUM):
        self._name = name
        self._channels = channels
        self._adc = ADS1115(address=addr, busnum=1)

    def getName(self):
        """
        Returns the name of the sensor.
        """
        return self._name

    def getHeaders(self):
        """
        Returns the list of headers of the data.
        First, the raw data for channels 1-4 is listed,
        then the voltage on the channel 1-4 is exported.
        """
        headers = [f"RawData_{ch}" for ch in range(1, self._channels + 1)]         # Generating the column headers for the channels raw data
        return headers

    def getValues(self):
        """
        Exporting the raw data on channels 1-4,
        then the voltages on channels 1-4.
        """
        values = []
        for i in range(self._channels):
            value = self._adc.read_adc(i, gain=GAIN, data_rate=128)
            values.append(value)
        return values

    def printValues(self):
        """
        Prints the current values of the ADC component.
        """
        headers = self.getHeaders()
        values = self.getValues()
        for i in range(len(values)):
            print(f"{headers[i]}: {values[i]}")
    