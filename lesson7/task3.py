# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться
# только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток,
# соответственно. В методе деления должно осуществляться округление значения до целого числа.

class Cell:

    def __init__(self, cell_number):
        self.cell_number = cell_number
    def __str__(self):
        return f'{self.cell_number}'
    def __add__(self, other):
        return Cell(self.cell_number + other.cell_number)
    def __sub__(self, other):
        if self.cell_number - other.cell_number > 0:
            return Cell(self.cell_number - other.cell_number)
        else:
            return f'Не достаточное количество ячеек для вычитания'
    def __mul__(self, other):
        return Cell(self.cell_number * other.cell_number)
    def __truediv__(self, other):
        return Cell(round(self.cell_number / other.cell_number)) # противоречие в задании. Я выбрал этот вариант

    def make_order(self, cell, row_length):
        self.cell = cell
        self.row_length = row_length
        self.st = ''
        for i in range(cell.cell_number):
            if i % row_length == 0:
                self.st += '\n'
            self.st += '*'
        return self.st


cell1 = Cell(8)
cell2 = Cell(10)
cell3 = cell1 + cell2
print(cell3)
cell4 = cell3 - cell2
print(cell4)
cell5 = cell4 * cell1
print(cell5)
cell6 = cell5 / cell3
print(cell6)
print(cell3.make_order(cell3, 4))


