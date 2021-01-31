
# Эта программа принимает в функцию два числа и делит их
# Добавлена функция которая ждет от пользователя только число типа float

def input_float():
        x = ''
        while('.' not in x):
            x = input()
            try:
                float(x)
            except:
                x = ''
        return float(x)

def division_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("На ноль делить нельзя")

print('Введите первое число типа float:')
a = input_float()
print('Введите второе число типа float:')
b = input_float()
c = division_numbers(a, b)
if c != None:
    print(f'Полученное число: {c:.2f}')
