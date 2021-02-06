# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
# метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        print('Машина поворачивает')

    def show_speed(self):
        print(f'Скорость автомобиля: {self.speed}')

    def show_info(self):
        print(f'Скорость: {self.speed}')
        print(f'Цвет: {self.color}')
        print(f'Название: {self.name}')
        if self.is_police == False:
            print('Это не полицейский автомобиль')
        else:
            print('Это полицейский автомобиль')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Ваша скорость {self.speed} Вы превышаете скорость')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Ваша скорость {self.speed} Вы превышаете скорость')

class PoliceCar(Car):
    pass


autobus = WorkCar(50, 'white', 'Mercedes', False)
autobus.go()
autobus.show_info()
autobus.show_speed()


ladasedan = PoliceCar(100500, 'Baklazhan', 'Priora', True)
ladasedan.show_info()
ladasedan.show_speed()
ladasedan.stop()

smart = TownCar(80, 'red', 'MiniCooper', False)
smart.show_info()
smart.show_speed()
smart.turn()
