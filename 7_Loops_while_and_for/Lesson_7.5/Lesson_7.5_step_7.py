# 7.5 Цикл while: обработка цифр числа
"""
Все вместе

Дано натуральное число. Напишите программу, которая вычисляет:

- сумму его цифр;
- количество цифр в нем;
- среднее арифметическое его цифр;
- его первую цифру;
- сумму его первой и последней цифры.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести значения указанных величин в указанном порядке.

"""

n = int(input())
last_digit1 = 0
last_digit2 = 0
total1 = 0
count = 0
total2 = 1
medium = 0
first_digit = 0
total3 = 0

last_digit1 = n % 10

while n != 0:
    last_digit2 = n % 10
    total1 += last_digit2
    count += 1
    total2 *= last_digit2
    medium = total1 / count
    if n // 10 == 0:
        first_digit = n
    n = n // 10

total3 = first_digit + last_digit1

print(total1)
print(count)
print(total2)
print(medium)
print(first_digit)
print(total3)