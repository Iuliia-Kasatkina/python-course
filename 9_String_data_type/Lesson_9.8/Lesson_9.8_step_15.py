# 9.8 Сравнение строк
"""
Сортируем слова 📶

На вход программе подаются 3 различных слова. Вам необходимо отсортировать эти слова по возрастанию в лексикографическом порядке и вывести их на одной строке, разделяя символом пробела.

Формат входных данных
На вход программе подаются 3 слова, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести 3 слова на одной строке, разделяя их символом пробела.


"""

s1 = input()
s2 = input()
s3 = input()
s_med = ''

if s1 != min(s1, s2, s3) and s1 != max(s1, s2, s3):
    s_med = s1
elif  s2 != min(s1, s2, s3) and s2 != max(s1, s2, s3):
    s_med = s2
else:
    s_med = s3

print(min(s1, s2, s3), s_med, max(s1, s2, s3))