# 11.3 Методы списков. Часть 1
"""
Удалите нечетные индексы

На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая создает из указанных чисел список, затем удаляет все элементы стоящие по нечетным индексам, а затем выводит полученный список.

Формат входных данных
На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести список в соответствии с условием задачи.

Примечание. Используйте оператор del.


"""

n = int(input())
list = []

for i in range(n):
    num = int(input())
    list.append(num)

del list[1::2]
print(list)