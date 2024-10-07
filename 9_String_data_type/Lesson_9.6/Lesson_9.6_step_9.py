# 9.6 Форматирование строк
"""
Курсы валют 💹

Вследствие кибератаки на банк «Разбогатеем вместе» сломался алгоритм, выводящий курсы валют для определённой даты в мобильном приложении. Технический отдел банка просит вас исправить ситуацию и наладить вывод. На вход программе подаются следующие значения:

- дата (в формате ДД-ММ-ГГГГ)
- курс доллара (сколько российских рублей стоит 1 доллар)
- курс юаня (сколько российских рублей стоит 1 юань)

Напишите программу, которая выводит строку, показывающую, сколько российских рублей стоит 1 доллар и 1 юань на указанную дату в формате:

На <дата>: 1$ = <курс доллара>₽, 1¥ = <курс юаня>₽

Формат входных данных
На вход программе подаются три строки (каждая на новой строке): дата, курс доллара и курс юаня.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.


"""

date = input()
rate_dollar = input()
rate_uan = input()

text = f'На {date}: 1$ = {rate_dollar}₽, 1¥ = {rate_uan}₽'
print(text)