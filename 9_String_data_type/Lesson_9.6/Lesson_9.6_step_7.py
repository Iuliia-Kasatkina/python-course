# 9.6 Форматирование строк
"""
Используя метод format(), дополните приведённый код так, чтобы он вывел текст:

In 2010, someone paid 10k Bitcoin for two pizzas.

Исходный код:

s = 'In {0}, someone paid {1} {2} for two pizzas.'

print()


"""

year = 2010
summa = '10k'
currency = 'Bitcoin'

s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(year, summa, currency)

print(s)