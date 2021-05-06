# Author:       Lukas Kretschmar (lukas.kretschmar@ost.ch)
# License:      MIT

from src.SensorController import SensorController
from .TemperatureSensor_Mock import TemperatureSensor_Mock

# Test program to check if the SensorController works as expected (on PC)
class Test:
    
    def run(self):
        # Creating a new instance of SensorController and add 4 different TemperatureSensors
        # build() at the end will create all registered sensors
        controller = SensorController()\
            .register(lambda : TemperatureSensor_Mock("TempSensor1"))\
            .register(lambda : TemperatureSensor_Mock("TempSensor2"))\
            .build()

        # Run the measurement for 10s and print the values to the console
        controller.measure(15, exportInterval=5, printValues=True)
