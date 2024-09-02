# 9.3 Методы строк. Часть 1
"""
Заглавные буквы

На вход программе подаётся строка, состоящая из имени и фамилии человека, разделённых одним пробелом. Напишите программу, которая проверяет, что имя и фамилия начинаются с заглавной буквы.

Формат входных данных
На вход программе подаётся строка.

Формат выходных данных
Программа должна вывести «YES», если имя и фамилия начинаются с заглавной буквы, или «NO» в противном случае.

Примечание. Строка содержит только буквы и символ пробела.

"""

s = input()

if s == s.title():
    print("YES")
else:
    print("NO")