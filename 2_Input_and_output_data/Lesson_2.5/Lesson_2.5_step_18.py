# 2.5 Целочисленная арифметика. Часть 2
"""
Номер купе 🚉🌶️

В купейном вагоне имеется 9 купе с четырьмя местами для пассажиров в каждом. Напишите программу, которая определяет номер купе, в котором находится место с заданным номером (нумерация мест сквозная, начинается с 1).

Формат входных данных
На вход программе подаётся целое число – место с заданным номером в вагоне.

Формат выходных данных
Программа должна вывести одно число – номер купе, в котором находится указанное место.

"""

n = int(input())

print(-(-(n) // 4))