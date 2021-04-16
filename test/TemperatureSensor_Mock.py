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

    def getValue(self):
        """
        Returns a normal distributed (N(25,1)) value
        """
        return self._rng.normal(25,1)

    def printValue(self):
        """
        Prints a temperature value
        """
        print(f"[{self._name}] Temperature: {self.getValue():0.3f} C")
