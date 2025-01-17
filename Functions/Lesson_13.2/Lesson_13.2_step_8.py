# 13.2 Функции с параметрами
"""
Звёздный треугольник

Напишите функцию draw_triangle(fill, base), которая принимает два параметра:

fill – символ заполнитель;
base – величина основания равнобедренного треугольника;
а затем выводит его.

Примечание. Гарантируется, что основание треугольника – нечётное число.

"""

def draw_triangle(fill, base):
    count = 0
    for i in range(1, base+1):
        if i <= (base+1) // 2:
            count += 1
            print(fill * count)
        else:
            count -= 1
            print(fill * count)

fill = input()
base = int(input())

draw_triangle(fill, base)