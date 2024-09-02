# 6.1 Числовые типы данных: int, float
"""
Dog age 🐶

На вход программе подаётся число n – количество собачьих лет. Напишите программу, которая вычисляет возраст собаки в человеческих годах по следующему алгоритму: в течение первых двух лет собачий год равен 10.5 человеческим годам, после этого каждый год собаки равен 4 человеческим годам.

Формат входных данных
На вход программе подаётся натуральное число – количество собачьих лет.

Формат выходных данных
Программа должна вывести возраст собаки в человеческих годах.

"""

n = int(input())

if 1 <= n <= 2:
    print(n * 10.5)
else:
    print(2 * 10.5 + (n - 2) * 4)