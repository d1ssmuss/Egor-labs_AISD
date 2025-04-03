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
    number_and_count = {str(i): 0 for i in range(10)}  # Создаем словарь с ключами от 0 до 9
    for digit in str(number): number_and_count[digit] += 1  # Увеличиваем счетчик для соответствующей цифры
    return max(number_and_count.values()) > K  # Проверяем, больше ли максимальное значение K


def process_number(file, K):
    if not any(checking_for_identical_numbers([int(i) // 10 for i in re.findall(r'\d+', open(file, encoding='utf-8').read())][i]) for i in range(len([int(i) // 10 for i in re.findall(r'\d+', open(file, encoding='utf-8').read())]))):
        print("Программа не нашла чисел, удовлетворяющие условию (выводит на экран очередной десяток, если в нем есть более К одинаковых чисел.")
    else:
        for i in range(len([int(i) // 10 for i in re.findall(r'\d+', open(file, encoding='utf-8').read())])):
            if checking_for_identical_numbers([int(i) // 10 for i in re.findall(r'\d+', open(file, encoding='utf-8').read())][i]): print(f"Число: {[int(i) // 10 for i in re.findall(r'\d+', open(file, encoding='utf-8').read())][i]}, последняя цифра: {["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"][(int(str([int(i) // 10 for i in re.findall(r'\d+', open(file, encoding='utf-8').read())][i])[-1]))]}")

if __name__ == "__main__":
    try:
        K = int(input("Введите число K, которое >= 0: "))
        if K >= 0: process_number("test.txt", K)
        else: print("Число K должно быть больше или равно 0. Перезапустите программу!")
    except: print("Некорректные данные. Перезапустите программу!")
