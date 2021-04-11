"""
Задание 5
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.
"""


class Warehouse:
    amount = 0              # Количество едениц техники
    total_cost = 0          # Стоимость всей техники
    all_equipment = dict()  # Словарь со всей техникой

    @classmethod
    def increase_amount(cls, equipment, brand, cost):
        """ Добавляет в словарь со всей техникой переданный экземпляр, увеличивает общее количество и общую стоимость
        техники на складе

        :param equipment: str - тип техники
        :param brand: str - бренд
        :param cost: int - стоимость
        :return: Запись в словарь: ["тип_бренд"]: стоимость
        """
        cls.amount += 1
        cls.total_cost += cost
        cls.all_equipment[f"{equipment}_{brand}"] = cost

    @classmethod
    def decrease_amount(cls, key, value):
        """ Удаление из словаря техники, уменьшение количества и стоимости техники на складе

        :param key: str
        :param value: int
        :return:
        """
        cls.amount -= 1
        cls.total_cost -= value
        cls.all_equipment.pop(key)

# Добавление на склад техники без создания экземпляра
    @staticmethod
    def technique_reception_printer(quantity=1):
        """Добавляет принтер на склад

        :param quantity: int - количество принтеров, по умолчанию 1
        :return:
        """
        for p in range(quantity):
            br = input("\nВведите имя бренда принтера: ")  # Имя бренда
            cos = Warehouse.cost_check()  # Цена
            Printer(br, cos)

    @staticmethod
    def technique_reception_scanner(quantity=1):
        """Добавляет сканер на склад

        :param quantity: int - количество сканеров, по умолчанию 1
        :return:
        """
        for s in range(quantity):
            br = input("\nВведите имя бренда сканера: ")
            cos = Warehouse.cost_check()
            Scanner(br, cos)

    @staticmethod
    def technique_reception_xerox(quantity=1):
        """Добавляет ксерокс на склад

        :param quantity: int - количество ксероксов, по умолчанию 1
        :return:
        """
        for x in range(quantity):
            br = input("\nВведите имя бренда ксерокса: ")
            cos = Warehouse.cost_check()
            Xerox(br, cos)

# Проверка ввода цены
    @staticmethod
    def cost_check():
        """ Проверяет и преобразует пользовательский ввод в число

        :return: int
        """
        string = str()
        while type(string) == str:
            try:
                string = int(input("Введите стоимость: "))
            except TypeError:
                print("Некорректный ввод")
                continue
            except ValueError:
                print("Некорректный ввод")
                continue
        return string

# Перемещение вида техники в подразделения
    @classmethod
    def transfer_printer(cls):
        """Запрашивает имя подразделения, куда надо передать принтер и удаляет данные об этой технике со склада

        :return:
        """
        subdivision = input("\nВведите название подразделения, куда надо передать принтер: ")
        for k, v in cls.all_equipment.items():
            if "Принтер" in k:
                print(f"{k} передан в {subdivision}")
                Warehouse.decrease_amount(k, v)
                break
        else:
            print("На складе не найдено принтеров.")

    @classmethod
    def transfer_scanner(cls):
        """Запрашивает имя подразделения, куда надо передать сканер и удаляет данные об этой технике со склада

        :return:
        """
        subdivision = input("\nВведите название подразделения, куда надо передать сканер: ")
        for k, v in cls.all_equipment.items():
            if "Сканер" in k:
                print(f"{k} передан в {subdivision}")
                Warehouse.decrease_amount(k, v)
                break
        else:
            print("На складе не найдено сканеров.")

    @classmethod
    def transfer_xerox(cls):
        """Запрашивает имя подразделения, куда надо передать ксерокс и удаляет данные об этой технике со склада

        :return:
        """
        subdivision = input("\nВведите название подразделения, куда надо передать ксерокс: ")
        for k, v in cls.all_equipment.items():
            if "Ксерокс" in k:
                print(f"{k} передан в {subdivision}")
                Warehouse.decrease_amount(k, v)
                break
        else:
            print("На складе не найдено ксероксов.")


class OfficeEquipment:
    name = "Оргтехника"
    location = None

    def __init__(self, brand, cost):
        self.brand = brand
        self.cost = cost
        print(f"\nДобавлен {self.name}, марки {self.brand}, стоимостью {self.cost}")
        Warehouse.increase_amount(self.name, self.brand, self.cost)  # Передаёт данные о новой технике на склад

    def __str__(self):
        if f"{self.name}_{self.brand}" in Warehouse.all_equipment:  # Если этот экземпляр найден на складе,
            self.location = "склад"                                 # то соответственно записывается.
        else:                                                       # Если нет,
            self.location = "передан в подразделение"               # то запись - передан
        return f"\n{self.name}, под маркой: {self.brand}, по цене: {self.cost}, место: {self.location}"


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


pr = Printer("Canon", 3461)
pr.print_document()

sc = Scanner("HP", 3000)
sc.scan_document()

xer = Xerox("Xerox", 4555)
xer.scan_document()
xer.print_document()

# Вывод словаря с техникой
print(Warehouse.all_equipment)

# Перемещение техники со склада
Warehouse.transfer_printer()
Warehouse.transfer_scanner()
Warehouse.transfer_xerox()

# Добавление принтера без создания экземпляра
Warehouse.technique_reception_printer()

# Вывод словаря с техникой после перемещения и добавления принтера
print(Warehouse.all_equipment)
