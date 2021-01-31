# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
from my_func import create_dict

with open('task3.txt', 'r', encoding='utf-8') as fl:
    content = fl.readlines()
    empl_dict = {}
    empl_dict.update(create_dict(content))
    print('Оклад менее 20000 рублей имеют следующие сотрудники:')
    sum_salary = 0
    for name, salary in empl_dict.items():
        if salary < 20000:
            print(name)
        sum_salary += salary
    print(f'Средняя зарплата по компании: {(sum_salary/len(empl_dict)):.0f} рублей')
