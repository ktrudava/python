class Cell:

    def __init__(self, num):
        self.__num = num

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __sub__(self, other):
        if other.num > self.__num:
            raise ValueError('We cannot have a negative number of cells!')
        return Cell(self.num - other.num)

    def __truediv__(self, other):
        return Cell(self.num / other.num)

    def make_order(self, cell, row_len: int) -> str:
        s = ''
        for i in range(cell.num):
            s += '*'
            if (i+1) % row_len == 0:
                s += '\n'
        return s

    @property
    def num(self):
        return self.__num

    def __str__(self):
        return 'Cell[' + str(self.__num) + ']'


c1 = Cell(19)
c2 = Cell(10)
print(f'Initial Cells: C1 {c1} and C2 {c2}')
print(f'Summing cells: C1 + C2 = {c1 + c2}')
print(f'Subtracting cells: C1 - C2 = {c1 - c2}')
print(f'Multiplying cells: C1 * C2 = {c1 * c2}')
print(f'Dividing cells: C1 / C2 = {c1 / c2}')
print(f'Making order: \n{c2.make_order(c1, 6)}')
