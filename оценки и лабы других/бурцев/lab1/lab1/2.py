# -*- coding: cp1251 -*-
day = int(raw_input('������� ����'))
month = int(raw_input('������� �����'))
year = int(raw_input('������� ���'))
if day < 0 or month < 0 or year < 0:
    print('������� ������������� �����')
elif day>31 or month>12:
    print('������ � ����')
else:
    print('%02d/%02d/%4d')%(day,month,year)
