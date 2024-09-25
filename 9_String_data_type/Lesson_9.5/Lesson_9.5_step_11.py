# 9.4 Методы строк. Часть 2
"""
Проверь никнейм 👩🌶️

Во время собеседования вам предложили решить задачу на валидацию имени пользователя. Пользователь пытается создать никнейм для своего аккаунта в соцсети Y. Правила для корректного никнейма в соцсети Y следующие:

- никнейм должен начинаться с символа @
- никнейм должен содержать от 5 до 15 (включительно) символов (включая первый символ @)
- никнейм должен содержать только строчные буквы и цифры (помимо первого символа @)

Напишите программу, которая выводит «Correct» (без кавычек), если никнейм соответствует всем вышеприведенным правилам, или «Incorrect» (без кавычек) в противном случае.

Формат входных данных
На вход программе подаётся одна строка – никнейм.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Обратите внимание, что никнейму необязательно содержать строчные буквы и цифры одновременно, никнейм может содержать только строчные буквы или только цифры (помимо первого символа @). Например, следующие никнеймы считаются корректными:

@duncan
@1111

"""

nickname = input()

nickname1 = nickname[1:]
if nickname.startswith('@') and 5 <= len(nickname) <= 15 and nickname1.isalnum() == True and (nickname1.islower() == True or nickname1.isdigit() == True):
    print('Correct')
else:
    print('Incorrect')