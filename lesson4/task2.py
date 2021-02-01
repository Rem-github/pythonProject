# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# два решения через цикл и через генератор

user_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# вариант без генератора

user_list2 = []
for i in range(len(user_list)-1):
    if user_list[i+1] > user_list[i]:
        user_list2.append(user_list[i+1])
print(user_list2)

# вариант с генератором

target_list = [user_list[i+1] for i in range(len(user_list)-1) if user_list[i+1] > user_list[i]]
print(target_list)
