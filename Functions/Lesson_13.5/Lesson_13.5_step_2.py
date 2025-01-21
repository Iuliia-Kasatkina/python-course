# 13.5 Функции с возвратом значения. Часть 2
"""
Is the Triangle Valid?

Напишите функцию is_valid_triangle(side1, side2, side3), которая принимает в качестве аргументов три натуральных числа, и возвращает значение True, если существует невырожденный треугольник со сторонами side1, side2, side3, или False в противном случае.

Примечание 1. С данной задачей мы уже сталкивались при изучении условного оператора.

Примечание 2. Приведённый ниже код:

print(is_valid_triangle(2, 2, 2))
print(is_valid_triangle(2, 3, 10))
print(is_valid_triangle(3, 4, 5))

должен выводить:

True
False
True

"""

def is_valid_triangle(side1, side2, side3):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

a, b, c = int(input()), int(input()), int(input())

print(is_valid_triangle(a, b, c))