# 7.4 Цикл while
"""
Количество пятёрок 5️⃣

На вход программе подается последовательность целых чисел от 1 до 5, характеризующее оценку ученика, каждое число на отдельной строке. Концом последовательности является любое неположительное число либо число, большее
5. Напишите программу, которая выводит количество пятерок.

Формат входных данных
На вход программе подается последовательность чисел, каждое число на отдельной строке.

Формат выходных данных
Программа должна вывести количество пятерок.

Примечание. Не забываем, что неположительными числами являются все отрицательные числа и число 0.

"""

num = int(input())
count = 0

while 0 < num <= 5:
    if num == 5:
        count += 1
    num = int(input())

print(count)
