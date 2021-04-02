"""
Задание 3
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
"""


class Worker:

    dict_income = {"Wage": 20000, "Bonus": 8000}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = self.dict_income["Wage"] + self.dict_income["Bonus"]


class Position(Worker):

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income


worker_1 = Position("Иван", "Факов", "Землекоп")

print("Проверка значений атрибутов",
      f"Имя: {worker_1.name}",
      f"Фамилия: {worker_1.surname}",
      f"Должность: {worker_1.position}", sep="\n")

print("\nМетоды",
      f"Полное имя: {worker_1.get_full_name()}",
      f"Доход: {worker_1.get_total_income()}", sep="\n")
