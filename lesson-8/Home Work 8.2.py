"""
Задание 2
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых
пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.
"""


class OwnZeroDivError(Exception):
    def __str__(self):
        return "Нельзя делить на ноль"


inp_data = input("Введите пример с делением: ")

dividend = str  # Делимое
divider = str   # Делитель

for i in range(len(inp_data)):  # Перебор пользовательского ввода
    if inp_data[i] != r'/':
        continue
    dividend = inp_data[:i]   # Делимое то, что до символа "/",
    divider = inp_data[i+1:]  # делитель - после
    break

try:
    dividend, divider = int(dividend), int(divider)  # Конвертация в целое число
    if divider == 0:
        raise OwnZeroDivError
except ValueError:  # Если невозможно конвертировать
    print("Некоректный ввод!")
except TypeError:  # Если в строке ввода не было знака "/", то обе переменные пустые
    print("Некоректный ввод!")
except OwnZeroDivError as err:
    print(err)
else:
    print(round(dividend / divider, 2))
