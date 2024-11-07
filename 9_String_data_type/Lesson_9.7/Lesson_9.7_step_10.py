# 9.7 Строки в памяти компьютера, таблица символов Unicode
"""
Стоимость ответа 💬

Модератору Сэму за каждый символ его сообщений в комментариях Тимур платит в 🐝 (пчелках-coin) по следующему тарифу:

<код символа в таблице Unicode>×3🐝

А стоимость всего сообщения складывается из суммы стоимостей всех символов. Сэму захотелось подсчитать, сколько 🐝 он зарабатывает за свои ответы в комментариях, и просит вас помочь ему.

На вход программе подается строка текста. Требуется написать программу, которая находит стоимость сообщения Сэма в 🐝 и выводит текст в следующем формате:

Текст сообщения: '<текст сообщения Сэма>'
Стоимость сообщения: <стоимость сообщения Сэма>🐝

Формат входных данных
На вход программе подается строка текста – очередной ответ Сэма в комментариях.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. 🐝 (пчелка-coin) – виртуальная валюта команды BEEGEEK, которой Тимур расплачивается со своими сотрудниками.


"""

s = input()
total = 0

for i in range(len(s)):
    total += ord(s[i]) * 3

print("Текст сообщения: ", "'", s, "'", sep='')
print("Стоимость сообщения: ", total,"🐝", sep='')