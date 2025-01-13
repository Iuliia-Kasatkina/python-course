# 11.6 Методы списков. Часть 2
"""
Количество артиклей

На вход программе подаётся строка, содержащая английский текст. Напишите программу, которая подсчитывает общее количество артиклей: a, an, the.

Формат входных данных
На вход программе подаётся строка, содержащая английский текст. Слова текста разделены символом пробела.

Формат выходных данных
Программа должна вывести общее количество артиклей a, an, the вместе с поясняющим текстом.

Примечание. Артикли могут начинаться с заглавной буквы A, An, The.


"""

s = input()
total = 0

words = s.split()
for i in range(len(words)):
    if words[i].lower() in ['a', 'an', 'the']:
        total += 1

print('Общее количество артиклей:', total)