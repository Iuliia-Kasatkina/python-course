# 9.4 Методы строк. Часть 2
"""
.com or .ru

На вход программе подается строка текста. Напишите программу, которая проверяет, что строка заканчивается подстрокой .com или .ru.

Формат входных данных
На вход программе подаётся строка текста.

Формат выходных данных
Программа должна вывести «YES», если введённая строка заканчивается подстрокой .com или .ru, или «NO» в противном случае.

"""

s = input()

if s.endswith('.com') == True or s.endswith('.ru') == True:
    print('YES')
else:
    print('NO')