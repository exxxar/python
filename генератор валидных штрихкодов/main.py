# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os

FONT_PATH = "segoe.ttf"
group_A = {
    '0': '0001101',
    '1': '0011001',
    '2': '0010011',
    '3': '0111101',
    '4': '0100011',
    '5': '0110001',
    '6': '0101111',
    '7': '0111011',
    '8': '0110111',
    '9': '0001011',
    }
group_B = {
    '0': '0100111',
    '1': '0110011',
    '2': '0011011',
    '3': '0100001',
    '4': '0011101',
    '5': '0111001',
    '6': '0000101',
    '7': '0010001',
    '8': '0001001',
    '9': '0010011',
    }
group_C = {
    '0': '1110010',
    '1': '1100110',
    '2': '1101100',
    '3': '1000010',
    '4': '1011100',
    '5': '1001110',
    '6': '1010000',
    '7': '1000100',
    '8': '1001000',
    '9': '1110100',
    }
combination = {
    '0':'AAAAAA',
    '1':'AABABB',
    '2':'AABBAB',
    '3':'AABBBA',
    '4':'ABAABB',
    '5':'ABBAAB',
    '6':'ABBBAA',
    '7':'ABABAB',
    '8':'AAABBA',
    '9':'ABBABA'
    }


def draw(code,path_f):
    image = Image.new("RGB", (120, 63), (255, 255, 255))
    draw = ImageDraw.Draw(image)  
    
    comb = code[0]
    part_1 = code[1:7:1]
    part_2 = code[7:13:1]

    path = combination[comb]
    index = 0
    step = 10
    step += 2
    draw.line((step, 0, step, 55), fill=(0, 0, 0))
    step += 2
    draw.line((step, 0, step, 55), fill=(0, 0, 0))
    step += 1
    print comb+"["+part_1+"]["+part_2+"]["+path+"CCCCCC]"
    for i in path:      
        if i == 'A':            
            for k in group_A[part_1[index]]:
                if (k == '1'):
                    draw.line((step, 0, step, 45), fill=(0, 0, 0))
                if (k == '0'):
                    draw.line((step, 0, step, 45), fill=(255, 255, 255))
                step += 1
        if i == 'B':
            for k in group_B[part_1[index]]:
                if (k == '1'):
                    draw.line((step, 0, step, 45), fill=(0, 0, 0))
                if (k == '0'):
                    draw.line((step, 0, step, 45), fill=(255, 255, 255))
                step += 1
        index += 1

    step += 1
    draw.line((step, 0, step, 55), fill=(0, 0, 0))
    step += 2
    draw.line((step, 0, step, 55), fill=(0, 0, 0))  
    step += 2
    
    index = 0
    while index < 6:
        for k in group_C[part_2[index]]:
            if (k == '1'):
                draw.line((step, 0, step, 45), fill=(0, 0, 0))
            if (k == '0'):
                draw.line((step, 0, step, 45), fill=(255, 255, 255))
            step += 1
        index += 1

    step += 1
    draw.line((step, 0, step, 55), fill=(0, 0, 0))
    step += 2
    draw.line((step, 0, step, 55), fill=(0, 0, 0))

    font = ImageFont.truetype(FONT_PATH, 16)
    draw.text((3, 45), comb, (1, 1, 1), font=font)
    draw.text((16, 45), part_1, (1, 1, 1), font=font)
    draw.text((62, 45), part_2, (1, 1, 1), font=font)

    image.save(path_f, "JPEG")
    #image.show()   
    del draw
    return 0

def recSearch(t):
    t+=1
    if t%10==0:
        return t
    else:        
        t = recSearch(t)
    return t

def recAdd(x):
    if (len(x)<5):
        x="0"+x
        x = recAdd(x)
    return x        
        
def checksum(x):
    i = 1
    sum_1 = 0
    sum_2 = 0
    while i<len(x):
        sum_1+=int(x[i])
        i+=2
    i=0
    while i<len(x)-1:
        sum_2+=int(x[i])
        i+=2
    sum_2 *=3
    sum_1 +=sum_2
    return recSearch(sum_1)-sum_1

def format(x,n):
    if (len(x)<int(n)):
        x = "0"+x
        x = format(x,n)
    return x

country = "460"#3    
    
while True:
     try:
            country = raw_input("country_code[3]:")#"460"#3
            if int(country)>0 and int(country)<=999:
                country = format(country,3)
                break
            else:
                print "Must be in range 001..999"
     except ValueError:
            print "Bad Number"            

codeBusiness = "0045"#4

while True:
     try:
            codeBusiness = raw_input("code business[4]:")#"0045"#4
            if int(codeBusiness)>0 and int(codeBusiness)<=9999:
                codeBusiness = format(codeBusiness,4)
                break
            else:
                print "Must be in range 0001..9999"
     except ValueError:
            print "Bad Number"

N = 301
while True:
     try:
            N = int(raw_input("count codes[0..99999]:")) 
            if N>0 and N<=99999:
                break
            else:
                print "Must be in range 0001..99999"
     except ValueError:
            print "Bad Number"

if not os.path.isdir("codes"):
    try:
        os.makedirs('codes')
    except OSError:
        pass
        print "Error creating direcory [codes]"
index = 1


while index<=N:
    codeProduct = recAdd(str(index))#5
    draw(country+codeBusiness+codeProduct+str(checksum(country+codeBusiness+codeProduct)),"codes\\"+str(index)+".jpg")
    index+=1