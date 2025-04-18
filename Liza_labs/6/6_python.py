"""
Задание на л.р. №6
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования
(алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов
(которое будет сокращать количество переборов)  и целевую функцию для нахождения оптимального  решения.
Вариант 8. В зоопарке К животных. Сформировать все возможные варианты расстановки клеток.
"""
# Подход с помощью функций питона

import time
import itertools


def generate_permutations_pythonic(animals):
    return list(itertools.permutations(animals))

# Пример использования
try:
    n = int(input("Введите количество животных: "))
    if n >= 0:
        animals = [input(f"Введите животное {i + 1}: ") for i in range(n)]
        start_time = time.time()
        pythonic_permutations = generate_permutations_pythonic(animals)
        end_time = time.time()
        print(f"Время подхода с помощью функций питона: {end_time - start_time} секунд")
        print("Все возможные варианты: ")
        for i in pythonic_permutations:
            print(i)
        print(f"Количество вариантов расстановки клеток : {len(pythonic_permutations)}")
    else:
        print("Вы ввели отрицательное число. Пожалуйста, перезапустите программу")
except:
    print("Некорректный ввод данных! Пожалуйста, перезапустите программу!")
