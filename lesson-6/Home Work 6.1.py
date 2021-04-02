"""
Задание 6
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый,
зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import time


class TrafficLight:
    __colors = ["Красный", "Жёлтый", "Зелёный"]
    __color_index = 0  # Индекс списка, для color
    __color = __colors[__color_index]

    def __status_update(self):
        """
        Выводит в консоль цвет светофора, обновляет таймер
        """

        self.__color = self.__colors[self.__color_index]
        print(self.__color)

        self.__timer = time()

    def running(self):
        self.__status_update()

        while True:
            if self.__color_index == 0 and time() - self.__timer > 7.0:  # если красный
                self.__color_index += 1
                self.__status_update()

            elif self.__color_index == 1 and time() - self.__timer > 2.0:  # если жёлтый
                self.__color_index += 1
                self.__status_update()

            elif self.__color_index == 2 and time() - self.__timer > 5.0:  # если зелёный
                self.__color_index = 0
                self.__status_update()


light = TrafficLight()
light.running()
