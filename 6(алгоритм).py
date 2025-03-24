"""
Сипатов Егор ИСТбд-23
Задание на л.р. №6
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение
на характеристики объектов (которое будет сокращать количество переборов)
и целевую функцию для нахождения оптимального  решения.
Вариант 23. Сформируйте разные варианты распределения Т предметов между К людьми.
Алгоритмический подход
"""
import time

def get_input():
    # Ввод количества предметов и их названий
    T = int(input("Введите количество предметов: "))
    items = []
    for i in range(T):
        item = input(f"Введите название предмета {i+1}: ")
        items.append(item)

    # Ввод количества людей
    K = int(input("Введите количество людей: "))
    people = []
    for i in range(K):
        person = input(f"Введите имя человека {i+1}: ")
        people.append(person)

    return items, people

def distribute_items_recursive(items, people, current=None, remaining=None, result=None):
    if current is None:
        current = []
    if remaining is None:
        remaining = items[:]
    if result is None:
        result = []

    if not remaining:
        result.append(current[:])
        return

    for person in people:
        current.append((remaining[0], person))
        distribute_items_recursive(items, people, current, remaining[1:], result)
        current.pop()

    return result

def find_optimal_distribution(distributions, people):
    # Поиск оптимального распределения, где у каждого человека есть хотя бы один предмет
    for dist in distributions:
        person_items = {person: 0 for person in people}
        for _, person in dist:
            person_items[person] += 1
        if all(count > 0 for count in person_items.values()):
            return dist
    return None

def main():
    items, people = get_input()

    start_time = time.time()
    distributions = distribute_items_recursive(items, people)
    end_time = time.time()

    print("Все возможные варианты распределения:")
    count = 0
    for dist in distributions:
        print(count, dist)
        count += 1
    print(f"Время выполнения: {end_time - start_time} секунд")

    optimal_distribution = find_optimal_distribution(distributions, people)
    if optimal_distribution:
        print("\nОптимальный вариант распределения (у каждого человека есть хотя бы один предмет):")
        print(optimal_distribution)
    else:
        print("\nНе удалось найти оптимальный вариант распределения.")

if __name__ == "__main__":
    main()

