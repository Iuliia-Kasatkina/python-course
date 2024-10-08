# 5.1 Задачи на программирование
"""
Ход слона ♗🌶️

Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли слон попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом слона можно попасть во вторую, или «NO» в противном случае.

Формат входных данных
На вход программе подаются четыре числа от 1 до 8.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Шахматный слон ходит по диагоналям.

"""

a, b, c, d = int(input()), int(input()), int(input()), int(input())

if a - b == 0:
    if c - d == 0:
        print("YES")
    else:
        if a != c and c % 2 == 1 and d % 2 == 1 and ((d - c) % 2 == 0 or -(d - c) % 2 == 0):
            print("YES")
        else:
            if a != c and c % 2 == 0 and d % 2 == 0 and ((d - c) % 2 == 0 or -(d - c) % 2 == 0) and b != d:
                print("YES")
            else:
                print("NO")
else:
    if (a == d and b == c) and (b - a == c - d or a - b == d - c):
        print("YES")
    else:
        if a - b == c - d or b -a == d -c:
            print("YES")
        else:
            print("NO") 