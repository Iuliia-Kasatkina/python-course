# 2.4 Целочисленная арифметика. Часть 1
"""
Следующее и предыдущее 🔢

Напишите программу, которая считывает целое число и выводит для него на экран следующее и предыдущее целые числа в следующем формате:

Следующее за числом <текущее число> число: <следующее число>
Для числа <текущее число> предыдущее число: <предыдущее число>

Формат входных данных
На вход программе подаётся одно целое число.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

"""

x = int(input())

print("Следующее за числом", x, "число:", x + 1)
print("Для числа", x, "предыдущее число:", x - 1)