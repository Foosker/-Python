"""
Задание 1
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


with open("text_file_1.txt", "w") as text_file:
    while True:
        user_input = input("Введите строку: ")
        if user_input:
            text_file.write(f"{user_input}\n")
        else:
            break
