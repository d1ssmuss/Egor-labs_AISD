# лев, тигр, медведь, волк, лиса, заяц, ёж, змея, кот, собака
"""
Пример:
лев: l
тигр: l
медведь: l
волк: m
лиса: s
заяц: s
ёж: s
змея: s
кот: s
собака: m
"""
"""
Задание на л.р. №6
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования
(алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов
(которое будет сокращать количество переборов)  и целевую функцию для нахождения оптимального  решения.
Вариант 8. В зоопарке К животных. Сформировать все возможные варианты расстановки клеток.
"""
# Усложнённый вариант

import time
import itertools


def generate_permutations_pythonic(items):
    return list(itertools.permutations(items))


def filter_permutations(permutations, size_info, required_small):
    return [perm for perm in permutations
            if sum(1 for animal in perm if size_info[animal] == 's') == required_small]


def calculate_rating(permutation, size_values, exclude_size):
    rating = 0
    for position, animal in enumerate(permutation, start=1):
        size = size_info[animal]
        if size != exclude_size:
            rating += position * size_values[size]
    return rating


def main():
    print("Программа расстановки клеток в зоопарке")
    print("Введите животных через запятую:")
    animals = [a.strip() for a in input().split(',')]

    if not animals:
        print("Должен быть хотя бы 1 зверь!")
        return

    global size_info
    size_info = {}
    size_values = {'s': 1, 'm': 2, 'l': 3}
    print("\nУкажите размер каждого животного (только латинские буквы: s, m или l):")
    for animal in animals:
        while True:
            size = input(f"{animal}: ").strip().lower()
            if size in size_values:
                size_info[animal] = size
                break
            print("Ошибка! Введите s, m или l (латинскими буквами).")

    total_small = sum(1 for a in animals if size_info[a] == 's')
    print(f"\nОбнаружено {total_small} животных с размером 's'")
    required_small = int(input(f"Сколько животных с размером 's' должно быть в расстановке (0-{total_small})? "))

    if required_small < 0 or required_small > total_small:
        print("Некорректное количество!")
        return

    print(f"\nГенерируем перестановки с {required_small} маленькими животными...")

    start_time = time.time()
    all_perms = generate_permutations_pythonic(animals)
    gen_time = time.time() - start_time
    print(f"Всего перестановок: {len(all_perms)} (время: {gen_time:.2f} сек)")

    start_time = time.time()
    filtered_perms = filter_permutations(all_perms, size_info, required_small)
    filter_time = time.time() - start_time
    print(f"После фильтрации: {len(filtered_perms)} (время: {filter_time:.2f} сек)")

    if not filtered_perms:
        print("Нет подходящих перестановок!")
        return

    print("\nКакой размер исключить из расчета рейтинга? (s/m/l):")
    while True:
        exclude = input().strip().lower()
        if exclude in ['s', 'm', 'l']:
            break
        print("Ошибка! Введите s, m или l")

    print("\nТоп-10 лучших расстановок:")
    start_time = time.time()

    rated_perms = [(perm, calculate_rating(perm, size_values, exclude))
                   for perm in filtered_perms]

    rated_perms.sort(key=lambda x: x[1])

    sort_time = time.time() - start_time
    print(f"Сортировка заняла {sort_time:.2f} сек\n")

    for i, (perm, rating) in enumerate(rated_perms[:10], 1):
        print(f"{i}. Рейтинг: {rating}")
        print("   Расстановка:", ", ".join(perm))
        print("   Детали:")

        details = []
        for pos, animal in enumerate(perm, 1):
            size = size_info[animal]
            if size != exclude:
                val = pos * size_values[size]
                details.append(f"{animal}({size}):{pos}*{size_values[size]}={val}")

        print("   " + " + ".join(details), "=", rating, end="\n\n")


if __name__ == "__main__":
    size_info = {}
    main()
