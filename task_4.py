class Car:
    def __init__(self, speed, colour, name, is_police: bool):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go(self):
        print('moving')

    def stop(self):
        print('stopped')

    def turn(self, direction):
        if direction == "right":
            print('turned right')
        elif direction == 'left':
            print('turned left')
        elif direction == 'straight':
            print('going straight')
        else:
            print('choose direction: left, straight or right')

    def show_speed(self, current_speed):
        print(f'Current speed is {current_speed}.')


class TownCar(Car):

    def __init__(self, speed, colour, name, is_police, seats):
        self.seats = seats
        Car.__init__(self, speed, colour, name, is_police)

    def show_speed(self, current_speed):
        Car.show_speed(self, current_speed)
        if current_speed > 60:
            print('You exceeded the speed limit (60 kmh)!')


class SportCar(Car):

    def __init__(self, speed, colour, name, is_police, year):
        self.year = year
        Car.__init__(self, speed, colour, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, colour, name, is_police, size):
        self.size = size
        Car.__init__(self, speed, colour, name, is_police)

    def show_speed(self, current_speed):
        Car.show_speed(self, current_speed)
        if current_speed > 40:
            print('You exceeded the speed limit (40 kmh)!')


class PoliceCar(Car):

    def __init__(self, speed, colour, name, is_police, wheels):
        self.wheels = wheels
        Car.__init__(self, speed, colour, name, is_police)


p = PoliceCar(200, 'blue', 'Mazda', True, 4)
w = WorkCar(120, 'yellow', 'Ford', False, 'small')
s = SportCar(350, 'red', 'Ferrari', False, 2014)
t = TownCar(180, 'black', 'Fiat', False, 2)

print(p.speed, p.wheels)
print(w.colour, w.size)
print(s.name, s.year)
print(t.is_police)
print(t.seats)

t.show_speed(120)
s.show_speed(80)
w.show_speed(70)

s.go()
t.stop()
p.turn('back')
p.turn('left')
