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


def count_size_violations(arrangement):
    violations = 0
    for i in range(len(arrangement) - 1):
        if animal_sizes[arrangement[i]] == "L" and animal_sizes[arrangement[i + 1]] == "L":
            violations += 1
    return violations


def find_best_size_arrangement(animals):
    best_arrangement = None
    min_violations = float('inf')

    for perm in itertools.permutations(animals):
        violations = count_size_violations(perm)
        if violations < min_violations:
            min_violations = violations
            best_arrangement = perm
            if min_violations == 0:  # идеальный вариант
                break

    return best_arrangement, min_violations


try:
    n = int(input("Введите количество животных: "))
    print("Список животных и их размер:")
    print(animal_sizes)
    if n >= 0:
        animals = [input(f"Введите животное {i + 1}: ") for i in range(n)]

        start_time = time.time()
        best_arrangement, violations = find_best_size_arrangement(animals)
        end_time = time.time()

        print("Оптимальная расстановка - нет двух больших (размера L) животных рядом")
        if violations == 0:
            print(f"\nЛучшая расстановка: {best_arrangement}")
        else:
            print("Не найдено лучшей расстановки!")
            print(f"Количество нарушений (два крупных животных рядом): {violations}")
        print(f"Время выполнения: {end_time - start_time:.5f} секунд")
    else:
        print("Ошибка: число животных не может быть отрицательным!")
except ValueError:
    print("Ошибка: введите целое число!")
