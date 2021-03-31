"""
Задание 6
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
"""


def found_key(string):
    """
    Находит слова для ключа

    :param string: строка
    :return: слово
    """
    for i in range(len(string)):
        if not string[i].isalpha():
            return string[:i]


def found_nums(string):
    """
    Находит цифры в строке и складывает

    :param string: строка
    :return: сумма всех чисел
    """
    result = 0
    number = ""
    for i in range(len(string)):
        if string[i].isdigit():  # Если элемент строки цифра,
            number += string[i]  # то записывает в строку number.

        elif not number:  # Если элемент не цифра и number пустая,
            continue      # то переходим к следующей итерации.

        elif number:              # Если элемент не цифра, а number не пустая,
            number = int(number)  # переводим number в тип int,
            result += number      # прибавляем получившееся число к результату,
            number = ""           # и обнуляем number
    return result


result_dict = dict()

with open("text_file_6.txt", "r", encoding="UTF-8") as file:
    for line in file.readlines():
        result_dict[found_key(line)] = found_nums(line)  # добавление пары ключ-значение

print(result_dict)
