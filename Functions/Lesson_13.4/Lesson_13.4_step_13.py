# 13.4 Функции с возвратом значения. Часть 1
"""
Merge lists 2

На вход программе подаются число n, а затем n строк, содержащих целые числа в порядке возрастания. Из данных строк формируются списки чисел. Напишите программу, которая объединяет указанные списки в один отсортированный список с помощью функции quick_merge(), а затем выводит его.

Формат входных данных
На вход программе подаются натуральное число n, а затем n строк, содержащих целые числа в порядке возрастания, разделённые символом пробела.

Формат выходных данных
Программа должна вывести элементы окончательного отсортированного списка каждое через пробел.

"""


def quick_merge(list1, list2):
    result = []

    p1 = 0
    p2 = 0

    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):
        result += list1[p1:]
    else:
        result += list2[p2:]

    return result


total_list = []
for i in range(int(input())):
    num = [int(q) for q in input().split()]
    result_new = quick_merge(total_list, num)
    total_list = result_new
print(*total_list)
