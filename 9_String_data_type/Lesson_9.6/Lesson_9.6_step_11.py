# 9.6 Форматирование строк
"""
(Не) Активное похудение 🏃🌶️

Гвидо, засевший за компьютером и не ведущий активный образ жизни, «немного» поднабрал в весе. Осталось всего 60 дней до лета, а хочется быть в форме. Вот Гвидо и решился на похудение. Все дни до лета он пронумеровал от 1 до 60 (включительно). Перед началом похудения у Гвидо был вес 100 кг, а своей целью он поставил достичь веса 88 кг (или меньше). Он решил худеть на одну и ту же массу ежедневно.

Напишите программу, которая принимает на вход текущий день и текущий вес Гвидо. Программа должна вывести фразу:

«Все идет по плану» (без кавычек), если Гвидо удаётся держать планку в похудении и его вес ниже либо равен тому, который он запланировал на текущий день
«Что-то пошло не так» (без кавычек), если Гвидо не очень старается и его вес выше того, который он запланировал на текущий день
Также программа должна вывести информацию о номере дня похудения, текущем весе Гвидо и цели по весу на текущий день в формате:

#<номер дня> ДЕНЬ: ТЕКУЩИЙ ВЕС = <текущий вес Гвидо> кг, ЦЕЛЬ по ВЕСУ = <цель по весу на текущий день> кг

Формат входных данных
На вход программе подаются два числа (каждое на новой строке): номер дня похудения (целое число) и текущий вес Гвидо (действительное число).

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. В 1-й день похудения Гвидо уже должен похудеть (см. 1 тест).


"""

current_day = input()
current_weight = float(input())

day_weight_loss = (100 - 88) / 60
goal_weight = 100 - (day_weight_loss * float(current_day))
if float(current_weight) <= goal_weight:
    print('Все идет по плану')
else:
    print('Что-то пошло не так')
print(f'#{current_day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {current_weight} кг, ЦЕЛЬ по ВЕСУ = {goal_weight} кг')