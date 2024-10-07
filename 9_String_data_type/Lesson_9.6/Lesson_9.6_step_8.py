# 9.6 Форматирование строк
"""
Используя f-строку, дополните приведённый код так, чтобы он вывел текст:

In 2010, someone paid 10K Bitcoin for two pizzas.

Исходный код:

s = 'In {}, someone paid {} {} for two pizzas.'

print()


"""

year = 2010
summa = '10K'
currency = 'Bitcoin'

s = f'In {year}, someone paid {summa} {currency} for two pizzas.'
print(s)