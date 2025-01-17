# 13.2 Функции с параметрами
"""
ФИО

Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:

name – имя человека;
surname – фамилия человека;
patronymic – отчество человека;
а затем выводит на печать ФИО человека.

Примечание. Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.

"""

def print_fio(name, surname, patronymic):
    print(surname.capitalize()[0]+name.capitalize()[0]+patronymic.capitalize()[0])

name, surname, patronymic = input(), input(), input()

print_fio(name, surname, patronymic)