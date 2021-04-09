"""
Задание 1
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def_date = "31-12-2020"

    def __init__(self, date_string):
        self.date_string = date_string

    @classmethod
    def convert_to_num(cls, date_to_num=def_date):
        date_to_conv = date_to_num.split('-')
        date_list = list()
        for el in date_to_conv:
            el = int(el)
            date_list.append(el)
        return date_list

    @staticmethod
    def validation(valid_string):
        date_conv = Date.convert_to_num(valid_string)
        year = date_conv[2]
        month = date_conv[1]
        day = date_conv[0]

        # Високосный ли год?
        leap_year = bool
        if year % 4 == 0:
            leap_year = True
        else:
            leap_year = False
        # Месяц
        if month > 12:
            month = 12
        elif month < 1:
            month = 1
        # День
        large_month_list = [1, 3, 5, 7, 8, 10, 12]
        if day < 1:
            day = 1
        elif month == 2:  # февраль
            if leap_year and day > 29:
                day = 29
            elif not leap_year and day > 28:
                day = 28
        elif month in large_month_list:
            if day > 31:
                day = 31
        else:
            if day > 30:
                day = 30

        return day, month, year



date = Date("12-03-1994")
print(f"Через экземпляр класса: {date.validation(date.def_date)}",
      f"Классовый метод, конвертирующий строку в числа: {Date.convert_to_num()}",
      f"Статический метод, исправляет ввод: {Date.validation('32-2-2021')}", sep="\n")
