# 11.3 Методы списков. Часть 1
"""
Список кубов

На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая создает из указанных чисел список их кубов.

Формат входных данных
На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести список, состоящий из кубов указанных чисел.


"""

n = int(input())
list = []

for i in range(n):
    num = int(input())
    list.append(num ** 3)

print(list)