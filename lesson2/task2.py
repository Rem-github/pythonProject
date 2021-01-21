
# Эта программа выводит список, меняя соседние элементы местами

list_length = int(input("Сколько элементов списка вы хотите ввести?: "))
user_list = []
changed_list = []
for i in range(0,list_length):
    user_list.append(input(f"Введите {i+1}-й элемент: "))

print(f"Получен список: {user_list}")
pos = 0
while (pos < list_length):
    if pos + 1 < list_length:
        changed_list.append(user_list[pos+1])
        changed_list.append(user_list[pos])
    else:
        changed_list.append(user_list[pos])
    pos +=2
print(f"Измененный список: {changed_list}")

