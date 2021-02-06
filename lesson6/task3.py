# Реализовать базовый класс Worker (работник).

# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
# с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.

class Worker:

    def __init__(self, _income, name = '', surname = '', position = ''):
        self._income = _income
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):

    def get_full_name(self):
        self.name = input('Введите имя: ')          # Можно было передать как аргументы метода, аналогично словарю с деньгами
        self.surname = input('Введите фамилию: ')   # Не знаю как правильнее
        return self.name, self.surname

    def get_total_income(self):
        self.total = sum(self._income.values())
        return self.total



a = Position({"wage": 10000, "bonus": 5000})
b = Position({"wage": 15000, "bonus": 10000})
a.get_full_name()
print(f'Имя: {a.name}, Фамилия: {a.surname}')
print(f'Общий доход: {a.get_total_income()} рублей')
b.get_full_name()
print(f'Имя: {b.name}, Фамилия: {b.surname}')
print(f'Общий доход: {b.get_total_income()} рублей')
