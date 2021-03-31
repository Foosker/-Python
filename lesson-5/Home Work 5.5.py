"""
Задание 5
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint

# Создание файла и запись десяти случайных чисел через пробел
with open("text_file_5.txt", "w") as file:
    file.writelines(str(randint(3, 20)) + " " for i in range(10))

with open("text_file_5.txt", "r") as file:
    num_list = file.readline().split()       # Чтение, переведение строки из файла в формат списка
    num_list = [int(el) for el in num_list]  # Перевод элементов списка в формат чисел с помощью генератора
    print(f"Сумма всех чисел из файла: {sum(num_list)}")
