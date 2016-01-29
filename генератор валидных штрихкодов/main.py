# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

FONT_PATH = "c:\\1\\segoe.ttf"
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
group_C = {
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
    for i in path:
        print i    
        if i == 'A':
            print group_A[part_1[index]]
            for k in group_A[part_1[index]]:
                if (k == '1'):
                    draw.line((step, 0, step, 45), fill=(0, 0, 0))
                if (k == '0'):
                    draw.line((step, 0, step, 45), fill=(255, 255, 255))
                step += 1
        if i == 'B':
            print group_B[part_1[index]]
            for k in group_B[part_1[index]]:
                if (k == '1'):
                    draw.line((step, 0, step, 45), fill=(0, 0, 0))
                if (k == '0'):
                    draw.line((step, 0, step, 45), fill=(255, 255, 255))
                step += 1
        index += 1

    step += 2
    draw.line((step, 0, step, 55), fill=(0, 0, 0))
    step += 2
    draw.line((step, 0, step, 55), fill=(0, 0, 0))  
    step += 1
    
    index = 0
    while index < 6:
        print "C"
        print group_C[part_2[index]]
        for k in group_C[part_2[index]]:
            if (k == '1'):
                draw.line((step, 0, step, 45), fill=(0, 0, 0))
            if (k == '0'):
                draw.line((step, 0, step, 45), fill=(255, 255, 255))
            step += 1
        index += 1

    step += 2
    draw.line((step, 0, step, 55), fill=(0, 0, 0))
    step += 2
    draw.line((step, 0, step, 55), fill=(0, 0, 0))

    font = ImageFont.truetype(FONT_PATH, 16)
    draw.text((3, 45), comb, (1, 1, 1), font=font)
    draw.text((15, 45), part_1, (1, 1, 1), font=font)
    draw.text((63, 45), part_2, (1, 1, 1), font=font)

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
    
    
country = "460"#3
codeBusiness = "0045"#4

index = 1
N = 301

while index<N:
    codeProduct = recAdd(str(index))#5
    draw(country+codeBusiness+codeProduct+str(checksum(country+codeBusiness+codeProduct)),"c:\\1\\codes\\"+str(index)+".jpg")
    index+=1