# 4.2 Логические операции
"""
Красивое число 🌶️

Назовём число красивым, если оно является четырёхзначным и делится нацело на 7 или на 17. Напишите программу, определяющую, является ли введённое число красивым. Программа должна вывести «YES» (без кавычек), если число является красивым, или «NO» (без кавычек) в противном случае.

Формат входных данных
На вход программе подаётся натуральное число.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

"""

x = int(input())

if 0 < x // 1000 < 10 and (x % 7 == 0 or x % 17 == 0):
    print("YES")
else:
    print("NO")