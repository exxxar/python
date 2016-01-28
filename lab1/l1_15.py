
import re
print [str(k) for k in re.findall(r'(\b[A-Z][a-z]+\d{2})\b', raw_input("Enter stroka="))]