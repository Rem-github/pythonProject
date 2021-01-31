
# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
from my_func import cut_space

with open('task2.txt', 'r', encoding='utf-8') as fl:
    content = fl.readlines()
    print('Количество строк в файле: ', len(content))
    for s in content:
        list_tmp = cut_space(s)
        print(f'Количество слов в строке №{content.index(s) + 1}: {len(list_tmp)}')
