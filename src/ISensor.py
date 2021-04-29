# Author:       Lukas Kretschmar (lukas.kretschmar@ost.ch)
# License:      MIT

from abc import ABC, abstractmethod

class ISensor(ABC):

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getHeaders(self):
        pass

    @abstractmethod
    def getValues(self):
        pass

    @abstractmethod
    def printValues(self):
        pass
