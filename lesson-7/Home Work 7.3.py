"""
Задание 3
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его
конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть
реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять увеличение,
 уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
"""


class Cell:
    def __init__(self, cellule):
        self.cellule = cellule

    def __add__(self, other):
        return Cell(self.cellule + other.cellule)

    def __sub__(self, other):
        if self.cellule - other.cellule > 0:
            return Cell(self.cellule - other.cellule)
        else:
            print("При вычитании количество ячеек меньше нуля или равняется ему")
            return Cell(0)

    def __mul__(self, other):
        return Cell(self.cellule * other.cellule)

    def __truediv__(self, other):
        return Cell(self.cellule // other.cellule)

    def make_order(self, row):
        _result = str()
        for c in range(1, self.cellule + 1):
            _result += "*"
            if c % row == 0:
                _result += "\n"
        print(_result + "\n")


print("Первая клетка (ряд 5):")
cell1 = Cell(9)
cell1.make_order(5)
print("Вторая клетка (ряд 4):")
cell2 = Cell(6)
cell2.make_order(4)
print("Суммирование (ряд 6):")
cell3 = cell1 + cell2
cell3.make_order(6)
print("Вычитание, результат больше нуля (ряд 3):")
cell4 = cell3 - cell1
cell4.make_order(3)
print("Вычитание, результат меньше либо равняется нулю:")
cell5 = cell4 - cell2
cell5.make_order(1)
print(f"Умножение (ряд 15):")
cell6 = cell2 * cell4
cell6.make_order(15)
print("Деление (ряд 1):")
cell7 = cell6 / cell3
cell7.make_order(1)


