# 6.1 Числовые типы данных: int, float
"""
Первая цифра после точки

Дано положительное действительное число. Выведите его первую цифру после десятичной точки.

Формат входных данных
На вход программе подаётся положительное действительное число.

Формат выходных данных
Программа должна вывести цифру в соответствии с условием задачи.

"""

n = float(input())

print(int(n * 10) % 10)