# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        st = ''
        for el in self.matrix_list:
            for num in el:
                st += str(num) + ' '
            st +='\n'
        return f'{st}'

    def __add__(self, other):
        new_list = []
        if len(self.matrix_list) == len(other.matrix_list):
            for el in range(len(self.matrix_list)):
                if len(self.matrix_list[el]) == len(other.matrix_list[el]):
                    new_list.append([])
                    for j in range(len(self.matrix_list[el])):
                        new_list[el].append(self.matrix_list[el][j] + other.matrix_list[el][j])
                else:
                    return f'Матрицы разного размера'
        else:
            return f'Матрицы разного размера'
        return Matrix(new_list)





x = Matrix([[1,2,3,4,5],[0,9,8,7,6],[5,6,4,7,3]])
y = Matrix([[0,2,3,4,0],[0,9,8,7,0],[0,6,4,7,0]])
print(x)
print(y)
z = x + y
print(z)
