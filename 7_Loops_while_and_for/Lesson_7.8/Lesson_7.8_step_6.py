# 7.8 Вложенные циклы. Часть 1
"""
Таблица-2

Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу размером n×5, где в i-ой строке указано число i (числа отделены одним пробелом).

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести таблицу размером n×5 в соответствии с условием.

Примечание. В конце строки может быть пробел.

"""

n = int(input())

for i in range(1, n+1):
    for j in range(5):
        print(i, end=' ')
    print()