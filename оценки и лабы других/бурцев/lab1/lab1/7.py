# -*- coding: cp1251 -*-

try:
    karta=raw_input('������� 16 ���� ��������� �����')
    if len(karta)!=16:
        raise ValueError('�� ���������� ����� ��� �����.������� 16 ����')
    print karta[0:4]+"*"*8+karta[12:16]

except ValueError,e:
    print e
