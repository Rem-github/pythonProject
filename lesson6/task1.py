# Создать класс TrafficLight (светофор).

# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.


from time import sleep, time

class TrafficLight:

    __color = 'red'
    time_run = time()

    def running(self):

        if self.__color == 'red' and time() > self.time_run + 7:
            self.__color = 'yellow'
        elif self.__color == 'yellow' and time() > self.time_run + 9:
            self.__color = 'green'
        elif self.__color == 'green' and time() > self.time_run + 13:
            self.__color = 'red'
            self.time_run = time()
        return self.__color


a = TrafficLight()
for i in range(30):
    print(a.running())
    sleep(1)


