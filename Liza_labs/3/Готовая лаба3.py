"""
С клавиатуры вводится два числа K и N.
Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10].
Для тестирования использовать не случайное заполнение, а целенаправленное.

Для ИСТд-13 вид матрицы А
D	Е
С	В

Для ИСТд-13
  4
3   1
  2

Вариант 8. Формируется матрица F следующим образом:
если в С количество простых чисел в нечетных столбцах в области 2 больше,
чем количество нулевых  элементов в четных строках в области 3,
то поменять в С симметрично области 1 и 3 местами,
иначе С и В поменять местами несимметрично.
При этом матрица А не меняется.
После чего вычисляется выражение: ((К*A)*F – (K * AT)).
Выводятся по мере формирования А, F и все матричные операции последовательно.
"""
import random
import os

count_prime_numbers = 0 # кол-во простых чисел
count_zero_elements = 0 # кол-во нулевых элементов

print("--- Начало работы --- ")

def multiply_matrix(m1, m2):
    return [
        [sum(x * y for x, y in zip(m1_r, m2_c)) for m2_c in zip(*m2)] for m1_r in m1
    ]


def is_prime(n):  
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


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
                 [0, 5, -1, 10, 10, 4, -9, -5, 2, -6],
                 [8, -4, 5, 10, -2, 8, 8, -5, -5, -3],
                 [0, 8, -10, 7, -1, -7, -6, -3, 3, -6],
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
            if choice == 0:
                for i in range(N):
                    for j in range(N):
                        print("{:8d}".format(A[i][j]), end="")
                    print()
                break
            elif choice == 1:
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

# Работаем с C - область 2
# если в С количество простых чисел в нечетных столбцах в области 2 больше,
for i in range((middle_line // 2) + 1, middle_line):
    for j in range(middle_line-i, i):
        # print(i,j) # индексы
        if j % 2 == 0 and is_prime(C[i][j]):
            count_prime_numbers += 1
print("Кол-во простых чисел в нечётных столбцах: ", count_prime_numbers)
# # Работаем с C - область 3
# чем количество нулевых  элементов в четных строках в области 3

for i in range(0, middle_line+1):
    for j in range(i+1, (middle_line - i)-1):
        if j % 2 != 0 and C[j][i] == 0:
            count_zero_elements += 1
print("Количество нулевых элементов в четных строках в области 3: ", count_zero_elements)

if count_prime_numbers > count_zero_elements:
    # то поменять в С симметрично области 1 и 3 местами,
    for i in range(middle_line):
        for j in range(middle_line):
            if j < i < middle_line - 1 - j:
                C[i][j], C[i][middle_line - 1 - j] = C[i][middle_line - 1 - j], C[i][j]
else:
    # иначе С и В поменять местами несимметрично.
    C, B = B, C

# Формируем матрицу F
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


print("Матрица F:")
print_matrix(F) # Матрица F
print()

# При этом матрица А не меняется.
print("Матрица A:")
print_matrix(A) # Матрица A остаётся неизменной
# Выводятся по мере формирования А, F и все матричные операции последовательно.
# После чего вычисляется выражение: ((К*A)*F – (K * AT)).
# 1) K * A
# 2) A**T (транспанирование)
# 3) (K * A ** T)
# 4) (K*A) * F
# 5) ((K*A) * F - (K * A ** T))

# Операции
# 1) K * A
KA = [[K * A[i][j] for j in range(N)] for i in range(N)] # Матрица F
print()
print("Матрица K * A:")
print_matrix(KA)

# 2) A**T (транспанирование)
# Ручное транспонирование
transposed_A = [[0] * N for _ in range(N)]  # Создаем пустую матрицу для транспонирования
for i in range(N):
    for j in range(N):
        transposed_A[j][i] = A[i][j]  # Меняем местами индексы
print()
print("Матрица AT:")
print_matrix(transposed_A)
# 3) (K * A ** T)
K_A_T = [[K * transposed_A[i][j] for j in range(N)] for i in range(N)] # Матрица F
print()
print("Матрица K * A ** T:")
print_matrix(K_A_T)
# 4) (K*A) * F
K_A_F = multiply_matrix(KA, F)
print()
print("Матрица F_A_AT:")
print_matrix(K_A_F)
# 5) ((K*A) * F - (K * A ** T))
K_A_F_minus_K_A_T = [[K_A_F[i][j] - K_A_T[i][j] for j in range(N)] for i in range(N)]
print()
print("Матрица K_A_F_minus_K_A_T:")
print_matrix(K_A_F_minus_K_A_T)
print()
print("--- Конец работы --- ")
