# 11.5 Методы строк: split, join
"""
 Диаграмма

На вход программе подается строка текста, содержащая целые числа. Напишите программу, которая по заданным числам строит столбчатую диаграмму.

Формат входных данных
На вход программе подается строка текста, содержащая целые числа, разделенных символом пробела.

Формат выходных данных
Программа должна вывести столбчатую диаграмму.

"""

s = input()

numbers = s.split()
for i in range(len(numbers)):
    print('+' * int(numbers[i]))