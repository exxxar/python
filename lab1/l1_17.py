# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import hashlib
import os
cwd = os.getcwd()
print cwd

print [str(k) for k in  os.listdir("c:\\1\\")]

f = open('c:\\1\\my_file.txt', 'r' )
data = f.read()
f.close()
checksum = hashlib.md5(data).hexdigest()
print checksum

f = open('c:\\1\\my_file2.txt', 'r' )
data = f.read()
f.close()
checksum = hashlib.md5(data).hexdigest()
print checksum