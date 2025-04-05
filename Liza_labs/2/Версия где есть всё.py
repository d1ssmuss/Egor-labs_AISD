"""
Лабораторная работа №2
Написать программу, решающую задачу из 1 лабораторной работы (в соответствии со своим вариантом) со следующими изменениями:
1.  Входной файл является обыкновенным (т.е. нет требования на «бесконечность» файла);
2.  Распознавание и обработку делать  через регулярные выражения;
3.  В вариантах, где есть параметр (например К), допускается его заменить на любое число;
4.  Все остальные требования соответствуют варианту задания лабораторной работы №1.
Вариант 8.
Натуральные числа. Обрабатывает числа по десяткам.
Выводит на экран очередной десяток, если в нем есть более(>) К одинаковых чисел.
В каждом десятке при выводе последнее число выводится прописью
"""
import re

def checking_for_identical_numbers(number):
    return True if max(map(str(number).count, str(number))) > K else False

def process_number(file):
    list_numbers = re.findall(r'\d+', open(file, encoding='utf-8').read())
    print("Список чисел:")
    numbers_int = [int(i) for i in list_numbers]
    print(numbers_int)
    dozens_list = [int(i) // 10 for i in list_numbers]
    print("Список десятков чисел")
    print(dozens_list)
    if not any(checking_for_identical_numbers(dozens_list[i]) for i in range(len(dozens_list))): print("Программа не нашла чисел, удовлетворяющие условию (выводит на экран очередной десяток, если в нем есть более К одинаковых чисел.")
    else:
        for i in range(len(dozens_list)):
            if checking_for_identical_numbers(dozens_list[i]): print(f"Число: {dozens_list[i]}, последняя цифра: {["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"][(int(str(dozens_list[i])[-1]))]}")

if __name__ == "__main__":
    try:
        K = int(input("Введите число K, которое >= 0: "))
        if K >= 0: process_number("test.txt")
        else: print("Число K должно быть больше или равно 0. Перезапустите программу!")
    except: print("Некорректные данные. Перезапустите программу!")
