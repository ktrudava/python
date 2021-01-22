class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

    def get_wage(self):
        return self._income.get('wage')

    def get_bonus(self):
        return self._income.get('bonus')

class Position(Worker):
    def get_full_name(self):
        print(f'Full name is {self.name} {self.surname}.')

    def get_total_income(self):
        print(f'Total income is: {self.get_wage() + self.get_bonus()}')


e_1 = Position('Tom', 'Johnson', 'director', 100, 20)
e_2 = Position('Jack', 'Slow', 'cleaner', 50, 8)

print(e_1.name)
print(e_2.surname)
print(e_1.position)

e_1.get_full_name()
e_1.get_total_income()
e_2.get_full_name()
e_2.get_total_income()

