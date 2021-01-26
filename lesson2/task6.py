
# Эта программа получает список товаров и выводит значения-характеристики

"""
example_list = [(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
(2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
(3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'}),
(4, {'название': 'чайник', 'цена': 56000, 'количество': 100, 'eд': 'шт.'})]
"""

def list_create(n):
    example_list = []
    temp_dict = {}
    temp_tuple = []
    for i in range(n):
        name = input("Введите название: ")
        cost = input("Введите цену товара: ")
        quantity = int(input("Введите количество товара: "))
        temp_dict = {'название': name, 'цена': cost, 'количество': quantity, 'ед.':'шт.'}
        temp_tuple = [i+1, temp_dict]
        temp_tuple = tuple(temp_tuple)
        example_list.append(temp_tuple)
    return example_list

n = int(input("Сколько позиций ассортимента вы хотите добавить? "))

example_list = list_create(n)


print(f'Получен список: {example_list}')
print('Собранная аналитика выглядит так:')

all_keys = []
for key in example_list[0][1]:
    all_keys.append(key)

required_dict = {}
for key in all_keys:
    val_list = []
    for i in range(len(example_list)):
        val_list.append(example_list[i][1][key])
    elem = {key : list(set(val_list))}
    required_dict.update(elem)

for key in required_dict:
    print(f"'{key}': '{required_dict[key]}'")
