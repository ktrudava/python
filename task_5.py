class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('drawing started')


class Pen(Stationary):

    def draw(self):
        print(f'drawing started with a pen!')


class Pencil(Stationary):

    def draw(self):
        print('your pencil needs sharpening!')


class Handle(Stationary):

    def draw(self):
        print('sorry, no drawing possible!')


s = Stationary(Stationary)
pn = Pen(Pen)
pnc = Pencil(Pencil)
h = Handle(Handle)

s.draw()
pn.draw()
pnc.draw()
h.draw()

