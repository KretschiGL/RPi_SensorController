# Author:       Lukas Kretschmar (lukas.kretschmar@ost.ch)
# License:      MIT

import time
from datetime import datetime
import csv
import os

"""
Controller class to handle multiple sensors.
This class implements the builder pattern.
"""
class SensorController:

    def __init__(self):
        """
        Creates a new SensorController.
        """
        self._sensorFactories = []                # List of factory methods to create sensors (see add() method)
        self._sensors = {}                        # Dictionary for all sensor instances
        self._exportFolder = "./Measurements"     # Folder to store the file

    def register(self, sensorFactory):
        """
        Add a new sensor factory to create a sensor instance when build() is called.
        The sensor factory must be a function or method, so the SensorController
        could provide information for all sensors (e.g., bus, id, etc)
        This feature is currently not used in this code.

        :param sensorFactory: Method to create a new sensor
        :return: This instance
        """
        if sensorFactory == None:                      # Ignore factory when not set
            return self                                # Return SensorController instance (builder pattern)
        self._sensorFactories.append(sensorFactory)    # Add factory to the list
        return self                                    # Return SensorController instance (builder pattern)  

    def build(self):
        """
        Creates all added sensors

        :return: This instance
        """
        self._sensors.clear()                  # Delete all existing sensor instances
        for f in self._sensorFactories:        # Loop through all factory methods
            s = f()                            # Execute factory --> create sensor instance
            self._sensors[s.getName()] = s     # Register sensor with its name to the dict
        return self                            # Return SensorController instance
    
    def measure(self, duration, interval=1.0, exportInterval=3600, printValues=False):
        """
        Run the measurement routine collecting data from all sensors and writing it to a *.csv file.

        :param duration: Duration of the measurement in [s]
        :param interval: Interval for the measruements in [s], default is 1s
        :param exportInterval: Interval to split csv files in [s], default is 3600s
        :param printValues: Option to print the current measurements to the console, default is False
        """
        self._ensureFolder(self._exportFolder)                              # Ensure that the folder exists
        end = time.time() + duration                                        # Calculate when to stop
        self._measureUntil(end, interval, exportInterval, printValues)      # Run the measurement
        return self

    def _ensureFolder(self, folder):
        if not os.path.exists(folder):             # Check if folder exists
            os.makedirs(folder, exist_ok=True)     # If not, create

    def _measureUntil(self, end, interval, exportInterval, printValues): 
        while time.time() < end:                                                               # Loop until end time is reached
            filename = self._createCsvFileName()                                               # Create new filename
            with open(filename, "w+", newline="") as csvFile:                                  # Create the file to write data to
                csvWriter = self._createCsvWriter(csvFile)                                     # Create new csv writer instance
                self._measureSequence(end, interval, exportInterval, printValues, csvWriter)   # Export values for one sequence (until exportInteval reached)

    def _createCsvFileName(self):
        fileDate = datetime.now().strftime("%Y%m%d-%H%M%S")           # Filename for the measurements
        return f"{self._exportFolder}/{fileDate}_Measurements.csv"    # Define file name                 

    def _createCsvWriter(self, csvfile):
        writer = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)    # Create csv writer instance
        header = ["Timestamp"]                                                       # Define header for first column (timestamps)
        for s in self._sensors.values():                                             # Loop through all sensors
            name = s.getName()                                                       # Getting name of sensor
            header.extend([f"{name}_{h}" for h in s.getHeaders()])                   # Adds a sensor's headers with name as prefix to the header list
        writer.writerow(header)                                                      # Write header row to file
        return writer                                                                # Return csv writer

    def _measureSequence(self, end, interval, exportInterval, printValues, csvWriter):
        sequenceEnd = time.time() + exportInterval
        while time.time() < sequenceEnd:                    # Run as long exportInterval not reached
            if time.time() >= end:                          # Check if program completed
                return                                      # Completed
            values = self._getValues(printValues)           # Get values of all sensors
            csvWriter.writerow(values)                      # Write values to csv file
            time.sleep(interval)                            # Wait until next measruement cycle
        return                                              # Export interval reached

    def _getValues(self, printValues):
        values = [datetime.now()]                           # Set timestamp for measruement
        for s in self._sensors.values():                    # Loop through all sensors
            v = s.getValues()                               # Get value of a sensor
            values.extend(v)                                # Add value to value list
            if printValues:                                 # Check if values also should be printed
                s.printValues()                             # If yes, print the value
        return values                                       # Return timestamp and measured values
