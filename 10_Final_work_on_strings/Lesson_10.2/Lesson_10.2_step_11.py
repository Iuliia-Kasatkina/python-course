# 10.2 Итоговая работа по строкам
"""
Переворот 🙃

На вход программе подается строка текста, в которой буква «h» встречается как минимум два раза. Напишите программу, которая возвращает исходную строку и переворачивает последовательность символов, заключенную между первым и последним вхождением буквы «h».

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

"""

s = input()

s = s[:s.find('h')] + s[s.rfind('h'):s.find('h'):-1] + s[s.rfind('h'):]
print(s)