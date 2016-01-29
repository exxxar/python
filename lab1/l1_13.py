stroka = raw_input("Enter stroka=")
mass = stroka.split(' ')
buf = ""
index = 0
for k in mass:
    if k.strip()!="-" and len(k.strip())>0:
        buf += k+"("+str(index)+")"
    else:
        buf +=k
    index+=1
print buf
