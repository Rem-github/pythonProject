
# Эта программа принимает в функцию три аргумента и выводит сумму наибольших двух

def my_func(a, b, c):
    temp_list = sorted([a, b, c], reverse=True)
    return temp_list[0] + temp_list[1]

a=-2
b=4
c=-5

print(my_func(a, b, c))
