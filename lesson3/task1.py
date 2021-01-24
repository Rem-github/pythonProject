
# Эта программа принимает в функцию два числа и делит их

def make_float(x):
        try:
            x = float(x)
            return x
        except ValueError:
            print("Необходимо вводить числа")

def division_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("На ноль делить нельзя")

a = make_float(input("Введите число a: "))
if a != None:
    b = make_float(input("Введите число b: "))
    if b != None:
        c = division_numbers(a, b)
        if c != None:
            print(f'Полученное число: {c:.2f}')
