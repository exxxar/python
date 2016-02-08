mystr="bla bla lalalal on ku rok"
print mystr
i=0
for el in mystr:
    
    for eltwo in mystr:
        if(el==eltwo):
            i+=1
        if(i==2):
            break
    if(i==1):
        print el
    i=0

