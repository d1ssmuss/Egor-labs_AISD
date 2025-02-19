"""
Егор Сипатов ИСТбд-23
С клавиатуры вводится два числа K и N.
Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10].
Для отладки использовать не случайное заполнение, а целенаправленное.
Вид матрицы А:

Для ИСТд-13
D	Е
С	В

Для простоты все индексы в подматрицах относительные.
По сформированной матрице F (или ее частям) необходимо вывести не менее 3 разных графика.
Программа должна использовать функции библиотек numpy  и mathplotlib

Вариант №23.
Формируется матрица F следующим образом:
скопировать в нее А и  если в Е сумма чисел,
больших К в нечетных столбцах больше,
чем произведение чисел по периметру,
то поменять местами С и Е симметрично,
иначе С и В поменять местами несимметрично.
При этом матрица А не меняется.
После чего если определитель матрицы А больше суммы диагональных элементов матрицы F,
то вычисляется выражение: A*A-1 – K * F-1,
иначе вычисляется выражение (AТ +G-FТ)*K,
где G-нижняя треугольная матрица, полученная из А.
Выводятся по мере формирования А, F и все матричные операции последовательно.
"""
import copy
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt
from numpy.random.mtrand import operator


print("Используем целенаправленное тестирование")
K = int(input("Введите число K:"))
# N = int(input("Введите число N:"))
N = 6
middle_line = N // 2

sum_of_numbers = 0 # Сумма чисел
product_of_numbers_perimetr = 1 # Произведение чисел по периметру

print("B")
b = np.array([[71,76,90], [41,12,53], [45,24,58]])
print(b, '\n')
print("C")
c = np.array([[10,57,74], [90,40,33], [15,52,11]])
print(c, '\n')
print("D")
d = np.array([[43,28,86], [36,48,75], [58,28,71]])
print(d, '\n')
print("E")
e = np.array([[89,64,86], [18,94,16], [29,80,29]])
print(e, '\n')

# Матрица А
print("Матрица A: ")
a = np.vstack(((np.hstack([d, e])), (np.hstack([c, b]))))
print(a)


# Определитель матрицы A
det_A = int(np.linalg.det(a))
# G-нижняя треугольная матрица, полученная из А
g = np.tri(N) * a
# Матрица F
f = copy.deepcopy(a)

# Работаем с E
for i in range(0, middle_line, 2):
    for j in range(0, len(e)):
        # print(j,i)
        if i % 2 == 0 and e[j][i] > K:
            sum_of_numbers += e[j][i]

# Здесь периметр - это внешние числа матрицы
# Периметр
for i in range(0, len(e)):
    if i == 0 or i == len(e) - 1:
        product_of_numbers_perimetr *= reduce(operator.mul, e[i], 1)
    else:
        product_of_numbers_perimetr *= e[i][0] + e[i][-1]

if sum_of_numbers > product_of_numbers_perimetr:
    # меняем C и E симметрично
    """f[middle_line:N, middle_line:N] = np.fliplr(c)
    f[middle_line:N, :middle_line] = np.fliplr(e)"""
    f[:middle_line, middle_line:N] = np.fliplr(c)
    f[middle_line:N, :middle_line] = np.flipud(e)
else:
    f = np.vstack(((np.hstack([d, e])), (np.hstack([b, c]))))

print("Матрица F")
print(f)
# Сумма Диагональных элементов
summ_diagonal_elements = sum(np.diagonal(f))

if det_A > summ_diagonal_elements:
    # A*A-1 – K * F-1
    """
    1) a-1
    2) a * a-1
    3) f-1
    4) k * f-1
    5) (a * a-1) - (k * f-1)
    """
    print("A ** -1")
    reverse_a = np.linalg.inv(a) # 1
    print(reverse_a)
    print("A * A ** -1")
    a_compose_reverse_a = np.dot(a, reverse_a) # 2
    print(a_compose_reverse_a)
    print("F ** -1")
    reverse_f = np.linalg.inv(f) # 3
    print(reverse_f)
    print("K * F ** -1")
    k_compose_reverse_f = K * reverse_f # 4
    print(k_compose_reverse_f)
    print("(A * A ** -1) - (K * F ** -1)")
    result = a_compose_reverse_a - k_compose_reverse_f # 5
    print(result)

else:
    # (AТ +G-FТ)*K
    """
    1) at
    2) ft
    3) at + g
    4) at + g - ft
    5) (at + g - ft) * k
    """
    print("A ** T")
    transposed_a = np.transpose(a) # 1
    print(transposed_a)
    print("F ** T")
    transposed_f = np.transpose(f) # 2
    print(transposed_f)
    print("A ** T + G")
    at_plus_g = transposed_a + g # 3
    print(at_plus_g)
    print("A ** T + G - F ** T")
    at_plus_g_minus_ft = at_plus_g - transposed_f # 4
    print(at_plus_g_minus_ft)
    print("(A ** T + G - F ** T) * K")
    result = at_plus_g_minus_ft * K
    print(result)

# Графики (визуализация)
# Создаем фигуру и подграфики
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Линейный график
axs[0, 0].plot(f.flatten())
axs[0, 0].set_title('Линейный график')

# Гистограмма
axs[0, 1].hist(f.flatten(), bins=30)
axs[0, 1].set_title('Гистограмма')

# Точечный график
rows = f.tolist()
columns = np.array(f).T.tolist()
axs[1, 0].scatter(rows, columns)
axs[1, 0].set_title('Точечный график')

# Тепловая карта
cax = axs[1, 1].imshow(f, cmap='hot', interpolation='nearest')
axs[1, 1].set_title('Тепловая карта')
fig.colorbar(cax, ax=axs[1, 1])

plt.tight_layout()
plt.show()
