# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

with open('task6.txt', 'r', encoding='utf-8') as fl:
    content = fl.readlines()
    line_list = []
    target_dict = {}
    for el in content:
        line_list = el.split(' ')
        sum_lessons = 0
        for n in line_list:
            lesson_hours = ''
            for i in n:
                if i.isdigit():
                    lesson_hours += i
            if lesson_hours.isdigit():
                sum_lessons += int(lesson_hours)
        target_dict[line_list[0]] = sum_lessons
    print('Необходимый словарь:')
    print(target_dict)
