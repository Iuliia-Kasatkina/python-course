# 11.4 Вывод элементов списка
"""
Значение функции

На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая для каждого введенного числа x выводит значение функции f(x) = x ** 2 + 2x + 1, каждое на отдельной строке.

Формат входных данных
На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести сначала введенные числа, затем пустую строку, а затем соответствующие значения функции.

Примечание. Для первого теста имеем:

f(1) = 1 ** 2 + 2⋅1 + 1 = 4, f(2) = 2 ** 2 + 2⋅2 + 1 = 9, f(3) = 3 ** 2  + 2⋅3 + 1 = 16, …


"""

n = int(input())
numbers = []

for i in range(n):
    x = int(input())
    numbers.append(x)
    print(x)

print()

for x in numbers:
    f = x ** 2 + 2 * x + 1
    print(f)