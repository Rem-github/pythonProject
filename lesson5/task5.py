# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint

with open('task5.txt', 'w', encoding='utf-8') as fl:
    for i in range(10):
        fl.write(str(randint(0, 10))+' ')

with open('task5.txt', 'r', encoding='utf-8') as fl:
    content = fl.read()
    con_list = content.split(' ')
    sum_nubmers = 0
    for n in con_list:
        try:
            sum_nubmers += int(n)
        except ValueError:
            pass
    print('Сумма чисел в файле:', sum_nubmers)
