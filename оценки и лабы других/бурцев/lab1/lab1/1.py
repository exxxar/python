# -*- coding: cp1251 -*-

age = raw_input('������� ���� ���, �������?')
answer_age = int(age) % 10

if answer_age >=5 and answer_age <= 9 or answer_age ==0:
    print '�, ��� ���� '+age+' ���, �������!'
elif answer_age == 1:
    
    print '�, ��� ���� '+age+' ���, �������!'
else:
    print '�, ��� ���� '+age+' ����, �������!'
