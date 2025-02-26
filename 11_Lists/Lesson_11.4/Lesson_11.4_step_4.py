# 11.4 Вывод элементов списка
"""
Remove outliers

При анализе данных, собранных в рамках научного эксперимента, бывает полезно удалить самое большое и самое маленькое значение.

На вход программе подается натуральное число n, а затем n различных натуральных чисел. Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел, а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.

Формат входных данных
На вход программе подаются натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.


"""

n = int(input())
num_max = 0
num_min = 0
list = []

for i in range(n):
    num = int(input())
    list.append(num)

del list[list.index(max(list))]
del list[list.index(min(list))]
print(*list, sep='\n')