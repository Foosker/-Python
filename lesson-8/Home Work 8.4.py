"""
Задание 4
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для
каждого типа оргтехники.
"""


class Warehouse:
    amount = 0  # Количество едениц техники
    total_cost = 0

    @classmethod
    def increase_amount(cls, cost):
        cls.amount += 1
        cls.total_cost += cost


class OfficeEquipment:
    name = "Оргтехника"

    def __init__(self, cost):
        self.cost = cost
        print(f"\nДобавлен {self.name}, на сумму {self.cost}")
        Warehouse.increase_amount(self.cost)

    def __str__(self):
        return f"\n{self.name} по цене {self.cost} \n" \
               f"Всего техники: {Warehouse.amount}, на общую стоимость {Warehouse.total_cost}"


class Printer(OfficeEquipment):
    name = "Принтер"

    def print_document(self):
        print(f"\n{self.name} печатает документ")


class Scanner(OfficeEquipment):
    name = "Сканер"

    def scan_document(self):
        print(f"\n{self.name} сканирует документ")


class Xerox(Printer, Scanner):
    name = "Ксерокс"


pr = Printer(34661)
pr.print_document()
print(pr)
sc = Scanner(40000)
sc.scan_document()
print(sc)
xer = Xerox(34555)
xer.scan_document()
xer.print_document()
print(xer)
