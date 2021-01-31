class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_quantity(self):
        return self._length * self._width * norm * thickness / 1000


norm = float(input('Enter the norm of asphalt needed to cover one square metre of road 1 cm thick, kilos - '))
thickness = float(input('How many centimetres thick should the road be? - '))

r = Road(20, 5000)
print(f'You will need {r.asphalt_quantity()} tons of asphalt to cover the road.')

