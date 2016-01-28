# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Aleks"
__date__ = "$26.01.2016 17:59:14$"

stroka = raw_input("Enter url=")

if stroka.find("http://")!=-1:
    print stroka
    if (stroka.find(".com",len(stroka)-4)==-1):
        stroka += ".com"
        print stroka

if stroka.find("www")!=-1 and stroka.find("http://")==-1:
    stroka = "http://"+stroka
    print stroka
    if (stroka.find(".com",len(stroka)-4)==-1):
        stroka += ".com"
        print stroka
    
        


 