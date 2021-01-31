# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

russian_numbers = ['Один','Два','Три','Четыре']

with open('task4_1.txt', 'r', encoding='utf-8') as fl:
    content = fl.readlines()

with open('task4_2.txt', 'w', encoding='utf-8') as fl:
    tmp_list = ''
    count = 0
    for s in content:
        tmp_list = s.split(' ')
        tmp_list.pop(0)
        tmp_list.insert(0, russian_numbers[count])
        count += 1
        fl.write(' '.join(tmp_list))
