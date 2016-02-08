# -*- coding: cp1251 -*-

try:
    karta=raw_input('Введите 16 цифр дебетовой карты')
    if len(karta)!=16:
        raise ValueError('Не корректное число для карты.Введите 16 цифр')
    print karta[0:4]+"*"*8+karta[12:16]

except ValueError,e:
    print e
