# 9.2 Срезы
"""
Палиндром
На вход программе подается одно слово, записанное в нижнем регистре. Напишите программу, которая определяет, является ли оно палиндромом.

Формат входных данных
На вход программе подается одно слово в нижнем регистре.

Формат выходных данных
Программа должна вывести «YES», если слово является палиндромом, и «NO» в противном случае.

Примечание. Палиндром считается слово, которое читается одинаково в обоих направлениях. Например, слово «потоп» является палиндромом.

"""

s = input()

s_new = s[::-1]
if s == s_new:
    print("YES")
else:
    print("NO")