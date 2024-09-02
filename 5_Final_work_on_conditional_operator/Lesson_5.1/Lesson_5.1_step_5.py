# 5.1 Задачи на программирование
"""
YES or NO вот в чем вопрос

Напишите программу, которая принимает на вход число и в зависимости от условий выводит текст «YES», либо «NO».

Условия:

- если число нечётное, то вывести «YES»;
- если число чётное в диапазоне от 2 до 5 (включительно), то вывести «NO»;
- если число чётное в диапазоне от 6 до 20 (включительно), то вывести «YES»;
- если число чётное и больше 20, то вывести «NO».

Формат входных данных
На вход программе подаётся натуральное число.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

"""

num = int(input())

if num % 2 == 0:
    if 2 <= num <= 5 or num > 20:
        print("NO")
    else:
        if 6 <= num <= 20:
            print("YES")
else:
    print("YES")