"""
Лабораторная работа №5
Задана рекуррентная функция. Область определения функции – натуральные числа.
Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
Определить границы применимости рекурсивного и итерационного подхода.
Результаты сравнительного исследования времени вычисления представить
в табличной и графической форме в виде отчета по лабораторной работе.

Вариант 8:
F(1) = G(1) = 1;
F(n) = (-1)**n * (G(n–1) / (2n)!),
G(n) = F(n–1), при n >=2
"""
import timeit
import os
# Ввод числа
n = int(input("Введите натуральное число N:"))

# Граница применимости
if n >= 85:
    print("Вы ввели огромное число, пожалуйста перезапустите программу!")
    os._exit(0)

time_recursive = []
time_iteration = []
# Список значений F и G
# Рекурсивно
F_recursion_result = []
G_recursion_result = []

# Итерационно
F_iteration_result = [1]
G_iteration_result = [1]
f_iteration_prev = 1
g_iteration_prev = 1
f, g = 0,0
sign = 1 # знак для итерационного подхода

# Факториал

def iterative_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Итерационный подход

def F_iteraive(i):
    global sign, g, f, f_iteration_prev, g_iteration_prev
    f = (sign * (g_iteration_prev / iterative_factorial(2 * (i+1))))
    F_iteration_result.append(f)
    f_iteration_prev = f
    g_iteration_prev = g
    sign *= -1

def G_iterative():
    global g, f, f_iteration_prev, g_iteration_prev
    g = f_iteration_prev
    G_iteration_result.append(g)


# Рекурсивный подход

def F_recursion(n):
    if n == 1:
        return 1
    else:
        return ((1 if n % 2 == 0 else -1) * (G_recursion(n-1) / iterative_factorial(2 * n)))


def G_recursion(n):
    if n == 1:
        return 1
    else:
        return F_recursion(n-1)

# Функция для измерения времени выполнения

def score_time(func):
    return timeit.timeit(lambda: func, number=1000)


for i in range(1, n+1):
    G_iterative()
    F_iteraive(i)

    iterative_time = score_time(F_iteraive)
    time_iteration.append(iterative_time)

    G_recursion_result.append(G_recursion(i))
    F_recursion_result.append(F_recursion(i))

    time_recursive.append(score_time(F_recursion(i)))

else:
    G_recursion_result.append(G_recursion(n+1))
    F_recursion_result.append(F_recursion(n+1))

print(f"{'n':<10}{'F_рекурсивно':<25}{'F_итерационно':<25}{'G_рекурсивно':<25}{'G_итерационно':<25}{'Рекурсивное время (мс)':<25}{'Итерационное время (мс)':<25}")
for i, n in enumerate(range(1, n+1)):
    print(f"{n:<10}{F_recursion_result[i]:<25}"
          f"{F_iteration_result[i]:<25}"
          f"{G_recursion_result[i]:<25}"
          f"{G_iteration_result[i]:<25}{
          time_recursive[i]:<25}"
          f"{time_iteration[i]:<25}")
