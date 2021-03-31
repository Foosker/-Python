"""
Задание 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""
list_for_replace = ["Один", "Два", "Три", "Четыре"]


def text_raplacement(string, ind):
    """
    Заменяет английский текст на русский по инлдексу

    :param string: строка с анг. текстом
    :param ind: индекс элемента
    :return: русский текст + остальная часть строки
    """
    for i in range(len(string)):
        if not string[i].isalpha():
            return list_for_replace[ind] + string[i:]


# создание списка с англ. текстом
with open("text_file_4.txt", "r", encoding="UTF-8") as eng_file:
    list_eng = eng_file.readlines()

# замещение англ. текста и перемещение в другой список
list_rus = list()
for i in range(len(list_eng)):
    list_rus.append(text_raplacement(list_eng[i], i))

# создание нового файла и запись переведённого текста
with open("text_file_4.1.txt", "w", encoding="UTF-8") as rus_file:
    rus_file.writelines(list_rus)
