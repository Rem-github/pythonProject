
# Эта программа вписывает число пользователя в невозрастающий список натуральных чисел
my_list = [9, 8, 6, 4, 2, 2]

user_number = 0
while(user_number < 1):
    try:
        user_number = int(input("Введите новый элемент рейтинга (натуральное число): "))
    except ValueError:
        print("Введите корректное число")

if user_number > my_list[0]:
    my_list.insert(0,user_number)
elif user_number < my_list[-1]:
    my_list.insert(len(my_list), user_number)
else:
    my_list.reverse()
    for num in range(len(my_list)):
        if user_number <= my_list[num]:
            my_list.insert(num, user_number)
            break
    my_list.reverse()
print(my_list)
