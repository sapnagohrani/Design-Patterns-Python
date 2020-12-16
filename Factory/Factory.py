from abc import ABCMeta, abstractmethod


class ChairInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_dimensions(self):
        """Abstract Method"""


class SmallChair(ChairInterface):
    def __init__(self, l, b, h):
        self.l = l
        self.b = b
        self.h = h

    def get_dimensions(self):
        print("Dimension of small chair -> Length : " + str(self.l) + " Breadth : " + str(self.b) + " Height : " + str(
            self.h))
class BigChair(ChairInterface):
    def __init__(self, l, b, h):
        self.l = l
        self.b = b
        self.h = h

    def get_dimensions(self):
        print("Dimension of small chair -> Length : " + str(self.l) + " Breadth : " + str(self.b) + " Height : " + str(
            self.h))


class ChairFactory:
    def get_chair_dimension(self, name):
        if name == 'SmallChair':
            return SmallChair(10, 20, 30)
        elif name == 'BigChair':
            return BigChair(80, 90, 100)


chfct = ChairFactory()
chair = chfct.get_chair_dimension('SmallChair')
chair.get_dimensions()
chair = chfct.get_chair_dimension('BigChair')
chair.get_dimensions()
