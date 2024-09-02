# 6.3 Модуль math
"""
Тригонометрическое выражение

Напишите программу, вычисляющую значение тригонометрического выражения sinx + cosx + tan**2x
по заданному числу градусов x.

Формат входных данных
На вход программе подается одно вещественное число x измеряемое в градусах.

Формат выходных данных
Программа должна вывести одно число – значение тригонометрического выражения.

Примечание 1. Тригонометрические функции принимают аргумент в радианах. Чтобы перевести градусы в радианы, воспользуйтесь формулой
r = (x * π) / 180

Примечание 2. Модуль math содержит встроенную функцию radians(), которая переводит угол из градусов в угол в радианах.

"""

from math import radians, pi, sin, cos, tan, pow
x = float(input())

print(sin(radians(x)) + cos(radians(x)) + pow(tan(radians(x)), 2))