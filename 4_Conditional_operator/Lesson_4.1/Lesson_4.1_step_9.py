# 4.1 Выбор из двух
"""
Арифметическая прогрессия

Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке) последовательными членами арифметической прогрессии.

Формат входных данных
На вход программе подаются три числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести «YES» или «NO» (без кавычек) в соответствии с условием задачи.

"""

a = int(input())
b = int(input())
c = int(input())

if b - a == c - b:
    print("YES")
else:
    print("NO")