# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен
# извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
# структуры на реальных данных.

class Data:

    data = ''
    data_dict = {
        'day': 0,
        'month': 0,
        'year': 0
    }

    def __init__(self, data):
        Data.data = data

    @classmethod
    def convert_to_int(cls):
        cls.value_list = cls.data.split('-')
        i = 0
        for cls.key, cls.value in cls.data_dict.items():
            cls.data_dict[cls.key] = int(cls.value_list[i])
            i += 1
        return cls.data_dict

    @staticmethod
    def check_date(data_dict):
        if data_dict['day'] in range(1, 32) and data_dict['month'] \
                in range(1, 13) and data_dict['year'] in range(1900, 2050):
            print('Дата введена корректно')
        else:
            print('Дата введена не корректно')


a = Data('31-12-2000')
print(Data.convert_to_int())
Data.check_date(Data.data_dict)
