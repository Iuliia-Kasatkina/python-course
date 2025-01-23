# 13.5 Функции с возвратом значения. Часть 2
"""
Good password 🌶️

Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password
и возвращает значение True, если пароль является надёжным, или False в противном случае.

Пароль является надёжным, если:

его длина не менее 8 символов;
он содержит как минимум одну заглавную букву (верхний регистр);
он содержит как минимум одну строчную букву (нижний регистр);
он содержит хотя бы одну цифру.

Примечание. Приведённый ниже код:

print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))

должен выводить:

True
False

"""

def is_password_good(password):
    if len(password) >= 8 and password.islower() == False and password.isupper() == False and password.isalpha() == False and password.isdigit() == False and password.isalnum() == True:
        return True
    else:
        return False

txt = input()

print(is_password_good(txt))