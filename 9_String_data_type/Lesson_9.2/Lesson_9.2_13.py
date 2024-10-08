# 9.2 Срезы
"""
Делаем срезы 2

На вход программе подается одна строка. Напишите программу, которая выводит:

- третий символ этой строки;
- предпоследний символ этой строки;
- первые пять символов этой строки;
- всю строку, кроме последних двух символов;
- все символы с четными индексами;
- все символы с нечетными индексами;
- все символы в обратном порядке;
- все символы строки через один в обратном порядке, начиная с последнего.

Формат входных данных
На вход программе подается одна строка, длина которой больше 5 символов.

Формат выходных данных
Программа должна вывести данные в соответствии с условием. Каждое значение выводится на отдельной строке.

"""

s = input()

print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
