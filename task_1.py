import time


class TrafficLight:

    def __init__(self):
        self.__color = "red"

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def show_status(self):
        print(f'The TrafficLight color is {self.get_color()}')

    def launch(self):
        self.set_color("red")
        self.show_status()
        time.sleep(7)
        self.set_color("yellow")
        self.show_status()
        time.sleep(2)
        self.set_color("green")
        self.show_status()
        time.sleep(3)


t = TrafficLight()
t.launch()
print("Now you can go! It's safe.")
