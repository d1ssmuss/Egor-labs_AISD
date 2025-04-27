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

def count_size_violations(arrangement, size_to_avoid, dangerous_pairs):
    violations = 0
    for i in range(len(arrangement) - 1):
        if animal_sizes[arrangement[i]] == size_to_avoid and animal_sizes[arrangement[i + 1]] == size_to_avoid:
            violations += 1
        if (arrangement[i], arrangement[i + 1]) in dangerous_pairs or (arrangement[i + 1], arrangement[i]) in dangerous_pairs:
            violations += 1
    return violations

def find_best_size_arrangement(animals, size_to_avoid, dangerous_pairs):
    best_arrangement = None
    min_violations = float('inf')

    for perm in itertools.permutations(animals):
        violations = count_size_violations(perm, size_to_avoid, dangerous_pairs)
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
            dangerous_pairs_input = input("Введите опасные пары через запятую (например, волк заяц, лиса антилопа): ")
            dangerous_pairs = set()
            for pair in dangerous_pairs_input.split(','):
                animal1, animal2 = pair.strip().split()
                dangerous_pairs.add((animal1, animal2))

            print(f"Оптимальная расстановка: Нет двух животных размера {size_to_avoid} рядом и опасных пар рядом")
            animals = [input(f"Введите животное №{i + 1}: ") for i in range(n)]
            start_time = time.time()
            best_arrangement, violations = find_best_size_arrangement(animals, size_to_avoid, dangerous_pairs)
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
