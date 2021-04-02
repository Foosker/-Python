"""
Задание 2
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта
для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    def __init__(self, _length, _width):
        self.__length = _length
        self.__width = _width
        self.__mass_of_one_meter = 25  # масса на 1 кв.м.

    def total_mass_calculation(self, canvas_thickness):
        result = self.__length * self.__width * self.__mass_of_one_meter * canvas_thickness
        if result % 1000 == 0:                # если число большое,
            return str(result / 1000) + " т"  # то округляем до тонн,
        else:                                 # иначе
            return str(result) + " кг"        # результат в килограммах


high = Road(20, 5000)
print(high.total_mass_calculation(canvas_thickness=5))
