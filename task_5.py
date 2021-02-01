class OfficeEquipment:

    def __init__(self, name: str, serial_number: str, cost: int, warranty: str):
        self.name = name
        self.serial_number = serial_number
        self.cost = cost
        self.warranty = warranty

    def work(self):
        pass

    def name_itself(self):
        pass


class Printer(OfficeEquipment):

    def __init__(self, name: str, serial_number: str, cost: int, warranty: str, inkpage: int):
        super().__init__(name, serial_number, cost, warranty)
        self.inkpage = inkpage

    def work(self):
        print("bzz bzz I'm Printing!")

    def name_itself(self):
        print(f"{self.serial_number}: I'm Printer!")


class Scanner(OfficeEquipment):

    def __init__(self, name: str, serial_number: str, cost: int, warranty: str, scanperminute: int):
        super().__init__(name, serial_number, cost, warranty)
        self.scanperminute = scanperminute

    def work(self):
        print("wooz wooz I'm Scanning!")

    def name_itself(self):
        print(f"{self.serial_number}: I'm Scanner!")


class Copier(OfficeEquipment):

    def __init__(self, name: str, serial_number: str, cost: int, warranty: str, copyperminute: int):
        super().__init__(name, serial_number, cost, warranty)
        self.copyperminute = copyperminute

    def work(self):
        print("prr prr I'm Copying!")

    def name_itself(self):
        print(f"{self.serial_number}: I'm Copier!")


class Warehouse:

    def __init__(self):
        self.storage = {}

    def addToStorage(self, e: OfficeEquipment):
        self.storage[e.serial_number] = e


print('Office Equipment:')

p1 = Printer("Printer", "PSD123123", 100, '6 months', 10)
p2 = Scanner("Scanner", "SJKKJ1324", 350, '12 months', 4)
p3 = Copier("Copier", "EDD333444", 200, '24 months', 8)

print('Store it on a Warehouse:')

w = Warehouse()
w.addToStorage(p1)
w.addToStorage(p2)
w.addToStorage(p3)

for equipment in (w.storage.values()):
    equipment.name_itself()
