class OfficeEquipment:

    def __init__(self, cost: int, warranty: str):
        self.cost = cost
        self.warranty = warranty

    def work(self):
        pass

class Printer(OfficeEquipment):

    def __init__(self, cost: int, warranty: str, inkpage: int):
        super().__init__(cost, warranty)
        self.inkpage = inkpage

    def work(self):
        print("bzz bzz I'm Printing!")

class Scanner(OfficeEquipment):

    def __init__(self, cost: int, warranty: str, scanperminute: int):
        super().__init__(cost, warranty)
        self.scanperminute = scanperminute

    def work(self):
        print("wooz wooz I'm Scanning!")

class Copier(OfficeEquipment):

    def __init__(self, cost: int, warranty: str, copyperminute: int):
        super().__init__(cost, warranty)
        self.copyperminute = copyperminute

    def work(self):
        print("prr prr I'm Copying!")


print('Office Equipment')

p1 = Printer(100, '6 months', 10)
p2 = Scanner(350, '12 months', 4)
p3 = Copier(200, '24 months', 8)

for el in (p1, p2, p3):
    el.work()
