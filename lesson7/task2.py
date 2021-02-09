# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся
# пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def quantity_cloth(self):
        pass

class Clothes(MyAbstractClass):

    def __init__(self, name):
        self.name = name


class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self.v = v

    def quantity_cloth(self):
        size = self.v/6.5 + 0.5
        return size

class Suit(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.h = h

    @property
    def quantity_cloth(self):
        size = self.h * 2 + 0.3
        return size

a = Coat('Modern', 6.5)
print(f'Пальто типа {a.name}, размера {a.v} требует {a.quantity_cloth()} м ткани')
b = Suit('New style', 2)
print(f'Костюм типа {b.name}, размера {b.h} требует {b.quantity_cloth} м ткани')
print(f'Общий необходимый метраж ткани: {a.quantity_cloth() + b.quantity_cloth}')
