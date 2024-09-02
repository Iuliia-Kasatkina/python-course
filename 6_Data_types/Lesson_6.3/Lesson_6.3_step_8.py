# 6.3 Модуль math
"""
Правильный многоугольник

Правильный многоугольник — выпуклый многоугольник, у которого равны все стороны и все углы между смежными сторонами. Площадь правильного многоугольника с длиной стороны a и количеством сторон n вычисляется по формуле:
S = (n * a ** 2) / 4 * tg(π / n)

Даны два числа: натуральное число n и вещественное число a. Напишите программу, которая находит площадь указанного правильного многоугольника.

Формат входных данных
На вход программе подается два числа n и a, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести вещественное число – площадь многоугольника.

"""

from math import pow, tan, pi
n, a = int(input()), float(input())

print((n * pow(a, 2)) / (4 * tan(pi / n)))