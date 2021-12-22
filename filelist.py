# -*- coding: utf-8 -*-
"""
@author: staie
"""

import copy     #import *
#from copy import deepcopy
import sys


b=[]
a=[1,2,3,4]
c= [1,2,3,4,4]
y=[]
d =[]
line=''
f = open("C:/Users/nat/emulator.txt","r") 
line = f.readline()

while True:
     line = f.readline()
     if not line:
      #  print("end of file") 
        break
     
     if line.find('end')>=0 :
       # print("end found")
        #print("d  ",d)
        b.append(d)
       # print("b   ",b)
        y = copy.deepcopy(b)
        b.clear()
        b=copy.deepcopy(y)
        #print("b   ",b)
        d.clear()
        #print("d  ",d)
        #print("b   ",b)
     else:
         line=line[:len(line)-1]
         #print("line  ",line)
         d.append(line)
f.close()   
print("p= ",b)
print()
print()
print()
print()
f = open("C:/Users/nat/shapka.txt","r") 
o = open("C:/Users/nat/result.py","w") 
line = f.readline()
for line in f:
     line
     o.write(line)
f.close()
o.close()     
o = open("C:/Users/nat/result.py","a") 
#print("p= ",b)
print("#############",file=o)
print("p=[",file=o)
for i in b:
    print(i,",",file=o)
print("]",file=o)  
o.close()
f = open("C:/Users/nat/podval.txt","r") 
o = open("C:/Users/nat/result.py","a") 
line = f.readline()
for line in f:
     line
     o.write(line)
f.close()
o.close()     
     