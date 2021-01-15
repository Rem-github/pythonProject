
number = input("Введите целое число: ")
maxNumber = 0
i = 0
while (i < len(number)):
    if maxNumber < int(number[i]):
        maxNumber = int(number[i])
    i += 1
print (f"Максимальное число: {maxNumber}")