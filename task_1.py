class Matrix:

    def __init__(self, m):
        self.__m = m
        self.__rows = len(self.__m)
        self.__columns = len(self.__m[0])

    def __str__(self):
        return f'Matrix Size: {self.rows()}x{self.columns()} -> {self.__m}'

    def __add__(self, other):
        if self.rows() != other.rows() or self.columns() != other.columns():
            raise Exception("The matrixes are different. You can't to sum them up.")
        for i in range(self.rows()):
            for j in range(self.columns()):
                self.__m[i][j] = self.get(i, j) + other.get(i, j)
        return self

    def rows(self):
        return self.__rows

    def columns(self):
        return self.__columns

    def get(self, x, y):
        return self.__m[x][y]


s = Matrix([[1, 4, 5, 0], [-5, 8, 1, 0], [-6, 7, 1, 0]])
s2 = Matrix([[2, 1, 4, 0], [-2, 3, 2, 3], [6, -1, 3, 3]])
print(f'First Matrix: {s}')
print(f'Second Matrix: {s2}')
print(f'Sum Matrix: {s + s2}')
