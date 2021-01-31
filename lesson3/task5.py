
# Эта программа получает от пользователя список чисел через пробел и суммирует их
# Если условный знак "-" будет поставлен в не корректной строке (с символами, дополнительными пробелами),
# то числа в этой строке программа не посчитает

def sum_numbers(user_string):
    user_list = user_string.split(' ')
    sum = 0
    try:
        for i in user_list:
            sum = sum + float(i)
        return sum
    except ValueError:
        return 0


def check_spec_char(user_string):
    return '-' in user_string

def cut_string(user_string):
    cut_string = ''
    index_spec = user_string.index('-')
    if user_string[index_spec-1] == ' ':
        index_spec = index_spec - 1
    for i in range(index_spec):
        cut_string = cut_string + user_string[i]
    return cut_string


sum_all_numbers = 0

while(True):
    print('Для выхода введите знак "-" без пробелов или через 1 пробел от последнего числа')
    user_string = input ("Введите строку чисел разделенных одним пробелом:")
    if check_spec_char(user_string) == True:
        sum_all_numbers += sum_numbers(cut_string(user_string))
        print(f"Итоговая сумма: {sum_all_numbers}")
        break
    else:
        sum_all_numbers += sum_numbers(user_string)
        print(f'Получена сумма: {sum_all_numbers}')


