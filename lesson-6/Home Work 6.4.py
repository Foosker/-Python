"""
Задание 4
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""
import random

class Car:
    colors = ["белого цвета", "красного цвета", "серого цвета", "синего цвета", "зелёного цвета", "жёлтого цвета"]
    speed = 0
    color = None
    name = None
    is_police = False

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self, direction):
        print(f"{self.name} повернула {direction}")

    def show_speed(self):
        print(f"{self.name} едет на скорости: {self.speed}")


class TownCar(Car):
    name = "Городская машина"

    def show_speed(self):
        print(f"{self.name} едет на скорости: {self.speed}")
        if self.speed > 60:
            print(f"{self.name} превысила допустимую скорость!")


class SportCar(Car):
    name = "Спортивная машина"


class WorkCar(Car):
    name = "Рабочая машина"

    def show_speed(self):
        print(f"{self.name} едет на скорости: {self.speed}")
        if self.speed > 40:
            print(f"{self.name} превысила допустимую скорость!")


class PoliceCar(Car):
    name = "Полицейская машина"
    is_police = True


cars = list()

[town_car, sport_car, work_car, police_car] = TownCar(), SportCar(), WorkCar(), PoliceCar()

cars.extend([town_car, sport_car, work_car, police_car])

for car in cars:
    # Присваивание и вывод цвета
    car.color = random.choice(car.colors)
    print(f"{car.name} {car.color}")
    # Движение машины и скорость
    car.speed = random.randint(41, 80)
    car.go()
    car.show_speed()
    car.turn(random.choice(["влево", "вправо"]))
    car.stop()
    print()
