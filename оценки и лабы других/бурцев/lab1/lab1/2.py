# -*- coding: cp1251 -*-
day = int(raw_input('Введите день'))
month = int(raw_input('Введите месяц'))
year = int(raw_input('Введите год'))
if day < 0 or month < 0 or year < 0:
    print('Введите положительные числа')
elif day>31 or month>12:
    print('Ошибка в дате')
else:
    print('%02d/%02d/%4d')%(day,month,year)
