"""
Задание 7
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, inp_x, inp_y):
        self.x = inp_x
        self.y = inp_y

    def __str__(self):

        return f"({self.x}+{self.y}j)"

    def __add__(self, other):
        return f"({self.x + other.x}+{self.y + other.y}j)"

    def __mul__(self, other):
        new_x = (self.x * other.x) - (self.y * other.y)
        new_y = (self.x * other.y) + (self.y * other.x)
        return f"({new_x}+{new_y}j)"


x = complex(50, 21)
y = complex(35, 49)

x1 = ComplexNumber(50, 21)
y1 = ComplexNumber(35, 49)

print(f"Пример со встроенной функцией:",
      f"x = {x}, y = {y}",
      f"x + y = {x + y}",
      f"x * y = {x * y}", end="\n")
print(f"Пример с созданным классом:",
      f"x1 = {x1}, y = {y1}",
      f"x1 + y1 = {x1 + y1}",
      f"x1 * y1 = {x1 * y1}")


