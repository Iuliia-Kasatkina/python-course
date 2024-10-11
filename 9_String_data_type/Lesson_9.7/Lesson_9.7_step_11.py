# 9.7 Строки в памяти компьютера, таблица символов Unicode
"""
Накручиваем стоимость ответа ⬆️🌶️

Как вы помните из прошлой задачи, модератору Сэму за каждый символ его сообщений в комментариях Тимур платит в 🐝 (пчелках-coin) по следующему тарифу:

<код символа в таблице Unicode>×3🐝

А стоимость всего сообщения складывается из суммы стоимостей всех символов. На этот раз Сэму захотелось схитрить и попробовать увеличить стоимость своего сообщения, заменив в нем некоторые английские буквы на русские. Как вы помните, русские буквы в таблице Unicode находятся после английских.

Сэм хочет заменить следующие английские буквы:

eyopaxcETOPAHXCBM
на соответствующие им русские буквы:

еуорахсЕТОРАНХСВМ
Тимур визуально разницу не заметит, а Сэм сможет зарабатывать больше пчелок-coin. 😊

На вход программе подается строка текста. Требуется написать программу, которая находит стоимость старого и нового сообщений Сэма в 🐝 и выводит текст в следующем формате:

Старая стоимость: <стоимость старого сообщения>🐝
Новая стоимость: <стоимость нового сообщения>🐝

Формат входных данных
На вход программе подается строка текста – очередной ответ Сэма в комментариях.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Обратите внимание, что если в строке не удается заменить буквы, то стоимость сообщения не изменится. 😢


"""

s = input()
total_old = 0
total_new = 0
alf_old = 'eyopaxcETOPAHXCBM'
alf_new = 'еуорахсЕТОРАНХСВМ'

for i in range(len(s)):
    total_old += ord(s[i]) * 3
print("Старая стоимость: ", total_old,"🐝", sep='')

for i in range(len(s)):
    if s[i] in alf_old:
        index = alf_old.find(s[i])
        s = s.replace(s[i], alf_new[index])

for i in range(len(s)):
    total_new += ord(s[i]) * 3
print("Новая стоимость: ", total_new,"🐝", sep='')