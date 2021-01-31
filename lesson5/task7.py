# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
# со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json

ownership = ['ООО', 'ИП', 'ЗАО']
line_list = []
average_profit = 0
company_dict = {}
av_profit = {}
with open('task7.txt', 'r', encoding='utf-8') as fl:
    content = fl.readlines()
    for el in content:
        line_list = el.split(' ')
        name_list = []
        name = ''
        profit = 0
        for st in line_list:
            if st in ownership:
                break
            else:
                name_list.append(st)
        name = ' '.join(name_list)
        profit = int(line_list[-2]) - int(line_list[-1])
        company_dict[name] = profit
        average_profit += profit
    average_profit = average_profit/len(content)
    av_profit['average_profit'] = round(average_profit)
    print(company_dict)
    print(av_profit)
    json_list = [company_dict,av_profit]
with open('task7.json', 'w', encoding='utf-8') as f_write:
    json.dump(json_list,f_write, ensure_ascii=False)

with open('task7.json', 'r', encoding='utf-8') as f_read:
    data = json.load(f_read)
    print(data)
