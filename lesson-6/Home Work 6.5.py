"""
Задание 5
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
описанный метод для каждого экземпляра.
"""

class Stationery:
    title = "Канцелярская принадлежность"

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    title = "Ручка"

    def draw(self):
        print(f"{self.title} пишет")


class Pencil(Stationery):
    title = "Карандаш"

    def draw(self):
        print(f"{self.title} штрихует")


class Handle(Stationery):
    title = "Маркер"

    def draw(self):
        print(f"{self.title} чертит")


stationery, pen, pencil, handle = Stationery(), Pen(), Pencil(), Handle()

stationery_list = [stationery, pen, pencil, handle]

for el in stationery_list:
    el.draw()