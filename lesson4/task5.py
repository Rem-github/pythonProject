
# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить
# результат вычисления произведения всех элементов списка.

from functools import reduce

user_list = [n for n in range(100, 1001, 2)]
result = reduce(lambda x,y: x * y, user_list)
print(result)