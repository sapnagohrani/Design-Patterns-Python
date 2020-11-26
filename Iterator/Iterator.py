# Iterator Design Pattern describes an interface with next and has_next methods.
from abc import ABCMeta, abstractmethod


class Iterator(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def has_next():
        """Return Boolean whether end of collection has come or not"""

    @staticmethod
    @abstractmethod
    def next():
        """ Return the next object in collection"""


class Iterable(Iterator):
    def __init__(self):
        self.x = 0
        self.maximum = 5

    def has_next(self):
        return self.x < self.maximum

    def next(self):
        if self.x < self.maximum:
            index = self.x
            self.x += 1
            return index
        else:
            raise Exception("End of Collection")


itert = Iterable()
while itert.has_next():
    print(itert.next())
