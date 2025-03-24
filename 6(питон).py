"""
Сипатов Егор ИСТбд-23
Задание на л.р. №6
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение
на характеристики объектов (которое будет сокращать количество переборов)
и целевую функцию для нахождения оптимального  решения.
Вариант 23. Сформируйте разные варианты распределения Т предметов между К людьми.
С помощью функций Питона
"""
import time
from itertools import product

def get_input():
    # Ввод количества предметов и их названий
    T = int(input("Введите количество предметов(<=7): "))
    items = []
    for i in range(T):
        item = input(f"Введите название предмета {i+1}: ")
        items.append(item)

    # Ввод количества людей
    K = int(input("Введите количество людей(<=7): "))
    people = []
    for i in range(K):
        person = input(f"Введите имя человека {i+1}: ")
        people.append(person)

    return items, people

def distribute_items(items, people):
    # Генерация всех возможных распределений
    distributions = list(product(people, repeat=len(items)))
    return distributions

def find_optimal_distribution(distributions, items, people):
    # Поиск оптимального распределения, где у каждого человека есть хотя бы один предмет
    for dist in distributions:
        person_items = {person: 0 for person in people}
        for person in dist:
            person_items[person] += 1
        if all(count > 0 for count in person_items.values()):
            return dist
    return None

def main():
    items, people = get_input()

    start_time = time.time()
    distributions = distribute_items(items, people)
    end_time = time.time()
    count = 0
    print("Все возможные варианты распределения:")
    for dist in distributions:
        print(count, list(zip(items, dist)))
        count += 1
    print(f"Время выполнения: {end_time - start_time} секунд")

    optimal_distribution = find_optimal_distribution(distributions, items, people)
    if optimal_distribution:
        print("\nОптимальный вариант распределения (у каждого человека есть хотя бы один предмет):")
        print(list(zip(items, optimal_distribution)))
    else:
        print("\nНе удалось найти оптимальный вариант распределения.")

if __name__ == "__main__":
    main()
