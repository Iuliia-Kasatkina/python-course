# 6.2 Строковый тип данных
"""
Три города 🏙️

Даны названия трёх городов. Напишите программу, которая определяет самое короткое и самое длинное название города.

Формат входных данных
На вход программе подаются названия трёх городов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.

Примечание. Гарантируется, что длины названий всех трёх городов различны.

"""

city1, city2, city3 = input(), input(), input()

short_name = min(len(city1), len(city2), len(city3))
long_name = max(len(city1), len(city2), len(city3))

if len(city1) == short_name:
    print(city1)
elif len(city2) == short_name:
    print(city2)
else:
    print(city3)

if len(city1) == long_name:
    print(city1)
elif len(city2) == long_name:
    print(city2)
else:
    print(city3)