# -*- coding: cp1251 -*-
import re

mystr = "«Petr93», «JohFny70», «Service023» vasya34 43 CV34"
print mystr
print re.findall(r'\b[[A-Z][a-z][a-zA-Z]+\d{2}\b',mystr)
