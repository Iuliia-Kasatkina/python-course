# 11.2 Основы работы со списками
"""
Дополните приведенный код так, чтобы элемент списка имеющий значение Green заменился на значение Зеленый, а элемент Violet на Фиолетовый. Далее необходимо вывести полученный список.

Исходный код

rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']


print()


"""

rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

rainbow[::3] = ['Red','Зеленый','Фиолетовый']

print(rainbow)