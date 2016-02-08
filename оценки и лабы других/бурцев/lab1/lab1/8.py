# -*- coding: cp1251 -*-
row = raw_input('Введите строку: ')
#row ="I live very long time and for me will just good.I say abrakadabra"
listrow =row.split(' ')
print listrow
big= []
middle = []
small = []
for item in listrow:
    if(len(item)>7):
        big.append(item)
    elif(len(item)>=4 and len(item)<=7):
        middle.append(item)
    else:
        small.append(item)

print "Слова больше 7 символов\n"
print big
print "Слова от 4 до 7 символов\n"
print middle
print "Слова остальные \n"
print small
