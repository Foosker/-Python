"""
Задание 2
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""


with open("text_file_2.txt", "r") as file:
    content = file.readlines()
    print(f"\nКоличество строк всего: {len(content)}\n")
    string_counter = 1
    for string in content:
        print(f"Количество слов в {string_counter}-й строке: {len(string.split())}")
        string_counter += 1
