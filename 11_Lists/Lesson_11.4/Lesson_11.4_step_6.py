# 11.4 Вывод элементов списка
"""
Google search - 1

На вход программе подается натуральное число n, затем n строк, затем еще одна строка — поисковый запрос. Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.

Формат входных данных
На вход программе подаются натуральное число n — количество строк, затем сами строки в указанном количестве, затем один поисковый запрос.

Формат выходных данных
Программа должна вывести все введенные строки, в которых встречается поисковый запрос.

Примечание. Поиск не должен быть чувствителен к регистру символов.


"""

n = int(input())
list = []

for i in range(n):
    p = input()
    list.append(p)

s = input()

for i in range(len(list)):
    if s.lower() in list[i].lower():
        print(list[i])