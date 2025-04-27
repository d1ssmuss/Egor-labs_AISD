"""
Задание на л.р. №6
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования
(алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов
(которое будет сокращать количество переборов)  и целевую функцию для нахождения оптимального  решения.
Вариант 8. В зоопарке К животных. Сформировать все возможные варианты расстановки клеток.
"""

import time
import itertools

# Размеры животных (S - маленький, M - средний, L - большой)
animal_sizes = {
    "лев": "L",
    "тигр": "L",
    "волк": "M",
    "лиса": "M",
    "заяц": "S",
    "антилопа": "M",
    "попугай": "S",
    "змея": "S"
}

def count_size_violations(arrangement, size_to_avoid):
    violations = 0
    for i in range(len(arrangement) - 1):
        if animal_sizes[arrangement[i]] == size_to_avoid and animal_sizes[arrangement[i + 1]] == size_to_avoid:
            violations += 1
    return violations

def find_best_size_arrangement(animals, size_to_avoid):
    best_arrangement = None
    min_violations = float('inf')

    for perm in itertools.permutations(animals):
        violations = count_size_violations(perm, size_to_avoid)
        if violations < min_violations:
            min_violations = violations
            best_arrangement = perm
            if min_violations == 0:  # идеальный вариант
                break

    return best_arrangement, min_violations

try:
    n = int(input("Введите количество животных (<= 8): "))
    if n > 8:
        print("Ваше число > 8. Перезапустите программу!")
    elif n >= 0:
        print("Список животных и их размер:")
        print(animal_sizes)
        size_to_avoid = input("Введите размер, который нужно избегать (S, M, L): ").upper()
        if size_to_avoid not in ["S", "M", "L"]:
            print("Неверный размер. Введите S, M или L.")
        else:
            print(f"Оптимальная расстановка: Нет двух животных размера {size_to_avoid} рядом")
            animals = [input(f"Введите животное №{i + 1}: ") for i in range(n)]
            start_time = time.time()
            best_arrangement, violations = find_best_size_arrangement(animals, size_to_avoid)
            end_time = time.time()

            if violations == 0:
                print(f"Оптимальная расстановка: {best_arrangement}")
            else:
                print("Не найдено оптимальной расстановки!")
            print(f"Время выполнения: {end_time - start_time:.5f} секунд")
    else:
        print("Ошибка: число животных не может быть отрицательным!")
except ValueError:
    print("Ошибка: введите целое число!")
