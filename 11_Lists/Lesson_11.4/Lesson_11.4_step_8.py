# 11.4 Вывод элементов списка
"""
Negatives, Zeros and Positives
На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая сначала выводит все отрицательные числа, затем нули, а затем все положительные числа, каждое на отдельной строке. Числа должны быть выведены в том же порядке, в котором они были введены.

Формат входных данных
На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.


"""

n = int(input())
list = []
list1 = []
list2 = []
list3 = []

for i in range(n):
    list.append(int(input()))

for j in range(len(list)):
    if list[j] < 0:
        list1.append(list[j])
for l in range(len(list)):
    if list[l] == 0:
        list2.append(list[l])
for m in range(len(list)):
    if list[m] > 0:
        list3.append(list[m])
print(*list1, *list2, *list3, sep='\n')