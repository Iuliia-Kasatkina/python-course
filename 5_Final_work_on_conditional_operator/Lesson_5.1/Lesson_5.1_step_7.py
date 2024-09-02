# 5.1 Задачи на программирование
"""
Ход коня ♘

Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли конь попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом коня можно попасть во вторую, или «NO» в противном случае.

Формат входных данных
На вход программе подаются четыре числа от 1 до 8.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Шахматный конь ходит буквой «Г».

"""

a, b, c, d = int(input()), int(input()), int(input()), int(input())

if a - c == 2 and (b - d == 1 or d - b == 1):
    print("YES")
elif a - c == 1 and (b - d == 2 or d - b == 2):
    print("YES")
elif c - a == 1 and (b - d == 2 or d - b == 2):
    print("YES")
elif c - a == 2 and (b - d == 1 or d - b == 1):
    print("YES")
else:
    print("NO")