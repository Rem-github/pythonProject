# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на
# склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и
# количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def add_to_storage(self):
        pass

    @abstractmethod
    def move_from_main_to_ddb(self):
        pass


class Storage():
    main_base = {}
    develop_department_base = {}


class OfficeEquipment(MyAbstractClass):

    def __init__(self, inventory_number, model, brand, speed):
        self.inventory_number = inventory_number
        self.model = model
        self.brand = brand
        self.speed = speed


class Printer(OfficeEquipment):

    def __init__(self, inventory_number, model, photo, brand, speed, name = 'printer'):
        self.name = name
        self.photo = photo
        super().__init__(inventory_number, model, brand, speed)

    def add_to_storage(self):
        Storage.main_base[self.inventory_number] = (self.name, self.model, self.photo, self.brand, self.speed)

    def move_from_main_to_ddb(self):
        Storage.develop_department_base[self.inventory_number] = (self.name, self.model, self.photo, self.brand, self.speed)
        del Storage.main_base[self.inventory_number]


class Xerox(OfficeEquipment):

    def __init__(self, inventory_number, model, double_side, brand, speed, name = 'xerox'):
        self.name = name
        self.double_side = double_side
        super().__init__(inventory_number, model, brand, speed)

    def add_to_storage(self):
        Storage.main_base[self.inventory_number] = (self.name, self.model, self.double_side, self.brand, self.speed)

    def move_from_main_to_ddb(self):
        Storage.develop_department_base[self.inventory_number] = (self.name, self.model, self.double_side, self.brand, self.speed)
        del Storage.main_base[self.inventory_number]


class Scanner(OfficeEquipment):

    def __init__(self, inventory_number, model, portative, brand, speed, name = 'scanner'):
        self.name = name
        self.portative = portative
        super().__init__(inventory_number, model, brand, speed)

    def add_to_storage(self):
        Storage.main_base[self.inventory_number] = (self.name, self.model, self.portative, self.brand, self.speed)

    def move_from_main_to_ddb(self):
        Storage.develop_department_base[self.inventory_number] = (self.name, self.model, self.portative, self.brand, self.speed)
        del Storage.main_base[self.inventory_number]

a = Printer('pr01', 'l366', 'Photo', 'Epson', 20)
a.add_to_storage()
b = Printer('pr02', 'l366', 'Photo', 'Epson', 20)
b.add_to_storage()
c = Printer('pr03', 'LJ800', 'Office', 'HP', 30)
c.add_to_storage()
d = Xerox('xr01', 'Xerox500', 'Double_Side', 'Xerox', 50)
d.add_to_storage()
s = Scanner('sc01', 'SJ1200', 'tablet', 'HP', 5)
s.add_to_storage()
c.move_from_main_to_ddb()
s.move_from_main_to_ddb()

print(Storage.main_base)
print(Storage.develop_department_base)
