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

def generate_permutations_pythonic(animals):
    return list(itertools.permutations(animals))

def is_valid_permutation(permutation, constraints):
    for i in range(len(permutation) - 1):
        if (permutation[i], permutation[i+1]) in constraints or (permutation[i+1], permutation[i]) in constraints:
            return False
    return True

def count_dangerous_pairs(permutation, constraints):
    count = 0
    for i in range(len(permutation) - 1):
        if (permutation[i], permutation[i+1]) in constraints or (permutation[i+1], permutation[i]) in constraints:
            count += 1
    return count

def find_optimal_permutation(animals, constraints):
    permutations = generate_permutations_pythonic(animals)
    valid_permutations = [p for p in permutations if is_valid_permutation(p, constraints)]
    if valid_permutations:
        optimal_permutation = min(valid_permutations, key=lambda p: count_dangerous_pairs(p, constraints))
        return optimal_permutation
    else:
        return None

# Ввод данных
animals = input("Введите животных через запятую: ").split(',')
animals = [animal.strip() for animal in animals]

num_constraints = int(input("Введите количество пар ограничений: "))
constraints = set()
for _ in range(num_constraints):
    pair = input("Введите пару животных через запятую (например, 'Лев,Тигр'): ").split(',')
    constraints.add((pair[0].strip(), pair[1].strip()))


# Поиск оптимальной расстановки
start_time = time.time()
optimal_permutation = find_optimal_permutation(animals, constraints)
end_time = time.time()
print(f"Поиск оптимальной расстановки: {end_time - start_time} seconds")
if optimal_permutation:
    print(f"Оптимальный вариант: {optimal_permutation}")
else:
    print("Невозможно найти допустимую расстановку с заданными ограничениями.")

