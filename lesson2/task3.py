
# Эта программа определяет время года по номеру месяца через странный список

strange_list = [[1, 2, 12],'зима',[3, 4, 5],'весна',[6, 7, 8],'лето',[9, 10, 11],'осень']
month = int(input("Введите месяц цифрой от 1 до 12:"))

for i in range(len(strange_list)):
    if type(strange_list[i]) != str and month in strange_list[i]:
            print(f'Это время года: {strange_list[i+1]}')
            break

# Эта программа определяет время года по номеру месяца с помощью словаря

season_dict = {'зима': [1, 2, 12], 'весна':[3, 4, 5], 'лето':[6, 7, 8], 'осень':[9, 10, 11]}
month = int(input("Введите месяц цифрой от 1 до 12:"))

for key in season_dict:
    if month in season_dict[key]:
        print(f'Это время года: {key}')
