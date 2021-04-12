"""
Задание 1
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц)
Результатом сложения должна быть новая матрица.
"""


class Matrix:
    def __init__(self, matrix):
        self._matrix = matrix

    def __str__(self):
        string = str()
        for row in self._matrix:
            for col in row:
                string += str(col) + " "
            string += "\n"
        return string

    def __getitem__(self, item):
        try:
            return self._matrix[item]
        except IndexError:
            return 0

    def __add__(self, other):
        result = str()
        for i in range(len(self._matrix)):
            for j in range(len(self._matrix[i])):
                result += str(self._matrix[i][j] + other[i][j])
                result += " "
            result += "\n"
        return result

"""
matr1 = Matrix([[1, 2], [4, 6], [8, 9]])
matr2 = Matrix([[2, 2], [4, 5], [7, 9]])
"""
"""
matr1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matr2 = Matrix([[2, 2, 3], [4, 5, 6], [7, 8, 9]])
"""

matr1 = Matrix([[1, 2, 3, 4], [4, 8, 5, 6], [10, 7, 8, 9]])
matr2 = Matrix([[2, 2, 3, 6], [1, 4, 5, 6], [7, 8, 2, 9]])

print(f"Первая матрица:\n{matr1}")
print(f"Вторая матрица:\n{matr2}")
print(f"Результат сложения:\n{matr1 + matr2}")
