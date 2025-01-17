# 13.2 Функции с параметрами
"""
Сумма цифр

Напишите функцию print_digit_sum(), которая принимает одно натуральное число num и выводит на печать сумму его цифр.

"""


def print_digit_sum(num):
    total = 0
    n_new = str(n)
    for i in range(len(n_new)):
        total += int(n_new[i])
    print(total)


n = int(input())

print_digit_sum(n)