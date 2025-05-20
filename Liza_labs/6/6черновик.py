"""
Задание на л.р. №6
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования
(алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов
(которое будет сокращать количество переборов)  и целевую функцию для нахождения оптимального  решения.
Вариант 8. В зоопарке К животных. Сформировать все возможные варианты расстановки клеток.
"""


import timeit
import itertools


def generate_permutations_pythonic(items):
    return list(itertools.permutations(items))

def generate_permutations_algorithmic(animals):
    def permute(prefix, remaining):
        if len(remaining) == 0:
            permutations.append(prefix)
        else:
            for i in range(len(remaining)):
                new_prefix = prefix + [remaining[i]]
                new_remaining = remaining[:i] + remaining[i+1:]
                permute(new_prefix, new_remaining)

    permutations = []
    permute([], animals)
    return permutations

def main():
    # Ввод животных и их размер
    number_of_animals = int(input("Введите количество животных: "))
    animals = [input(f"Животное №{i}: ") for i in range(1, number_of_animals + 1)]
    size_info = {}
    size_values = {'s': 1, 'm': 2, 'l': 3}
    if not animals:
        print("Должен быть хотя бы 1 зверь!")
        return
    print("\nУкажите размер каждого животного (только латинские буквы: s, m или l):")

    for animal in animals:
        while True:
            size = input(f"Размер {animal} = ")
            if size in size_values:
                size_info[animal] = size
                break
            else:
                print("Ошибка! Введите s, m или l (латинскими буквами).")
    size_info = {k: v for k, v in size_info.items() if v != 's'}
    animals = [i for i, v in size_info.items()]
    # print(size_info, animals)
    time_pythonic = timeit.timeit(lambda: generate_permutations_pythonic(animals), number=10000)
    time_algorithmic = timeit.timeit(lambda: generate_permutations_algorithmic(animals), number=1000)
    print(f"\nВремя выполнения (питонический способ): {time_pythonic:.5f} секунд")
    print(f"Время выполнения (алгоритмический способ): {time_algorithmic:.5f} секунд")
    # print(timeit.timeit(generate_permutations_algorithmic(animals)))
    # print(animals, size_info)
    # ['панда', 'заяц'] {'панда': 'm', 'заяц': 'l'}

    # Примеры расчёта рейтинга для всех животных
    print("Примеры расчёта рейтинга для каждого животного:")
    for idx, animal in enumerate(animals):
        animal_size = size_values[size_info[animal]]
        rating = idx * animal_size
        print(f"{animal}: (№ позиции) {idx} * (Размер животного {size_info[animal]}) {animal_size} = {rating} очков")
    # Создаю словарь рейтингов
    ratings = {animal: size_values[size_info[animal]] * idx for idx, animal in enumerate(animals)}

    print("\n-- Рейтинг животных --")
    for key, value in ratings.items():
        print("{0}: {1} очков".format(key, value))

if __name__ == "__main__":
    main()
