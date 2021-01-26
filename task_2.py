from abc import ABC, abstractmethod

class Clothing (ABC):

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothing):

    def __init__(self, size):
        self.__v = size

    @property
    def consumption(self):
        return round(self.__v / 6.5 + 0.5, 2)

    @property
    def size(self):
        return self.__v

class Suit(Clothing):

    def __init__(self, height):
        # height in cm
        self.__h = height

    @property
    def consumption(self):
        return round((2 * self.__h + 0.3) / 100, 2)

    @property
    def height(self):
        return self.__h


c = Coat(48)
s = Suit(178)

print(f'This coat is in size {c.size}. Fabric consumption: {c.consumption} m')
print(f'This Suit is for height {s.height} cm. Fabric consumption: {s.consumption} m')
print(f'Total consumption: {c.consumption + s.consumption} m')
