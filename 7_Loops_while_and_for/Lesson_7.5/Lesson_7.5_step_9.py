# 7.5 Цикл while: обработка цифр числа
"""
Одинаковые цифры

Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести «YES» если число состоит из одинаковых цифр и «NO» в противном случае.

"""

n = int(input())
flag = True
last_digit1 = 0
last_digit2 = 0
first_digit = 0
m = 0

m = n
while m != 0:
    last_digit1 = m % 10
    if m // 10 == 0:
        first_digit = m
    m = m // 10

while n // 10 != 0 and flag != False:
    last_digit2 = n % 10
    if last_digit2 != first_digit:
        flag = False
    else:
        flag = True
    n = n // 10

if flag == True:
    print("YES")
else:
    print("NO")






