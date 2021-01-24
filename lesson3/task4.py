
# Эта программа возводит число в степень с помощью разных функций

def my_func(x, y):
    if y >= 0:
        number = x**y
    else:
        number = 1/(x**abs(y))
    return number

def my_func_hard(x, y):
    number = 1
    if y >= 0:
        for i in range(abs(y)):
            number = number * x
    else:
        for i in range(abs(y)):
            number = number * x
        number = 1 / number
    return number


x = 0.5
y = -5

print(my_func(x, y))
print(my_func_hard(x, y))
