# 8.2 Итоговая работа по циклам
"""
Все вместе 2

Дано натуральное число. Напишите программу, которая вычисляет:

- количество цифр 3 в нем;
- сколько раз в нем встречается последняя цифра;
- количество четных цифр;
- сумму его цифр, больших пяти;
- произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
- сколько раз в нем встречаются цифры 0 и 5 (всего суммарно).

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести значения указанных величин в указанном порядке.

"""

n = int(input())
digit = 0
count_3 = 0
last_digit = n % 10
count_last_digit = 0
count_chet = 0
total_sum = 0
total_prod = 1
count_1_and_5_sum = 0

while n > 0:
    digit = n % 10
    if digit == 3:
        count_3 += 1
    if digit == last_digit:
        count_last_digit += 1
    if digit % 2 == 0:
        count_chet += 1
    if digit > 5:
        total_sum += digit
    if digit > 7:
        total_prod *= digit
    if digit == 0 or digit == 5:
        count_1_and_5_sum += 1
    n //= 10

print(count_3)
print(count_last_digit)
print(count_chet)
print(total_sum)
print(total_prod)
print(count_1_and_5_sum)



