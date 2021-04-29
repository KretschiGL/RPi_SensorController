# Author:       Lukas Kretschmar (lukas.kretschmar@ost.ch)
# License:      MIT

import board
import busio
import digitalio
from adafruit_max31865 import MAX31865
from .ISensor import ISensor

"""
Wrapper class for the MAX31865 module.
This class can be used with the SensorController.
"""
class TemperatureSensor_MAX31865(ISensor):
    def __init__(self, name, inout):
        """
        Creates a new MAX31865 wrapper instance.
        :param name: Human readable name of the sensor
        :param inout: Digital identifier for the module the senser is attached to
        """
        spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
        cs = digitalio.DigitalInOut(inout)
        self._name = name
        self._inout = inout
        self._sensor = MAX31865(spi, cs)

    def getName(self):
        """
        Returns the name of the sensor
        """
        return self._name

    def getHeaders(self):
        """
        Returns a list of headers for the values
        """
        return [f"{self._name}_Temp"]

    def getValues(self):
        """
        Returns the measured temperature
        """
        return [self._sensor.temperature]

    def printValues(self):
        """
        Prints the currently measured temperature
        """
        headers = self.getHeaders()
        values = self.getValues()
        for i in range(len(values)):
            print(f"[{headers[i]}] Temperature: {values[i]:0.3f} C")
