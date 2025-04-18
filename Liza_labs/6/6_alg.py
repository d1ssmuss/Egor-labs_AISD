"""
Задание на л.р. №6
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования
(алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов
(которое будет сокращать количество переборов)  и целевую функцию для нахождения оптимального  решения.
Вариант 8. В зоопарке К животных. Сформировать все возможные варианты расстановки клеток.
"""
# Алгоритмический подход

import time

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

# Пример использования
n = int(input("Введите количество животных: "))
animals = [input(f"Введите животное {i + 1}: ") for i in range(n)]
start_time = time.time()
algorithmic_permutations = generate_permutations_algorithmic(animals)
end_time = time.time()
print(f"Время алгоритмического подхода: {end_time - start_time} секунд")
print("Все возможные варианты: ")
for i in algorithmic_permutations:
    print(i)
print(f"Количество вариантов расстановки клеток : {len(algorithmic_permutations)}")
