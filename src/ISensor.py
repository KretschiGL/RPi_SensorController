# Author:       Lukas Kretschmar (lukas.kretschmar@ost.ch)
# License:      MIT

from abc import ABC, abstractmethod

class ISensor(ABC):

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getValue(self):
        pass

    @abstractmethod
    def printValue(self):
        pass
