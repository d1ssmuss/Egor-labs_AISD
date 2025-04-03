"""
Лабораторная работа №1
Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом, читающимся поблочно),
распознает, преобразует и выводит на экран лексемы по определенному правилу.
Лексемы разделены пробелами. Преобразование делать по возможности через словарь.
Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.
Регулярные выражения использовать нельзя.
Вариант 8.
Натуральные числа. Обрабатывает числа по десяткам.
Выводит на экран очередной десяток, если в нем есть более(>) К одинаковых чисел.
В каждом десятке при выводе последнее число выводится прописью
"""
import re

def checking_for_identical_numbers(number):
    number_and_count = [0] * 10
    for i in str(number):
        number_and_count[int(i)] += 1
    return True if max(number_and_count) > K else False


def process_number(file, K):
    """Обработка чисел из файла"""
    a = open(file, encoding='utf-8').read()
    # print('a', a)
    list_numbers = re.findall(r'\d+', a)
    print('l', list_numbers)

    print("Список чисел:")
    numbers_int = [int(i) for i in list_numbers]
    print(numbers_int)

    # Обработка по десяткам
    # dozens - десятки

    dozens_list = [int(i) // 10 for i in list_numbers]
    print("Список десятков чисел")
    print(dozens_list)

    words = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]

    if not any(checking_for_identical_numbers(dozens_list[i]) for i in range(len(dozens_list))):
        print("Программа не нашла чисел, удовлетворяющие условию (выводит на экран очередной десяток, если в нем есть более К одинаковых чисел.")
    else:
        for i in range(len(dozens_list)):
            if checking_for_identical_numbers(dozens_list[i]):
                print(f"Число: {dozens_list[i]}, последняя цифра: {words[(int(str(dozens_list[i])[-1]))]}")


if __name__ == "__main__":
    try:
        K = int(input("Введите число K, которое >= 0: "))
        if K >= 0:
            file = "test.txt"
            print(f"-- Результат вычисления --")
            process_number(file, K)
        else:
            print("Число K должно быть больше или равно 0. Перезапустите программу!")
    except:
        print("Некорректные данные. Перезапустите программу!")
