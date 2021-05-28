"""
Задание 3
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить
работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение
должен контролировать типы данных элементов списка.
"""

curr_list = [1, 2, 3, 52, "3fe", 5, 9, 7, 0, 4, "Ж12"]


class OwnTypeNumError(Exception):
    num = str()
    class_list = list()

    @classmethod
    def __init__(cls, inp):
        """При передаче нового аргумента проверяет его тип

        :param inp: str
        """
        for i in range(len(inp)):           # На случай если переданная строка длинее одного символа
            if chr(48) < inp[i] < chr(58):  # если элемент от 0 до 9,
                continue                    # продолжаем перебор строки.
            else:
                print("Введено не число!")  # Иначе, выводим сообщение и прекращаем цикл.
                break
        else:                                # Если цикл завершился сам, то введёная строка состоит из чисел
            cls.class_list.append(int(inp))  # и число добавляется в список.

    @classmethod
    def num_list_check(cls, num_list):
        """Удаляет из переданного списка всё кроме int

        :param num_list: list
        :return: -
        """
        cls.class_list = num_list
        for el in cls.class_list:
            if type(el) == int:  # Если тип элемента списка - число,
                continue         # то оставляем его в списке.
            else:
                cls.class_list.remove(el) # Иначе - удаляем.


user_input = str()  # Строка куда будет записываться пользовательский ввод
OwnTypeNumError.num_list_check(curr_list)  # Передача списка в класс
while user_input != "stop":
    user_input = input('Введите число или "stop" для остановки: ')
    OwnTypeNumError(user_input)  # Передача нового аргумента в класс

print(OwnTypeNumError.class_list)  # Вывод списка в конце работы цикла
