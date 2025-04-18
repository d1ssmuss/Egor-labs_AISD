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
скопировать в нее А и если в С количество простых чисел в нечетных столбцах, 
чем количество нулевых  элементов в четных строках, 
то поменять местами Е и С симметрично, 
иначе С и В поменять местами несимметрично. 
При этом матрица А не меняется. 
После чего если определитель матрицы А больше суммы диагональных элементов матрицы F, 
то вычисляется выражение: A-1*AT – K * F, 
иначе вычисляется выражение (AТ +G-1-F-1)*K, где G-нижняя треугольная матрица, полученная из А. 
Выводятся по мере формирования А, F и все матричные операции последовательно.
"""
