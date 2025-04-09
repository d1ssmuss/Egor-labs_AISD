"""
С клавиатуры вводится два числа K и N.
Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10].
Для отладки использовать не случайное заполнение, а целенаправленное.
Вид матрицы А:
Для ИСТд-13
D	Е
С	В

Для простоты все индексы в подматрицах относительные.
По сформированной матрице F (или ее частям) необходимо вывести не менее 3 разных графиков.
Программа должна использовать функции библиотек numpy  и mathplotlib

8. Формируется матрица F следующим образом:
скопировать в нее А и
если в С количество простых чисел в нечетных столбцах больше,
чем количество нулевых  элементов в четных строках,

то поменять местами Е и С симметрично,

иначе С и В поменять местами несимметрично.

При этом матрица А не меняется.
После чего если определитель матрицы А больше суммы диагональных элементов матрицы F,
то вычисляется выражение: A-1*AT – K * F,
иначе вычисляется выражение (A**Т +G-1-F-1)*K, где G-нижняя треугольная матрица, полученная из А.
Выводятся по мере формирования А, F и все матричные операции последовательно.
"""
import copy
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt
from numpy.random.mtrand import operator

print("Тестирование: Целенаправленное")
K = int(input("Введите число K: "))
print("Для тестирования будем использовать матрицу 6x6")
N = 6
# M - middle_line средняя линия
M = N // 2

count_prime_numbers = 0 # кол-во простых чисел
count_zero_elements = 0 # кол-во нулевых элементов


# Матрицы
print("Матрица B :")
b = np.array([[-27,61,39], [88,-63,52], [45,-92,-37]])
print(b, '\n')
print("Матрица C :")
c = np.array([[-67,-39,96], [25,-45,31], [39,60,-40]])
print(c, '\n')
print("Матрица D :")
d = np.array([[43,-52,79], [73,92,-42], [82,28,92]])
print(d, '\n')
print("Матрица E :")
e = np.array([[96,-90,-32], [50,12,67], [-83,82,-73]])
print(e, '\n')

print("Матрица A: ")
a = np.vstack(((np.hstack([d, e])), (np.hstack([c, b]))))
print(a)

# Детерминант
det_A = int(np.linalg.det(a))
# G-нижняя треугольная матрица, полученная из А
g = np.tri(N) * a
# Матрица F
f = copy.deepcopy(a)

# Функция нахождения простого числа
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


# Работаем с C
for i in range(0, len(c)):
    for j in range(0, len(c)):
        if j % 2 == 0 and is_prime(c[i][j]): # нечётные столбцы
            count_prime_numbers += 1
        elif i % 2 != 0 and c[i][j] == 0: # чётные строки
            count_zero_elements += 1
if count_prime_numbers > count_zero_elements:
    # поменять местами Е и С симметрично
    f[:M, M:N] = np.fliplr(c)
    f[M:N, :M] = np.flipud(e)
else:
    # иначе С и В поменять местами несимметрично.
    f = np.vstack(((np.hstack([d, e])), (np.hstack([b, c]))))

print("Матрица F")
print(f)
# Сумма Диагональных элементов
summ_diagonal_elements = sum(np.diagonal(f))
if det_A > summ_diagonal_elements:
    # A-1*AT – K * F
    """
    1) a ** t
    2) a ** -1
    3) (a ** -1) * (a ** t)
    4) k * f
    5) ((a ** -1) * (a ** t)) - (k * f)
    """
    print("A ** T")
    a_t = np.transpose(a) # 1
    print(a_t)
    print("A ** -1")
    reverse_a = np.linalg.inv(a) # 2
    print(reverse_a)
    print("(A ** -1) * (A ** T)")
    reverse_a_multiply_a_t = np.dot(reverse_a,a_t) # 3
    print(reverse_a_multiply_a_t)
    print("K * F")
    kf = K * f # 4
    print(kf)
    print("((A ** -1) * (A ** T)) - (K * F)")
    reverse_a_multiply_a_t_minus_kf = reverse_a_multiply_a_t - kf # 5
    print(reverse_a_multiply_a_t_minus_kf)
else:
    # (A**Т+G-1-F-1)*K
    """
    1) a ** t
    2) g ** -1
    3) f ** -1
    4) (a ** t) + (g ** -1)
    5) (a ** t) + (g ** -1) - (f ** -1)
    6) ((a ** t) + (g ** -1) - (f ** -1)) * k
    """
    print("A ** T")
    a_t = np.transpose(a) # 1
    print(a_t)
    print("G ** -1")
    reverse_g = np.linalg.inv(g) # 2
    print(reverse_g)
    print("F ** -1")
    reverse_f = np.linalg.inv(f) # 3
    print(reverse_f)
    print("(A ** T) + (G ** -1)")
    a_t_plus_reverse_g = a_t + reverse_g # 4
    print(a_t_plus_reverse_g)
    print("(A ** T) + (G ** -1) - (f ** -1)")
    a_t_plus_reverse_g_minus_reverse_F = a_t_plus_reverse_g - reverse_f # 5
    print(a_t_plus_reverse_g_minus_reverse_F)
    print("((A ** T) + (G ** -1) - (f ** -1)) * k")
    a_t_plus_reverse_g_minus_reverse_F_multiply_k = K * a_t_plus_reverse_g_minus_reverse_F # 6
    print(a_t_plus_reverse_g_minus_reverse_F_multiply_k)

# -- Графики --
# Графики (визуализация)
column_index = 0
data = f[:, column_index]

# Создание графиков
plt.figure(figsize=(12, 10))

# 1. Точечный график
plt.subplot(2, 2, 1)  # 2 строки, 2 колонки, 1-й график
plt.scatter(np.arange(len(data)), data, color='blue', label='Scatter Plot')
plt.title('Scatter Plot of Column 1')
plt.xlabel('Row Index')
plt.ylabel('Value')
plt.grid()
plt.legend()

# 2. Стеблевый график
plt.subplot(2, 2, 2)  # 2 строки, 2 колонки, 2-й график
plt.stem(np.arange(len(data)), data, basefmt=" ")
plt.title('Stem Plot of Column 1')
plt.xlabel('Row Index')
plt.ylabel('Value')
plt.grid()

# 3. Линейный график
plt.subplot(2, 2, 3)  # 2 строки, 2 колонки, 3-й график
plt.plot(np.arange(len(data)), data, marker='o', label='Line Plot', color='orange')
plt.title('Line Plot of Column 1')
plt.xlabel('Row Index')
plt.ylabel('Value')
plt.grid()
plt.legend()

# 4. Гистограмма
plt.subplot(2, 2, 4)  # 2 строки, 2 колонки, 4-й график
plt.hist(data, bins=10, alpha=0.7, label='Histogram', color='green')
plt.title('Histogram of Column 1')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
