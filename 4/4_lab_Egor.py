"""
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
import matplotlib as plt
from numpy.random.mtrand import operator


print("тут менять k n ")
K = -9
# N = int(input("Введите число N:"))
N = 6
middle_line = N // 2

sum_of_numbers = 0 # Сумма чисел
product_of_numbers_perimetr = 1 # Произведение чисел по периметру

print("B")
b = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(b, '\n')
print("C")
c = np.array([[1,1,1], [1,1,1], [1,1,1]])
print(c, '\n')
print("D")
d = np.array([[5,5,5], [5,5,5], [5,5,5]])
print(d, '\n')
print("E")
e = np.array([[1,1,1], [2,2,2], [4,4,4]])
print(e, '\n')

# Матрица А
print("Матрица A: ")
a = np.vstack(((np.hstack([d, e])), (np.hstack([c, b]))))
print(a)


#  **** Определитель матрицы A
det_A = int(np.linalg.det(a))
print(f"Определитель матрицы A: {det_A}")


# G-нижняя треугольная матрица, полученная из А
g = np.tri(N) * a
print("Матрица G:")
print(g)


print("f")
f = copy.deepcopy(a)
print(f)

# Работаем с E - область 3
for i in range(0, middle_line, 2):
    for j in range(0, len(e)):
        # print(j,i)
        if i % 2 == 0 and e[j][i] > K:
            print(e[j][i])
            sum_of_numbers += e[j][i]
print("Сумма чисел, больших К в нечетных столбцах в матрице E: ", sum_of_numbers)


# ------
# Здесь периметр - это внешние числа матрицы
# Периметр
elements_p = []
print('-'*100)
for i in range(0, len(e)):
    if i == 0 or i == len(e) - 1:
        product_of_numbers_perimetr *= reduce(operator.mul, e[i], 1)
        print(reduce(operator.mul, e[i], 1), "!!")
    else:
        print(e[i][0] + e[i][-1], "!")
        product_of_numbers_perimetr *= e[i][0] + e[i][-1]

print(f"Элементы периметра области 2: {elements_p}")
print("Произведение чисел по периметру в области 2: ", product_of_numbers_perimetr)





# --------------------------------------

if sum_of_numbers > product_of_numbers_perimetr:
    # меняем C и E симметрично
    # Вроде правильно
    print("Случай!!!")
    print("sum_of_numbers > product_of_numbers_perimetr")
    """f[middle_line:N, middle_line:N] = np.fliplr(c)
    f[middle_line:N, :middle_line] = np.fliplr(e)"""
    f[:middle_line, middle_line:N] = np.fliplr(c)
    f[middle_line:N, :middle_line] = np.flipud(e)
else:
    print("sum_of_numbers < product_of_numbers_perimetr")
    f = np.vstack(((np.hstack([d, e])), (np.hstack([b, c]))))


print("f::")
print(f)

# *** Сумма Диагональных элементов
summ_diagonal_elements = sum(np.diagonal(f))
print("Сумма Диагональных элементов:", summ_diagonal_elements)


print('*'*100)

if det_A > summ_diagonal_elements:
    # A*A-1 – K * F-1
    pass
else:
    # (AТ +G-FТ)*K
    # G-нижняя треугольная матрица, полученная из А
    pass



# Выводятся по мере формирования А, F и все матричные операции последовательно

# + график



