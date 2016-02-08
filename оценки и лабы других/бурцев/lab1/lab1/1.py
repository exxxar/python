# -*- coding: cp1251 -*-

age = raw_input('Сколько тебе лет, дружище?')
answer_age = int(age) % 10

if answer_age >=5 and answer_age <= 9 or answer_age ==0:
    print 'А, так тебе '+age+' лет, братюнь!'
elif answer_age == 1:
    
    print 'А, так тебе '+age+' год, братюнь!'
else:
    print 'А, так тебе '+age+' года, братюнь!'
