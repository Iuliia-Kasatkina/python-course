# 9.1 Индексация
"""
ФИО

На вход программе подаются три строки: имя, фамилия и отчество (именно в таком порядке). Напишите программу, которая выводит инициалы человека.

Формат входных данных
На вход программе подаются три строки, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести ФИО человека.

Примечание. Гарантируется, что имя, фамилия и отчество начинаются с заглавной буквы.

"""

name, surname1, surname2 = input(), input(), input()

print(surname1[0] + name[0] + surname2[0])