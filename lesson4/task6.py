
# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count, cycle

def int_list_generator(begin, end):
    int_list = []
    for n in count(begin):
        int_list.append(n)
        if n > end:
            return int_list
            break

def list_element_repeater(inc_list, repeat_number):
    result_list = []
    count = 0
    for n in cycle(inc_list):
        result_list.append(n)
        count += 1
        if count > repeat_number:
            return result_list
            break


# Передаем число с которого начинать генерацию и общее количество нужных элементов, выводим списком

print(int_list_generator(5, 10))

# Передаем сгенерированный список и количество элементов, которые хотим повторить, выводим списком

print(list_element_repeater(int_list_generator(5, 10), 20))


