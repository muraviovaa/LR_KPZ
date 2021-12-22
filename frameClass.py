# -*- coding: utf-8 -*-
"""
@author: stacie
"""

# !/usr/bin/python3
from tkinter import *
from tkinter import filedialog

top = Tk()
top.geometry("400x800")

A = []  # 

      
class Row:
    def __init__(self):
       self.Row = 0
    def addRow(self):
       self.Row = self.Row +1
    def getRow(self):
        return self.Row
    
class blockType:
    def __init__(self):
        self.BlockType = 1
    def setBlock(self,bn):
        self.BlockType = bn
    def getBlock(self):
        return self.BlockType


def getBlockNumber(event):
    print("EVENT ",event.widget)
    SelectWiget =str( event.widget)
  #     print(type(SelectWiget))
    print(SelectWiget)
    print("widget name:", str(event.widget).split(".!")[-1])
    commandNumber =str(event.widget).split(".!")[-1]
    commandNumber = commandNumber[5:]
    print(commandNumber)
    if commandNumber == "":
        BlockType = 1
    else:
        BlockType = int(commandNumber)
    print (BlockType)
    top.title("           блок №   "+str(BlockType))
    bt.setBlock(BlockType)    


def commandSelect(event):
#    makeEn()
    print(event)
    BlockType = bt.getBlock()
    if BlockType == 1 :
       command1()
      #  A.append(command1())
    if BlockType == 2:
        command2()
    if BlockType == 3:
        command3()
    if BlockType ==4 :
        command4()
    if BlockType == 5:
        command5()
    if BlockType == 6:
        command6()



def saveFile():
 
    for wid in frame2.winfo_children():
        wid.event_generate('<Button-2>')
    print("OUT List ",A)
    f= filedialog.asksaveasfile()
    for i in A:
        outstr =""
        for j in range(len(i)):
            outstr = outstr+str(i[j])+","
        outstr= outstr[:len(outstr)-1]
        f.write(outstr+"\n")  
    f.write("end")    
    f.close()
    

def halt():
    top.destroy()    


Frame1 = Frame(top,width=400,height=400,bg="light grey")   #   light grey
Frame1.pack(side=LEFT,fill=BOTH,expand=1,padx=40,pady=40)
frame2 = Frame(top,width=200,bg="SkyBlue1")  #   light grey 
frame2.pack(side=LEFT,fill=Y,expand=1,padx=10,pady=10)
# scrolly = Scrollbar(frame2, orient='vertical')   #, command=canvas.yview)
# scrolly.grid(row=0, column=1,rowspan=15,sticky='ns')
Label(Frame1,text=f"    Vi = Vj    ").pack(pady=10,anchor="w",padx=5)
Label(Frame1,text=f"    Vi = Cj    ").pack(pady=10,anchor="w",padx=5)
Label(Frame1,text=f"  input   Vi  ").pack(pady=10,anchor="w",padx=5)
Label(Frame1,text=f"  output Vi  ").pack(pady=10,anchor="w",padx=5)
Label(Frame1,text=f"  if  Vi==Cj  ").pack(pady=10,anchor="w",padx=5)
Label(Frame1,text=f"  if  Vi< Cj   ").pack(pady=10,anchor="w",padx=5)

for wid in Frame1.winfo_children():
      wid.bind("<Button-1>",getBlockNumber)
      # print(wid)
Frame1.bind("<Button-3>",commandSelect) 

mainmenu = Menu(top) 
top.config(menu=mainmenu) 

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Сохранить...",command=saveFile)
filemenu.add_command(label="Выход",command=halt)


mainmenu.add_cascade(label="Файл",  menu=filemenu)
      

class command1:
    
    def  __init__(self):
         self.setpoint()
    
    def setpoint(self):
        self.b = Frame(frame2,bg="ivory2",width = 250, height=60)
     #   self.b.place(x=self.x, y = self.y)
        self.b.config( bd = 6,relief= GROOVE)
        self.N=Entry(self.b,width = 6)
        self.N.grid(row=0,column=0)
        self.l2=Label(self.b,text="1")
        self.l2.grid(row=0,column=2)
        self.v1=Entry(self.b,width = 6) 
        self.v1.grid(row=1,column=1)
        Label(self.b,text="Vi=Vj").grid(row=1,column=2)
        self.v2=Entry(self.b,width = 6)
        self.v2.grid(row=1,column=3)

        print(row.getRow())    
        self.b.grid(column=0,row=row.getRow())
        row.addRow()
        self.b.bind("<Button-3>",self.BlockDelete)
        self.b.bind("<Button-2>",self.getValue)
        
        
    def BlockDelete(self,event):
 
        self.b.grid_remove()
        
    def getValue(self,event):
       
        B=[self.N.get(),self.l2.cget("text"),self.v1.get(),self.v2.get()]
        A.append(B)
    
        
class command2:
    def  __init__(self):
    
        self.setpoint()
        
    def setpoint(self):
        self.b = Frame(frame2,bg="ivory2",width = 250, height=60)
     #   self.b.place(x=self.x, y = self.y)
        self.b.config( bd = 6,relief= GROOVE)
        self.N=Entry(self.b,width = 6)
        self.N.grid(row=0,column=0)
        self.l2=Label(self.b,text="2")
        self.l2.grid(row=0,column=2)
        self.v1=Entry(self.b,width = 6) 
        self.v1.grid(row=1,column=1)
        Label(self.b,text="Vi=Cj").grid(row=1,column=2)
        self.v2=Entry(self.b,width = 6)
        self.v2.grid(row=1,column=3)

        print(row.getRow())    
        self.b.grid(column=0,row=row.getRow())
        row.addRow()
        self.b.bind("<Button-3>",self.BlockDelete)
        self.b.bind("<Button-2>",self.getValue) 
    
 
    def BlockDelete(self,event):
 
        self.b.grid_remove()
        
    def getValue(self,event):
  
        B=[self.N.get(),self.l2.cget("text"),self.v1.get(),self.v2.get()]
        A.append(B)

        
class command3:
    def  __init__(self):
         self.setpoint()
        
    def setpoint(self):
        self.b = Frame(frame2,bg="ivory2",width = 250, height=60)
     #   self.b.place(x=self.x, y = self.y)
        self.b.config( borderwidth = 6,relief= GROOVE)
      
        self.N=Entry(self.b,width = 6)
        self.N.grid(row=0,column=0)
        self.l2=Label(self.b,text="3")
        self.l2.grid(row=0,column=2)
        # self.v1=Entry(self.b,width = 6) 
        # self.v1.grid(row=1,column=1)
        Label(self.b,text="INPUT Vi").grid(row=1,column=2)
        self.v2=Entry(self.b,width = 6)
        self.v2.grid(row=1,column=3)

        print(row.getRow())    
        self.b.grid(column=0,row=row.getRow())
        row.addRow()
        self.b.bind("<Button-3>",self.BlockDelete)
        self.b.bind("<Button-2>",self.getValue)
    

    def BlockDelete(self,event):
 
        self.b.grid_remove()
        
    def getValue(self,event):
  
        B=[self.N.get(),self.l2.cget("text"),self.v2.get()]
        A.append(B)
 

        
class command4:
    def  __init__(self):
        self.setpoint()
        
    def setpoint(self):
        self.b = Frame(frame2,bg="ivory2",width = 250, height=60)
     #   self.b.place(x=self.x, y = self.y)
        self.b.config( bd = 6,relief= GROOVE)
        self.N=Entry(self.b,width = 6)
        self.N.grid(row=0,column=0)
        self.l2=Label(self.b,text="4")
        self.l2.grid(row=0,column=2)
        Label(self.b,text="OUTPUT Vj").grid(row=1,column=2)
        self.v2=Entry(self.b,width = 6)
        self.v2.grid(row=1,column=3)

        print(row.getRow())    
        self.b.grid(column=0,row=row.getRow())
        row.addRow()
        self.b.bind("<Button-3>",self.BlockDelete)
        self.b.bind("<Button-2>",self.getValue)
    

    def BlockDelete(self,event):
    
        self.b.grid_remove()
        
    def getValue(self,event):
 
        B=[self.N.get(),self.l2.cget("text"),self.v2.get()]
        A.append(B)
 
        
class command5:
    def  __init__(self):
        self.setpoint()
        
    def setpoint(self):
        self.b = Frame(frame2,bg="ivory2",width = 250, height=60)
     #   self.b.place(x=self.x, y = self.y)
        self.b.config( bd = 6,relief= GROOVE)
        self.N=Entry(self.b,width = 6)
        self.N.grid(row=0,column=0)
        self.N1=Entry(self.b,width = 6)
        self.N1.grid(row=1,column=0)
        self.l2=Label(self.b,text="5")
        self.l2.grid(row=0,column=2)
        self.v1=Entry(self.b,width = 6) 
        self.v1.grid(row=1,column=1)
        Label(self.b,text="Vi==Cj").grid(row=1,column=2)
        self.v2=Entry(self.b,width = 6)
        self.v2.grid(row=1,column=3)

        print(row.getRow())    
        self.b.grid(column=0,row=row.getRow())
        row.addRow()
        self.b.bind("<Button-3>",self.BlockDelete)
        self.b.bind("<Button-2>",self.getValue)
    

    def BlockDelete(self,event):

        self.b.grid_remove()
        
        
    def getValue(self,event):
  
     
        B=[self.N.get(),self.N1.get(),self.l2.cget("text"),self.v1.get(),self.v2.get()]
        A.append(B)

 
        

class command6:
    def  __init__(self):
        self.setpoint()
        
    def setpoint(self):
        self.b = Frame(frame2,bg="ivory2",width = 250, height=60)
     #   self.b.place(x=self.x, y = self.y)
        self.b.config( bd = 6,relief= GROOVE)
        self.N=Entry(self.b,width = 6)
        self.N.grid(row=0,column=0)
        self.N1=Entry(self.b,width = 6)
        self.N1.grid(row=1,column=0)
        self.l2=Label(self.b,text="6")
        self.l2.grid(row=0,column=2)
        self.v1=Entry(self.b,width = 6) 
        self.v1.grid(row=1,column=1)
        Label(self.b,text="Vi < Cj").grid(row=1,column=2)
        self.v2=Entry(self.b,width = 6)
        self.v2.grid(row=1,column=3)

        print(row.getRow())    
        self.b.grid(column=0,row=row.getRow())
        row.addRow()
        self.b.bind("<Button-3>",self.BlockDelete)
        self.b.bind("<Button-2>",self.getValue)
    


    def BlockDelete(self,event):
 
        self.b.grid_remove()
        
    def getValue(self,event):
  
        B=[self.N.get(),self.N1.get(),self.l2.cget("text"),self.v1.get(),self.v2.get()]
        A.append(B)
        
 

row = Row()
bt = blockType()
mainloop()