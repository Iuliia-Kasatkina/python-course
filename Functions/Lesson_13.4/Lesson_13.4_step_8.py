# 13.4 Функции с возвратом значения. Часть 1
"""
Делители 1

Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и возвращающую список всех делителей данного числа.

Примечание. Приведённый ниже код:

print(get_factors(1))
print(get_factors(5))
print(get_factors(10))

должен выводить:

[1]
[1, 5]
[1, 2, 5, 10]

"""

def get_factors(num):
    result = []
    for i in range(1, num+1):
        if num % i == 0:
            result.append(i)
    return result

n = int(input())

print(get_factors(n))