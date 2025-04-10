"""
Задание на л.р. №6
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования
(алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов
(которое будет сокращать количество переборов)  и целевую функцию для нахождения оптимального  решения.
Вариант 8. В зоопарке К животных. Сформировать все возможные варианты расстановки клеток.
"""


import itertools

def generate_permutations_functional(animals):
    print("Все возможные варианты: ", list(itertools.permutations(animals)))
    print("длина: ", len(list(itertools.permutations(animals))))
    return list(itertools.permutations(animals))

def calculate_adjacent_pairs(permutation, forbidden_pairs):
    return sum(1 for i in range(len(permutation) - 1)
               for pair in forbidden_pairs
               if (permutation[i], permutation[i + 1]) == pair or (permutation[i + 1], permutation[i]) == pair)

def find_optimal_arrangement(animals, forbidden_pairs):
    all_permutations = generate_permutations_functional(animals)
    optimal_permutation = min(all_permutations, key=lambda p: calculate_adjacent_pairs(p, forbidden_pairs))
    return optimal_permutation, calculate_adjacent_pairs(optimal_permutation, forbidden_pairs)


def input_animals_and_forbidden_pairs():
    K = int(input("Введите количество животных (K): "))
    animals = []
    for i in range(K):
        animal = input(f"Введите имя животного {i + 1}: ")
        animals.append(animal)

    forbidden_pairs = []
    print("Введите пары животных, которые не могут быть рядом (например, 'Лев Обезьяна' означает, что Лев и Обезьяна не могут быть рядом).")
    print("Введите 'done', когда закончите.")

    while True:
        pair_input = input("Введите пару или 'done': ")
        if pair_input.lower() == 'done':
            break
        try:
            animal1, animal2 = pair_input.split()
            forbidden_pairs.append((animal1, animal2))
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите два имени, разделенные пробелом.")

    return animals, forbidden_pairs

# Основная часть программы
animals, forbidden_pairs = input_animals_and_forbidden_pairs()
optimal_arrangement, adjacent_pairs_count = find_optimal_arrangement(animals, forbidden_pairs)

print(animals, forbidden_pairs)
print("Оптимальная расстановка:", optimal_arrangement)
print("Количество запрещенных пар, которые стоят рядом:", adjacent_pairs_count)
