# 9.8 Сравнение строк
"""
Название класса 👩🏻‍🏫

В школе BEEGEEK названия учебных классов необычные. Они имеют следующий формат:

<номер класса><буква класса>
где <номер класса> должен находиться в диапазоне от 0 (как и все у программистов) до 9 включительно, а буквой класса могут быть все буквы в диапазоне от «А» до «П» включительно.

Напишите программу, которая принимает натуральное число n, а далее n названий классов, каждое на новой строке. Для каждого названия класса ваша программа должна выводить на отдельной строке «YES» (без кавычек), если название класса корректное, или «NO» (без кавычек) в противном случае.

Формат входных данных
На вход программе подается натуральное число n, а затем n названий классов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести на отдельной строке для каждого названия класса «YES» (без кавычек) или «NO» (без кавычек) в соответствии с условием задачи.

Примечание. Будем считать, что буквы Ё нет в русском алфавите, а значит, класс с такой буквой также будет считаться некорректным. 😢


"""

n = int(input())


for i in range(n):
    klass = input()
    if len(klass) == 2 and klass.isalnum() == True and  klass[1] != 'Ё' and 1040 <= ord(klass[1]) <= 1055:
        print('YES')
    else:
        print('NO')