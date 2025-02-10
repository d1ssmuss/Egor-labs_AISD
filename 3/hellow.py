"""
✅
Лабораторная работа № 3 - АиСД
С клавиатуры вводятся два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц,
B, C, D, E заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное
заполнение, а целенаправленное.
Вид матрицы А:
D	Е
С	В
Каждая из матриц B, C, D, E имеет вид:
     4
  3     1
     2

Вариант 23:
Формируется матрица F следующим образом: 
если в Е сумма чисел, больших К в нечетных столбцах в области 3 больше, 
чем произведение чисел по периметру в области 2, 
то поменять в Е симметрично области 1 и 2 местами, 
иначе С и В поменять местами несимметрично. 
При этом матрица А не меняется. 
После чего вычисляется выражение: (К*A)*F+ K* FT.
Выводятся по мере формирования А, F и все матричные операции последовательно.
"""

import random
import os
print("--- Начало работы --- ")


sum_of_numbers = 0 # Сумма чисел
product_of_numbers_perimetr = 1 # Произведение чисел по периметру

def multiply_matrix(m1, m2):
    return [
        [sum(x * y for x, y in zip(m1_r, m2_c)) for m2_c in zip(*m2)] for m1_r in m1
    ]

def print_matrix(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print("{:8d}".format(arr[i][j]), end="")
        print()

while True:
    try:
        # Выборы вариантов работы
        print("--- Выбор варианта работы --- ")
        print("[0] - Если вы хотите использовать целенаправленное заполнение матрицы")
        print("[1] - Если вы хотите использовать случайное заполнение матрицы")
        print("[2] - Выход из программы")
        choice = int(input("Введите номер варианта: "))
        if choice == 0:
            # Целенаправленное заполнение матрицы
            print("--- Целенаправленное заполнение матрицы --- ")
            print("Пример матрицы 10x10")
            N = 10
            A = [[2, -7, 4, 3, -4, 10, 1, 0, 2, 7],
                 [-9, 9, -9, 2, -2, -9, 5, 10, 4, -4],
                 [-7, 2, 3, 6, 6, 4, 0, 6, 4, -1],
                 [3, 2, 9, 1, -5, -4, 5, 5, -9, 7],
                 [-3, -2, -4, 5, -7, -5, 10, -10, 6, 5],
                 [8, 6, 2, -6, 1, 1, 0, 1, 0, 5],
                 [-3, 5, -1, 10, 10, 4, -9, -5, 2, -6],
                 [8, -4, 5, 10, -2, 8, 8, -5, -5, -3],
                 [2, 8, -10, 7, -1, -7, -6, -3, 3, -6],
                 [1, -10, 5, -1, 1, -9, -8, 9, -6, 8]]
        elif choice == 1:
            # Случайное заполнение матрицы
            print("--- Случайное заполнение матрицы --- ")
            N = int(input("Введите число N: "))
        elif choice == 2:
            print("--- Выход из программы --- ")
            os._exit(0)
        else:
            print("--- Неизвестная команда! Перезапустите программу --- ")
            os._exit(0)
        K = int(input("Введите число K: "))
        # Примечание! Т.к в ЛР, матрица состоит из 4-х равных по размерам под матриц следует что N % 2 == 0 и N >= 6
        middle_line = N // 2  # Размерность под матрицы D, E, C, B и средняя линия
        if N % 2 == 0 and N >= 6:
            # Создаем матрицу A NxN и заполняем ее вручную
            print("Матрица A:")
            A = [[0 for i in range(N)] for j in range(N)]
            for i in range(N):
                for j in range(N):
                    A[i][j] = random.randint(-10, 10)
                    print("{:8d}".format(A[i][j]), end="")
                print()
            break
        else:
            print("Т.к матрица состоит из 4-х равных по размерам под матриц следует что N % 2 == 0 и N >= 6")
    except:
        print("Некорректный запрос! Повторите попытку.")


D = [[A[i][j] for j in range(N // 2)] for i in range(N//2)]
E = [[A[i][j] for j in range(N // 2, N)] for i in range(0, N//2)]
C = [[A[i][j] for j in range(N // 2)] for i in range(N//2, N)]
B = [[A[i][j] for j in range(N // 2, N)] for i in range(N//2, N)]
F = [[A[i][j] for j in range(N)] for i in range(N)] # Матрица F, при этом матрица А не меняется

# Работаем с E - область 3
for i in range(0, middle_line+1):
    for j in range(i+1, (middle_line - i)-1):
        if j % 2 == 0 and E[j][i] > K:
            sum_of_numbers += E[j][i]
print("Сумма чисел, больших К в нечетных столбцах в области 3: ", sum_of_numbers)
# работаем с E - область 2
# Периметр
elements_p = []
# 1)
for i in range(N-1, middle_line - 1, -1):
    product_of_numbers_perimetr *= (A[i][N - i - 1])
    elements_p.append(A[i][N - i - 1])
# 2)
for i in range(middle_line, N):
    product_of_numbers_perimetr *= A[i][i]
    elements_p.append(A[i][i])
# 3)
for j in range(1, N-1):
    product_of_numbers_perimetr *= A[N-1][j]
    elements_p.append(A[N-1][j])

print(f"Элементы периметра области 2: {elements_p}")
print("Произведение чисел по периметру в области 2: ", product_of_numbers_perimetr)
"""
если в Е сумма чисел, больших К в нечетных столбцах в области 3 больше, 
чем произведение чисел по периметру в области 2, 
то поменять в Е симметрично области 1 и 2 местами, 
иначе С и В поменять местами несимметрично. 
"""
# Выполняется условие
# если в Е сумма чисел, больших К в нечетных столбцах в области 3 больше,
# Чем произведение чисел по периметру в области 2,
if sum_of_numbers > product_of_numbers_perimetr:
    print("Если в Е сумма чисел, больших К в нечетных столбцах в области 3 больше, чем произведение чисел по периметру в области 2")
    # Меняем симметрично области 1 и 2 в матрице Е
    for i in range((middle_line // 2) + 1, middle_line):
        for j in range(middle_line - i, i):
            E[i][j], E[j][i] = E[j][i], E[i][j]
else:
    print("Если в Е сумма чисел, больших К в нечетных столбцах в области 3 меньше, чем произведение чисел по периметру в области 2")
    C, B = B, C

# Формируем матрицу F
print()
for i in range(N // 2):
    for j in range(N // 2):
        F[i][j] = D[i][j]  # D

for i in range(N // 2):
    for j in range(N // 2, N):
        F[i][j] = E[i][j - (N // 2)]  # E

for i in range(N // 2, N):
    for j in range(N // 2):
        F[i][j] = C[i - N // 2][j]  # C

for i in range(N // 2, N):
    for j in range(N // 2, N):
        F[i][j] = B[i - N // 2][j - N // 2]  # B

# При этом матрица А не меняется.
print("Матрица A:")
print_matrix(A) # Матрица A остаётся неизменной
print()
print("Матрица F:")
print_matrix(F)
print()
# Выводятся по мере формирования А, F и все матричные операции последовательно.
# После чего вычисляется выражение: (К*A)*F+ K* FT.
# 1) FT (транспанирование)
# 2) K * FT
# 3) K * A
# 4) (K*A) * F
# 5) (K*A) * F + K * FT

# Операции
# 1) FT (транспанирование)
transposed_F = [[0] * N for _ in range(N)]  # Создаем пустую матрицу для транспонирования

for i in range(N):
    for j in range(N):
        transposed_F[j][i] = F[i][j]  # Меняем местами индексы
print("Матрица FT:")
print_matrix(transposed_F)
print()
# Проверка матриц
# 2) K * FT
K_FT = [[K * transposed_F[i][j] for j in range(N)] for i in range(N)] # Матрица F
print("Матрица K * FT:")
print_matrix(K_FT)
# 3) K * A
K_A = [[K * A[i][j] for j in range(N)] for i in range(N)]
print()
print("Матрица K_A:")
print_matrix(K_A)
# 4) (K*A) * F
K_A_F = multiply_matrix(K_A, F)
print()
print("Матрица K_A_F:")
print_matrix(K_A_F)
# 5) (K*A) * F + K * FT
K_A_F_plus_K_FT = [[K_A_F[i][j] + K_FT[i][j] for j in range(N)] for i in range(N)]
print()
print("Матрица K_A_F_plus_K_FT:")
print_matrix(K_A_F_plus_K_FT)
print()
print("--- Конец работы --- ")