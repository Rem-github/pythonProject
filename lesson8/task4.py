# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Storage():
    pass


class OfficeEquipment():

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


class Xerox(OfficeEquipment):

    def __init__(self, inventory_number, model, double_side, brand, speed, name = 'xerox'):
        self.name = name
        self.double_side = double_side
        super().__init__(inventory_number, model, brand, speed)


class Scanner(OfficeEquipment):

    def __init__(self, inventory_number, model, portative, brand, speed, name = 'scanner'):
        self.name = name
        self.portative = portative
        super().__init__(inventory_number, model, brand, speed)

