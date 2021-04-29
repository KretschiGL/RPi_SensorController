# Author:       Lukas Kretschmar (lukas.kretschmar@ost.ch)
# License:      MIT

import numpy
from src.ISensor import ISensor

"""
Mock TemperatureSensor to test the code.
This class should not be used in production.
"""
class TemperatureSensor_Mock(ISensor):
    
    def __init__(self, name):
        """
        :param name: Human readable name of the sensor
        """
        self._name = name
        self._rng = numpy.random.RandomState(42)

    def getName(self):
        """
        Returns the name of the sensor
        """
        return self._name

    def getHeaders(self):
        """
        Returns a list of headers
        """
        return [f"{self._name}_Temp"]

    def getValues(self):
        """
        Returns a normal distributed (N(25,1)) value
        """
        return [self._rng.normal(25,1)]

    def printValues(self):
        """
        Prints a temperature value
        """
        headers = self.getHeaders()
        values = self.getValues()
        for i in range(len(values)):
            print(f"[{headers[i]}] Temperature: {values[i]:0.3f} C")
