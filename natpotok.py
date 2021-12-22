# -*- coding: utf-8 -*-
"""
@author: stacie
"""

import threading
#from numba import jit
#@jit

mutex = threading.Lock()


GlobalConstant = {'c1':5 ,'c2':3}
GlobalVariable = {'v1':8,'v2':2,'v3':9}

p=[["1,2,v1,c1","2,1,v1,v3","3,4,v2","4,5,1,v2,c1","5,4,v3","6,6,2,v3,c1"],
   ["1,2,v1,c1","2,1,v1,v3","3,4,v2"]]

class emulator:
    
    def __init__( self,mylist ):
        
        self.pro = mylist
    
 
    
    def MakeProg(self):
        self.i=0
        while self.i<len(self.pro):
            self.command = self.pro[self.i]
            print(self.i,'   ',self.command)
            self.com =  self.parse(self.command)
            # print(self.i)   
            # a  = input()
            if self.com == 0:
                self.i=self.i+1
            else:
                self.i=self.com

    def parse(self,kod):
        num = kod.find(",")
        opnum = kod[:num]
        kod = kod[num+1:]
        num = kod.find(",")
        oper = kod[:num]
        if (oper == '2'):  #  vi=cj
            kod = kod[num:]
            op1 = kod[kod.find(",")+1:kod.find(",",kod.find(",")+1)]
            kod = kod[kod.find(",",kod.find(",")+1)+1:]
# make operation
            mutex.acquire()
            GlobalVariable[op1]= GlobalConstant[kod]    
            mutex.release()
            return 0

        if (oper == '1'):  #    vi=vj
            kod = kod[num:]
            op1 = kod[kod.find(",")+1:kod.find(",",kod.find(",")+1)]
            kod = kod[kod.find(",",kod.find(",")+1)+1:]
#make operation
            mutex.acquire()
            GlobalVariable[op1]= GlobalVariable[kod]    
            mutex.release()
            return 0


        if (oper == '3'):  #  input  vi
            kod = kod[num:]
            op1 = kod[kod.find(",")+1:]
#make operation
            print("введи значение ",op1)
            a=input()     
            mutex.acquire()
            GlobalVariable[op1] =a
            mutex.release()
            return 0

        if (oper == '4'):  # input ci
            kod = kod[num:]
            mutex.acquire()
            op1 = kod[kod.find(",")+1:]
#make operation
            mutex.release()
            return 0
    
        if (oper == '5'):  # условие равно
            kod = kod[num+1:]
            com1 = kod.find(',')
            cc =int( kod[:com1])
            kod = kod[com1+1:]
            com1 = kod.find(',')
            op1 = kod[:com1]
            op2 = kod[com1+1:]
#   make compare
            mutex.acquire()
            if op1 == op2 :
                mutex.release()
                return cc
            else:
                mutex.release()
                return 0


        if (oper == '6'):  # условие меньше
            kod = kod[num+1:]
            com1 = kod.find(',')
            сс = cc =int( kod[:com1])
            kod = kod[com1+1:]
        
            com1 = kod.find(',')
            op1 = kod[:com1]
            op2 = kod[com1+1:]
#   make compare
            mutex.acquire()
            if GlobalVariable[op1] < GlobalConstant[op2] : 
                mutex.release()   
                return cc
            else:
                mutex.release()  
                return 0            
            
            
            
A=[]
th=[]
k=0            
for i in p:
    print(i)        
    B = emulator(i)
    A.append(B)
    thread = threading.Thread(target=A[k].MakeProg()) 
    th.append(thread)  
    th[k].start()  
    k=k+1    
s = k-1
print(s)    
for k in range(len(p)):
    th[k].join()
    
   