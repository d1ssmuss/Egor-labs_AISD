"""
Сипатов Егор ИСТбд-23
Задание на л.р. №6
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение
на характеристики объектов (которое будет сокращать количество переборов)
и целевую функцию для нахождения оптимального  решения.
Вариант 23. Сформируйте разные варианты распределения Т предметов между К людьми.
"""
import time
from itertools import product

def distribute_items_algorithmic(T, K):
    if K == 0:
        return [[]] if T == 0 else []

    result = []
    for i in range(T + 1):
        for distribution in distribute_items_algorithmic(T - i, K - 1):
            result.append([i] + distribution)
    return result


# Переменные
T = int(input("Кол-во предметов (<= 10): "))  # Количество предметов
K = int(input("Кол-во людей (<= 10): "))  # Количество людей

start_time = time.time()
result_algorithmic = distribute_items_algorithmic(T, K)
end_time = time.time()

print("Алгоритмический подход:")
print(result_algorithmic)
print(f"Время выполнения: {end_time - start_time:.6f} секунд")


def distribute_items_functional(T, K):
    # Все возможные комбинации распределения предметов
    return [distribution for distribution in product(range(T + 1), repeat=K) if sum(distribution) == T]

start_time = time.time()
result_functional = distribute_items_functional(T, K)
end_time = time.time()

print("Функциональный подход:")
print(result_functional)
print(f"Время выполнения: {end_time - start_time:.6f} секунд")
print()
print("Усложнённая часть")
print("Ограничение: Пусть каждый человек может получить не более max_items предметов.")
print("Целевая функция\nРавномерное распределение предметов между людьми, минимизируя разницу между максимальным и минимальным количеством предметов, полученных каждым человеком.")

def distribute_items_with_constraints(T, K, max_items):
    if K == 0:
        return [[]] if T == 0 else []

    result = []
    for i in range(min(T, max_items) + 1):
        for distribution in distribute_items_with_constraints(T - i, K - 1, max_items):
            result.append([i] + distribution)
    return result


def optimal_distribution(T, K, max_items):
    try:
        distributions = distribute_items_with_constraints(T, K, max_items)
        optimal = min(distributions, key=lambda x: max(x) - min(x))
        print("Оптимальное распределение с ограничениями:")
        return optimal
    except:
        return "Параметр max_items должен быть больше или равно, чем (кол-во людей / кол-во вещей) + 1"


max_items = int(input("Max_items: ")) # Максимальное количество предметов для каждого человека
optimal_result = optimal_distribution(T, K, max_items)

print(optimal_result)