# 9.5 Методы строк. Часть 3
"""
Плохие комментарии 😈

На платформе Stepik пользователи оставляют комментарии, но не все из них соответствуют правилам. Так, например, модератор Сэм считает неуместными комментарии те, которые представляют собой пустую строку или состоят только из пробелов. Подобные комментарии он удаляет – нечего засорять курс бесполезным материалом!

Ваша задача – написать программу, которая поможет Сэму проверять комментарии. Программа должна принимать на вход натуральное число n, а затем n строк, представляющих тексты комментариев. Для каждого комментария ваша программа должна выводить номер этого комментария (начиная с 1), затем двоеточие (:), затем через пробел его текст или сообщение «COMMENT SHOULD BE DELETED» (без кавычек), если комментарий должен быть удалён Сэмом.

Формат входных данных
На вход программе подаётся одно натуральное число n, а затем – n строк.

Формат выходных данных
Для каждого комментария программа должна вывести его текст или сообщение «COMMENT SHOULD BE DELETED», если комментарий должен быть удалён.

"""

n = int(input())

for i in range(1, n+1):
    s = input()
    if s.isspace() == True or s == '':
        print(i,':',' COMMENT SHOULD BE DELETED', sep='')
    else:
        print(i,':', ' ', s, sep='')


