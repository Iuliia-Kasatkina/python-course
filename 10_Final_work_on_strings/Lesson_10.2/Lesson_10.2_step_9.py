# 10.2 Итоговая работа по строкам
"""
Удали меня полностью ❌

На вход программе подается строка текста. Напишите программу, которая удаляет все вхождения символа «@».

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

"""

s = input()
s_new = ''

for i in range(len(s)):
    if s[i] != '@':
        s_new += s[i]

print(s_new)

