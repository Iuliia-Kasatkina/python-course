# 9.3 Методы строк. Часть 1
"""
Хороший оттенок

На вход программе подается строка текста. Напишите программу, которая определяет является ли оттенок текста хорошим или нет. Текст имеет хороший оттенок, если содержит подстроку «хорош» во всевозможных регистрах.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести «YES» если текст имеет хороший оттенок и «NO» в противном случае.

Примечание. Текст содержащий хорош, ХОРОШ, Хорош, хОРОШ и т.д. имеет хороший оттенок.

"""

s = input()
s1 = 'Xорош'

if s1.lower() in s or s1.upper() in s or s1.swapcase() in s:
    print("YES")
else:
    print("NO")
