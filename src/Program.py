# Author:       Lukas Kretschmar (lukas.kretschmar@ost.ch)
# License:      MIT

import board
from .SensorController import SensorController
from .TemperatureSensor_MAX31865 import TemperatureSensor_MAX31865

class Program:

    def run(self):
        # Creating a new instance of SensorController and add 4 different TemperatureSensors
        # build() at the end will create all registered sensors
        # With this design, multiple different sensors can be registered (not only for measuring
        # the temperature)
        controller = SensorController()\
            .register(lambda : TemperatureSensor_MAX31865("TempSensor1", board.D25))\
            .register(lambda : TemperatureSensor_MAX31865("TempSensor2", board.D26))\
            .register(lambda : TemperatureSensor_MAX31865("TempSensor3", board.D27))\
            .register(lambda : TemperatureSensor_MAX31865("TempSensor4", board.D28))\
            .build()

        # Run the measurement for 10s and print the values to the console
        controller.measure(10, printValues=True)
