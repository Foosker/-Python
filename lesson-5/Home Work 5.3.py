"""
Задание 3
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
дохода сотрудников.
"""


def find_numbers(string):
    """
    Находит зарплату в строке

    :param string: принимает всю строку файла
    :return: переводится в формат float
    """
    for i in range(len(string)):
        if string[i].isdigit():
            return float(string[i:])


def find_surname(string):
    """
    Выделяет из строки фамилию

    :param string: вся строка
    :return: возвращает строку
    """
    for i in range(len(string)):
        if string[i].isspace():
            return string[:i]


amount_of_salarys = 0    # сумма зарплат га всех сотрудников
number_of_employees = 0  # число сотрудников

with open("text_file_3.txt", "r", encoding="UTF-8") as file:
    print("\nСотрудники, с окладом меньше 20 тыс: ", end="")
    for line in file.readlines():
        salary = find_numbers(line)

        amount_of_salarys += salary
        number_of_employees += 1

        if salary < 20000:
            print(find_surname(line), end=" ")

print(f"\nСредняя зарплата: {round(amount_of_salarys / number_of_employees, 2)}")