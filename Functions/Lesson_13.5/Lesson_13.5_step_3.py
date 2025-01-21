# 13.5 Функции с возвратом значения. Часть 2
"""
Is the Number Prime? 🌶️

Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True, если число является простым, или False в противном случае.

Примечание. Приведённый ниже код:

print(is_prime(1))
print(is_prime(10))
print(is_prime(17))

должен выводить:

False
False
True

"""


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input())

print(is_prime(n))

